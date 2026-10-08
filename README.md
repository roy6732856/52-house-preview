# 伍貳居所 — Website design preview

C is the default homepage. A and C prototypes and their comparison are available at `a/`, `c/`, and `compare/`.

Static HTML/CSS/JS hosted on Cloudflare Pages (Direct Upload). GitHub preserves the source and earlier GitHub Pages copy. No build dependencies.

Primary preview: https://52-house-preview.pages.dev/

The first version is preserved under tag `v1-preserved-20260922`. The separate redesign is at https://52-house-preview.pages.dev/v2/compare/ (A2 and C2). See `VERSIONS.md` and `reviews/v2/design-qa.md`.

This is a design preview, not the official operating website. Opening hours, menu and LINE details remain to be confirmed. Brand photographs supplied for the project; copper-pot photograph sourced from Klook with its watermark retained. Media rights remain with their respective owners. No license to reuse photographs is granted by this repository.

## 正式網域與搜尋收錄（2026-10-08）

正式網域為 https://www.tangerine2.tw。`site-release.json` 保存正式發佈設定，
`python3 tools/build_delivery.py` 預設使用正式 canonical、robots.txt 與兩頁 sitemap。
`--preview` 可建立全站 noindex 的測試產物，勿用來覆蓋正式部署。
Pages.dev 主機與舊版路徑仍以 X-Robots-Tag 禁止收錄。
搜尋引擎收錄與 Search Console 提交為不同狀態；本次未宣稱已被 Google 收錄。
