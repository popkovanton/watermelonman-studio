# Watermelon Man Studio

The public website for Watermelon Man Studio, Fig: Video Editor, and Car Pixels: Color by Number. It is a dependency-free static site deployed as Cloudflare Workers static assets.

## Project structure

```text
public/
├── index.html                 Homepage
├── privacy/index.html         Privacy policy directory
├── privacy/fig/index.html     Fig Privacy Policy
├── privacy/cars/index.html    Car Pixels Privacy Policy
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

## Car Pixels release

- Car Pixels: Color by Number is listed on the homepage and in the privacy directory.
- Its Privacy Policy URL is `https://watermelonman.studio/privacy/cars/` after deployment.
- Developer and privacy contact: Watermelon Man Studio, `watermelonman.studio@gmail.com`.
- Support messages and attachments are retained until the request is resolved, then deleted.
- Firebase Analytics and Firebase Crashlytics are planned for Car Pixels and disclosed in the policy. Their use was confirmed separately from the original app brief, which describes local event logging only. Exact custom events, identifiers, collection timing, consent controls, and Analytics retention settings remain undecided; reconcile the policy with the implementation before publication. The policy does not currently promise collection only after consent or an in-app analytics opt-out.
- The policy is based on the app privacy brief reviewed on October 5, 2026 and the confirmed Firebase plans. It describes an adult audience (18+), local game data, Android backup, analytics, crash reporting, rewarded ads, consent, Google Play purchases, and sharing.
- Before release, verify the actual AdMob partners and consent configuration against the release build and reconcile Google Play Data safety answers with the policy. The brief lists Mobile Ads 25.4.0; Google's current disclosure covers 25.5.0, so it does not by itself verify the shipped SDK version.
- After deployment, update the policy link in both the Android app and Play Console. Add a store link to the homepage when the public listing is confirmed.

## `app-ads.txt`

The AdMob publisher record is stored in `public/app-ads.txt`. Cloudflare serves it at:

```text
https://watermelonman.studio/app-ads.txt
```

Keep this record synchronized with the publisher entry supplied by the AdMob account. Do not use an AdMob application ID or ad-unit ID.
