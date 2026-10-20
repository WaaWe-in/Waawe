#!/usr/bin/env python3
"""
OPTIONAL. The brand-logo marquee and partner logos are still loaded from your Shopify CDN
(cdn.shopify.com). That works as long as your Shopify store/files stay online. To make the site
fully self-contained, run this once (needs internet):

    python3 tools/localize-cdn-images.py

It downloads every cdn.shopify.com image into assets/img/brands/ and rewrites the pages to use them.
"""
import re, sys, urllib.request
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parent.parent
out = root / 'assets/img/brands'
out.mkdir(parents=True, exist_ok=True)
pat = re.compile(r'https://cdn\.shopify\.com/[^"\s\'<>]+')
done = {}

for f in sorted(root.rglob('*.html')):
    rel = f.relative_to(root).as_posix()
    if rel.startswith('tools/'):
        continue
    prefix = '../' * rel.count('/')
    html = f.read_text(encoding='utf-8')

    def swap(m):
        url = m.group(0).replace('&amp;', '&')
        name = Path(urlparse(url).path).name
        if url not in done:
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                (out / name).write_bytes(urllib.request.urlopen(req, timeout=30).read())
                done[url] = name
                print('downloaded', name)
            except Exception as e:
                print('FAILED', name, e)
                done[url] = None
        return prefix + 'assets/img/brands/' + done[url] if done[url] else m.group(0)

    new = pat.sub(swap, html)
    new = new.replace('<link rel="preconnect" href="https://cdn.shopify.com" crossorigin>', '')
    if new != html:
        f.write_text(new, encoding='utf-8')
print('Finished. %d images localised.' % sum(1 for v in done.values() if v))
