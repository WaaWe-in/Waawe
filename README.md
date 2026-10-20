# Your website — GitHub Pages edition

Everything in this folder is the finished, optimised static site. No build step, no Shopify.

## 1. Add your media (required, 5 minutes)
Your Shopify export contained only code — your images and videos live in Shopify *Content → Files*, so they
were not in the zip. Download them and **replace the labelled placeholders** (keep the exact file names):

| Replace this file | With (original Shopify file) |
|---|---|
| `assets/img/logo.png` | `wawee-removebg-preview.png` |
| `assets/img/results/result-1.png` | `ROAS-2.png` (₹1Cr+ / 5.77x) |
| `assets/img/results/result-2.png` | `ROAS.png` (₹2Cr+ / 4.68x) |
| `assets/img/results/result-3.png` | `Screenshot_2026-05-18_at_9.23.34_PM.png` (5.17x) |
| `assets/img/results/result-4.png` | `Screenshot_2026-05-18_at_9.11.07_PM.png` (4.9x) |
| `assets/video/ad-1.mp4` | `creative-3_b9d1a4fe-….mp4` (8.4X) |
| `assets/video/ad-2.mp4` | `creative-3.mp4` (6.7X) |
| `assets/video/ad-3.mp4` | `creative-2.mp4` (5.8X) |

Shrink videos first (big speed win). With ffmpeg:
`ffmpeg -i input.mp4 -vf "scale=-2:960" -c:v libx264 -crf 28 -preset slow -an -movflags +faststart ad-1.mp4`

## 2. Connect the forms (required)
GitHub Pages can't receive form data. Create a free endpoint at Formspree or Web3Forms and paste it into
`assets/js/site-config.js` (instructions are inside the file). One endpoint serves all three forms.

## 3. Publish
1. Create a GitHub repo and upload everything in this folder to the repo root (keep `.nojekyll`).
2. Repo → Settings → Pages → Deploy from branch → `main` / root.
3. Once you know your address, run once:
   `python3 tools/set-site-url.py https://YOURNAME.github.io/REPO` (or your custom domain).
   This adds canonical/social URLs, `sitemap.xml`, and fixes the 404 page.

Optional: `python3 tools/localize-cdn-images.py` downloads the brand/partner logos from Shopify's CDN so the site no longer depends on Shopify.
