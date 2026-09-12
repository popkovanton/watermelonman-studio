# Repository Guidance

## Project stack

- The website is plain HTML and CSS served from `public/` as Cloudflare Workers static assets.
- Keep the project dependency-free unless a requested feature cannot reasonably use browser or standard-library capabilities.
- Run `python3 tests/validate_site.py` after changing pages, links, metadata, assets, or Wrangler configuration.
- Preview locally with `python3 -m http.server 8000 --directory public`.
- Deploy with `npx wrangler deploy`; there is no build command.

## Working agreements

- Keep changes focused on the requested outcome and avoid speculative abstractions.
- Follow conventions already present in the repository; if none exist, prefer standard tooling and the smallest maintainable solution.
- Never commit secrets, credentials, generated build output, or machine-specific files.
- Add or update tests when behavior changes. Run all available relevant checks before reporting completion.
- Update user-facing documentation when setup or behavior changes.

## Git hygiene

- Preserve unrelated user changes in the working tree.
- Use concise, imperative commit messages when commits are requested.
- Do not rewrite shared history or use destructive Git commands without explicit approval.
