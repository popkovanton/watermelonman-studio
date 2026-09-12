# Watermelon Man Studio Website Design

## Goal

Build a production-ready, dependency-free website for Watermelon Man Studio that serves as the studio's public home and the official developer website for the Android app FrameCut.

## Audience and primary tasks

The site serves prospective FrameCut users, Google Play reviewers, and people seeking support or privacy information. Visitors must be able to understand what the studio and FrameCut make, reach support, and read the privacy policy without scripts, accounts, cookies, or trackers.

## Architecture

The project is a static multi-page site served from `public/` by Cloudflare Workers static assets. Each public route has its own `index.html`, allowing clean trailing-slash URLs without client-side routing:

- `/` → `public/index.html`
- `/privacy/` → `public/privacy/index.html`
- `/support/` → `public/support/index.html`

Shared styles live in `public/assets/styles.css`. The site icon is a local SVG under `public/assets/`. No package manager, build tool, framework, external font, analytics service, or client-side JavaScript is required.

`wrangler.jsonc` names the Worker `watermelonman-studio`, uses compatibility date `2026-09-12`, and serves `./public`. Deployment is `npx wrangler deploy` with no build command.

## Visual direction

The site uses a restrained editorial layout with generous whitespace, strong system typography, dark charcoal text, and small watermelon-red and rind-green accents. Dividers, offset rules, and compact geometric details provide personality without literal watermelon illustrations, glass effects, excessive gradients, or rounded-card repetition.

The visual hierarchy remains sparse on the homepage and becomes more practical on the product, support, and policy pages. All layouts adapt to narrow screens without horizontal scrolling. Main text remains at least 16px, interactive targets are comfortably sized, focus states are visible, and motion is unnecessary.

## Shared navigation and footer

Every page includes a skip link, a semantic header with the studio wordmark and navigation, a single `main` region, and a shared footer. Navigation links point to root-relative clean routes so they work consistently when deployed. The footer links to Privacy and Support and includes the 2026 copyright notice.

## Homepage

The homepage introduces Watermelon Man Studio as an independent studio making small, focused software. Its first viewport contains the studio identity and a concise editorial headline rather than a generic oversized SaaS hero.

A single product feature presents FrameCut as a fast, straightforward Android video editor. It is intentionally not linked while the app is in development. The page contains no invented metrics, testimonials, logos, or extra marketing sections.

## FrameCut public presence

FrameCut is represented only by the restrained product block on the homepage. The `/framecut/` route, screenshots, store badge, and navigation links are not published until the app is ready to share.

## Support page

The support page briefly invites questions about FrameCut or other Watermelon Man Studio products. It exposes `watermelonman.studio@gmail.com` as a clickable `mailto:` link and does not add a form or external service.

## Privacy policy

The policy is dated September 2026 and written as an initial policy based only on confirmed behavior:

- Editing happens locally on the device.
- Watermelon Man Studio does not receive uploaded video or media files through FrameCut.
- Planned rewarded ads use Google AdMob / Google Mobile Ads, whose SDK may process device and advertising identifiers, diagnostics, approximate location, and other data under Google's policies.
- The policy does not claim that crash reporting or analytics currently exists.

It includes sections for information collection, video and media files, advertising, third-party services, retention, children, security, policy changes, and contact. A source-only HTML comment reminds the developer to verify the final SDK configuration, consent behavior, Play Data safety answers, age rating, and linked third-party policy before publishing. The reminder is not visible to visitors.

## Metadata and assets

Each page has a unique title and description, canonical URL, responsive viewport, color-scheme and theme-color metadata, and Open Graph metadata. A minimal local SVG favicon avoids external requests.

## Future `app-ads.txt`

The README instructs the developer to add the final AdMob record at `public/app-ads.txt`, which Cloudflare will expose at `/app-ads.txt`. No speculative publisher ID is included.

## Documentation

The README documents the route-to-file structure, local serving with Python's standard library, Cloudflare deployment through Wrangler, the future `app-ads.txt` location, and how to restore a FrameCut product route when it is ready.

## Validation

Because the implementation is static markup and configuration with no application logic, validation uses dependency-free structural checks rather than adding a test framework. Checks verify:

- all three public route entry points exist and the private FrameCut page does not;
- internal links resolve to files under `public/`;
- referenced local assets exist;
- every page has expected semantic landmarks, metadata, and a single primary heading;
- email and canonical links are correct;
- `wrangler.jsonc` parses after removing JSON comments and points to `./public`;
- the site responds successfully for every route through a local static server;
- HTML, CSS, and SVG files contain no obvious syntax or whitespace errors;
- the final Git diff contains only intended source and documentation.

## Deployment and completion

After validation, all repository changes are committed with a clear message and pushed to `origin/main`. Cloudflare Workers remains the sole deployment target for this project; no separate hosting platform or generated build output is added.
