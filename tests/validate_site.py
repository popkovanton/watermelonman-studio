#!/usr/bin/env python3
"""Dependency-free structural validation for the static website."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
ROUTES = {
    "/": PUBLIC / "index.html",
    "/privacy/": PUBLIC / "privacy/index.html",
    "/support/": PUBLIC / "support/index.html",
}
SITE_URL = "https://watermelonman.studio"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: dict[str, int] = {}
        self.attrs: list[tuple[str, dict[str, str]]] = []
        self.h1_count = 0
        self.in_title = False
        self.title = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags[tag] = self.tags.get(tag, 0) + 1
        values = {key: value or "" for key, value in attrs}
        self.attrs.append((tag, values))
        if tag == "h1":
            self.h1_count += 1
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


def fail(message: str) -> None:
    raise AssertionError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def local_target(url: str) -> Path | None:
    parsed = urlparse(url)
    if parsed.scheme or parsed.netloc or url.startswith(("mailto:", "tel:", "#")):
        return None
    path = parsed.path
    if not path:
        return None
    target = PUBLIC / path.lstrip("/")
    if path.endswith("/"):
        target /= "index.html"
    return target


def validate_page(route: str, path: Path) -> None:
    require(path.is_file(), f"Missing route {route}: {path.relative_to(ROOT)}")
    source = path.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(source)

    require(source.lstrip().lower().startswith("<!doctype html>"), f"Missing doctype: {route}")
    require(parser.tags.get("html") == 1, f"Expected one html element: {route}")
    require(parser.tags.get("main") == 1, f"Expected one main element: {route}")
    require(parser.tags.get("nav", 0) >= 1, f"Missing navigation: {route}")
    require(parser.tags.get("footer") == 1, f"Expected one footer: {route}")
    require(parser.h1_count == 1, f"Expected one h1: {route}")
    require(parser.title.strip(), f"Missing title: {route}")

    meta = [attrs for tag, attrs in parser.attrs if tag == "meta"]
    links = [attrs for tag, attrs in parser.attrs if tag == "link"]
    anchors = [attrs for tag, attrs in parser.attrs if tag == "a"]
    images = [attrs for tag, attrs in parser.attrs if tag == "img"]

    require(any(item.get("name") == "description" and item.get("content") for item in meta), f"Missing description: {route}")
    for prop in ("og:title", "og:description", "og:url"):
        require(any(item.get("property") == prop and item.get("content") for item in meta), f"Missing {prop}: {route}")

    canonical = next((item.get("href") for item in links if item.get("rel") == "canonical"), None)
    require(canonical == f"{SITE_URL}{route}", f"Incorrect canonical URL for {route}: {canonical}")
    og_url = next(item.get("content") for item in meta if item.get("property") == "og:url")
    require(og_url == canonical, f"Open Graph URL differs from canonical: {route}")

    for attrs in anchors + links + images:
        url = attrs.get("href") or attrs.get("src") or ""
        target = local_target(url)
        if target is not None:
            require(target.is_file(), f"Broken local reference in {route}: {url}")


def validate_wrangler() -> None:
    path = ROOT / "wrangler.jsonc"
    require(path.is_file(), "Missing wrangler.jsonc")
    source = re.sub(r"/\*.*?\*/|//[^\n]*", "", path.read_text(encoding="utf-8"), flags=re.S)
    config = json.loads(source)
    require(config.get("name") == "watermelonman-studio", "Incorrect Wrangler project name")
    require(config.get("compatibility_date") == "2026-09-12", "Incorrect compatibility date")
    require(config.get("assets", {}).get("directory") == "./public", "Wrangler assets directory must be ./public")


def main() -> int:
    try:
        require(not (PUBLIC / "framecut/index.html").exists(), "Private FrameCut page must not be published")
        require("Belgrade · Serbia" not in (PUBLIC / "index.html").read_text(encoding="utf-8"), "Homepage must not publish the studio location")
        for route, path in ROUTES.items():
            validate_page(route, path)
        validate_wrangler()
    except (AssertionError, json.JSONDecodeError) as error:
        print(f"Site validation failed: {error}", file=sys.stderr)
        return 1
    print("Site validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
