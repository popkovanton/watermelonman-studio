# Watermelon Man Studio

The public website for Watermelon Man Studio and Fig: Video Editor. It is a dependency-free static site deployed as Cloudflare Workers static assets.

## Project structure

```text
public/
├── index.html                 Homepage
├── privacy/index.html         Privacy policy directory
├── privacy/fig/index.html     Fig Privacy Policy
├── support/index.html         Support page
└── assets/
    ├── styles.css             Shared styles
    └── favicon.svg            Site icon
tests/validate_site.py         Dependency-free structural checks
wrangler.jsonc                 Cloudflare Workers configuration
```

## Run locally

From the repository root:

```sh
python3 -m http.server 8000 --directory public
```

Open [http://localhost:8000](http://localhost:8000). Clean routes such as `/privacy/` and `/support/` work through their directory index files.

## Validate

```sh
python3 tests/validate_site.py
```

The validator checks route files, semantic page structure, metadata, internal links, local assets, canonical URLs, and the Wrangler static-assets configuration.

## Deploy to Cloudflare

No build command is required. Authenticate Wrangler for the Cloudflare account connected to this repository, then run:

```sh
npx wrangler deploy
```

Wrangler publishes the contents of `public/` using the Worker name `watermelonman-studio`.

## Fig release

- Fig is currently mentioned only on the homepage; no public product route is deployed while the app is in development.
- Add a product page, store link, and navigation link when Fig is ready to share publicly.
- Use `https://watermelonman.studio/privacy/fig/` in Fig and its Play Console listing.
- Reconcile Fig's Privacy Policy and Google Play Data safety answers with the released app and current Google SDK disclosures before distribution.

## `app-ads.txt`

The AdMob publisher record is stored in `public/app-ads.txt`. Cloudflare serves it at:

```text
https://watermelonman.studio/app-ads.txt
```

Keep this record synchronized with the publisher entry supplied by the AdMob account. Do not use an AdMob application ID or ad-unit ID.
