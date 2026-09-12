# Watermelon Man Studio Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a polished, accessible, dependency-free four-route studio website through Cloudflare Workers static assets.

**Architecture:** Four semantic HTML documents under `public/` share one stylesheet and local SVG assets. A standard-library Python validator checks routes, metadata, links, assets, and Wrangler configuration without adding package tooling.

**Tech Stack:** HTML5, CSS, SVG, Python 3 standard library, Cloudflare Wrangler configuration

**Spec:** `docs/superpowers/specs/2026-09-12-watermelonman-studio-website-design.md`

## Global Constraints

- Website files live in `public/`; deployment is `npx wrangler deploy` with no build command.
- Do not add JavaScript frameworks, CSS frameworks, package manifests, analytics, cookies, trackers, or external runtime assets.
- Use only confirmed FrameCut features and privacy behavior from the approved specification.
- Preserve clean routes `/`, `/framecut/`, `/privacy/`, and `/support/`.

---

### Task 1: Add structural validation

**Files:**
- Create: `tests/validate_site.py`

**Interfaces:**
- Consumes: repository root, `public/`, and `wrangler.jsonc`
- Produces: exit code 0 with `Site validation passed.` when all structural contracts hold

- [x] **Step 1: Write the validator before site files exist**

```python
ROUTES = {
    "/": Path("public/index.html"),
    "/framecut/": Path("public/framecut/index.html"),
    "/privacy/": Path("public/privacy/index.html"),
    "/support/": Path("public/support/index.html"),
}

for route, path in ROUTES.items():
    require(path.is_file(), f"Missing route {route}: {path}")
```

Parse each HTML file with `html.parser.HTMLParser`; require one `h1`, a `main`, navigation, footer, title, description, canonical URL, Open Graph title/description/url, and valid local links/assets. Parse comment-free `wrangler.jsonc` with `json.loads` and require the exact Worker name and `./public` assets directory.

- [x] **Step 2: Run the validator and confirm the expected failure**

Run: `python3 tests/validate_site.py`

Expected: non-zero exit with `Missing route /: public/index.html`.

### Task 2: Build the shared visual system and public pages

**Files:**
- Create: `public/assets/styles.css`
- Create: `public/assets/favicon.svg`
- Create: `public/assets/framecut-icon.svg`
- Create: `public/index.html`
- Create: `public/framecut/index.html`
- Create: `public/support/index.html`
- Create: `public/privacy/index.html`

**Interfaces:**
- Consumes: the route and metadata contracts in `tests/validate_site.py`
- Produces: four responsive static pages with shared navigation, footer, styles, and local assets

- [x] **Step 1: Create the shared CSS and SVG assets**

```css
:root {
  --ink: #171918;
  --paper: #f8f7f3;
  --melon: #e94f57;
  --rind: #1f6b4f;
  --line: #d9d8d2;
}
```

Build the typography, layout grid, skip link, focus states, editorial rules, product composition, screenshot placeholders, policy typography, and mobile breakpoints from these tokens. Keep body text at `1rem` or larger and support `prefers-reduced-motion` by avoiding required motion.

- [x] **Step 2: Author the homepage and FrameCut page**

Use semantic `header`, `nav`, `main`, `section`, and `footer` elements. The homepage headline is “Small software, thoughtfully made.” with the approved studio description. The FrameCut headline is “Simple video editing. Without all the clutter.” and lists exactly the five approved capabilities. Mark replacement locations with source comments and show “Coming to Google Play” without a fake link.

- [x] **Step 3: Author support and privacy pages**

Support exposes `mailto:watermelonman.studio@gmail.com`. Privacy is dated September 2026 and covers collection, local video files, planned AdMob processing, third parties, retention, children, security, changes, and contact. Include a non-visible developer comment requiring final SDK, consent, Data safety, age-rating, and policy checks before release.

- [x] **Step 4: Run the validator and make the implementation green**

Run: `python3 tests/validate_site.py`

Expected: `Site validation passed.`

### Task 3: Add deployment configuration and maintainer documentation

**Files:**
- Create: `wrangler.jsonc`
- Create: `README.md`
- Modify: `AGENTS.md`

**Interfaces:**
- Consumes: `public/` static site
- Produces: documented local-preview and Cloudflare deployment workflows

- [x] **Step 1: Configure Cloudflare static assets**

```jsonc
{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "watermelonman-studio",
  "compatibility_date": "2026-09-12",
  "assets": {
    "directory": "./public"
  }
}
```

- [x] **Step 2: Document maintenance and deployment**

Document `python3 -m http.server 8000 --directory public`, `python3 tests/validate_site.py`, and `npx wrangler deploy`. Explain that `public/app-ads.txt` maps to `/app-ads.txt`, and identify the exact assets and markup to replace for the FrameCut icon, screenshots, and future Play link.

- [x] **Step 3: Update repository guidance**

Replace the empty-project status with the actual static stack and validation, preview, and deployment commands. Preserve the existing working agreements and Git hygiene.

- [x] **Step 4: Re-run validation**

Run: `python3 tests/validate_site.py`

Expected: `Site validation passed.`

### Task 4: Verify, preview, and publish

**Files:**
- Inspect: all tracked and untracked project files

**Interfaces:**
- Consumes: completed site source
- Produces: validated commit on `origin/main` and a running local preview URL

- [x] **Step 1: Run static checks**

Run: `python3 tests/validate_site.py`

Run: `git diff --check`

Expected: validator success and no whitespace errors.

- [x] **Step 2: Serve and probe every route**

Run the documented local server on port 8000. Request `/`, `/framecut/`, `/privacy/`, `/support/`, the stylesheet, and both SVG assets; require HTTP 200 for each. Leave the server running and provide `http://localhost:8000/` to the user.

- [x] **Step 3: Inspect repository state and diff**

Run: `git status --short --branch`

Run: `git diff --stat`

Run: `git diff -- . ':(exclude)docs/superpowers/specs/2026-09-12-watermelonman-studio-website-design.md'`

Confirm only intended website, validation, documentation, and repository-guidance changes are present.

- [x] **Step 4: Commit and push**

Stage all intended files and commit with `feat: launch studio website`. Push the resulting `main` commit to `origin/main`, then verify local `HEAD` matches `refs/remotes/origin/main`.
