#!/usr/bin/env python3
"""
Run ONCE, after you know your final web address. Adds canonical links, social-share URLs,
sitemap.xml and robots.txt, and fixes the 404 page for your hosting path.

    python3 tools/set-site-url.py https://yourname.github.io/your-repo
    python3 tools/set-site-url.py https://www.yourdomain.com

Safe to run again if the address changes.
"""
import re, sys
from pathlib import Path
from urllib.parse import urlparse

if len(sys.argv) != 2 or not sys.argv[1].startswith('http'):
    sys.exit(__doc__)

site = sys.argv[1].rstrip('/')
base_path = (urlparse(site).path.rstrip('/') + '/')
root = Path(__file__).resolve().parent.parent
has_og = (root / 'assets/img/og.png').exists()

urls = []
for f in sorted(root.rglob('*.html')):
    rel = f.relative_to(root).as_posix()
    if rel.startswith('tools/'):
        continue
    html = f.read_text(encoding='utf-8')
    if rel == '404.html':
        html = re.sub(r'<base href="[^"]*">', '<base href="%s">' % base_path, html, count=1)
        f.write_text(html, encoding='utf-8')
        continue
    page_url = site + '/' + ('' if rel == 'index.html' else rel[:-len('index.html')])
    urls.append(page_url)
    html = re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:url"[^>]*>|<meta property="og:image"[^>]*>', '', html)
    html = html.replace('<meta name="twitter:card" content="summary_large_image">', '<meta name="twitter:card" content="summary">')
    seo = '<link rel="canonical" href="%s"><meta property="og:url" content="%s">' % (page_url, page_url)
    if has_og:
        seo += '<meta property="og:image" content="%s/assets/img/og.png">' % site
        html = html.replace('<meta name="twitter:card" content="summary">', '<meta name="twitter:card" content="summary_large_image">')
    html = html.replace('<!--seo-->', '<!--seo-->' + seo, 1) if '<!--seo-->' in html else html
    f.write_text(html, encoding='utf-8')

(root / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join('  <url><loc>%s</loc></url>\n' % u for u in urls) + '</urlset>\n', encoding='utf-8')
(root / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % site, encoding='utf-8')
print('Done. %d pages in sitemap. 404 base set to %s' % (len(urls), base_path))
