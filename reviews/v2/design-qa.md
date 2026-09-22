# v2 design review

## Request and preservation

Preserve v1 in GitHub, then make a separate new version. Revise formulaic copy on both A and C; align C more closely with https://dine.framer.website/ and prioritize mobile.

Baseline: `v1-preserved-20260922`, preservation commit `995f25a`. Root HTML, original `a/`, `c/`, `compare/`, shared files and original assets remain unchanged. New pages live under `v2/`.

## Source capture

Dine was inspected live in Chromium at 1440px and 390px, from hero through footer, with section screenshots and DOM typography evidence. Local working evidence: `/tmp/52-redesign/source-*.png`, `source-*.json`, `detail-*.png`.

Observed design: nearly white #fefcfa; forest green #162b15; orange #fe4806; oversized wordmark with botanical overlap; desktop information strip; small rectangular CTAs; full-bleed photographic bands; two-column menu rows; alternating split sections; green story section; contact grid and FAQ. Mobile hides the desktop strip and uses a menu toggle, a large one-line brand name and vertically stacked content.

## Implementation and differences

- A2 retains A's curve and photograph composition, removes the presentation bar and numbered English headings, and rewrites copy using concrete restaurant details. Mobile actions are phone and Maps.
- C2 rebuilds the composition above, replacing the previous cream/rounded-card system. Chinese typography uses Noto Sans TC rather than the reference's Latin Archivo.
- Content, photos and brand logo are the project's restaurant assets. Citrus branch is an original SVG, replacing the source's Japanese tree/sushi decoration. No Framer code or image assets were copied.
- Reference pricing, statistics, testimonials, classes, sushi/catering claims and unsupported forms are omitted. Known restaurant details replace them.
- Motion is a short fade/slide; reduced-motion mode shows everything immediately. No blur animation over text.
- The layout is a brand adaptation, not an exact pixel clone; photography, typography and verified content differ intentionally.

## Verification

A2 and C2 at 1440, 820, 390 and 360px: no horizontal overflow, all image resources decode, no JS page errors, gallery opens and closes with Escape, mobile nav closes after anchor selection. A tabs switch with click and arrow keys. C FAQ and normal-motion visibility are checked separately. Desktop full page, mobile hero and selected mobile sections visually inspected against the reference structure.

Preservation check: `git diff v1-preserved-20260922 -- index.html a c compare shared.css shared.js assets brand-assets previews` produces no changes.

Telephone/Maps/social destinations checked as links only; no calls or messages sent. Native iPhone/Safari testing and client acceptance are not claimed. Menu/hours/LINE and full commercial photo rights remain pending as already disclosed in the preview.

final result: passed
