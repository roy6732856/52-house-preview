# Design versions

## v1-preserved — 2026-09-22

User requested preserving this version before the next redesign.

- Website source: initial commit `55f9ebc7be3799d7200e9c60af45e9ac6408074e`.
- C homepage: https://52-house-preview.pages.dev/
- A: https://52-house-preview.pages.dev/a/
- C: https://52-house-preview.pages.dev/c/
- Comparison: https://52-house-preview.pages.dev/compare/
- Immutable CF deployment: https://4059f223.52-house-preview.pages.dev/
- Preserve existing root, A, C and comparison content when adding the next version under `/v2/`.
- Next iteration: edit formulaic copy on A and C; reconstruct C's composition and mobile hierarchy using https://dine.framer.website/ as the visual reference, with the restaurant's own brand content and photographs.

Cloudflare Pages is the intended hosting destination (Direct Upload). The earlier GitHub Pages copy remains available. This repository is the versioned source.

## v2 — separate redesign

- C2: https://52-house-preview.pages.dev/v2/c/
- A2: https://52-house-preview.pages.dev/v2/a/
- New comparison: https://52-house-preview.pages.dev/v2/compare/
- A2 copy cleanup; C2 Dine-based layout rebuild, Chinese brand adaptation and original citrus artwork.
- `reviews/v2/design-qa.md` records source comparison and validation.
- Root and all v1 pages remain unchanged. CF deploys must include the original site plus `v2/`.
