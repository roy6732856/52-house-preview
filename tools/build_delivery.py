#!/usr/bin/env python3
"""Build a reviewable Pages artifact. Default is noindex; production requires a real origin."""
import argparse, json, shutil, re
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--origin',default='https://52-house-preview.pages.dev');p.add_argument('--production',action='store_true');args=p.parse_args()
origin=args.origin.rstrip('/');u=urlparse(origin)
if u.scheme!='https' or not u.hostname or u.path or u.query or u.fragment: p.error('--origin must be an HTTPS origin')
if args.production and u.hostname.endswith('pages.dev'):p.error('Production requires the purchased domain')
dst=ROOT/'delivery-dist';dst.mkdir(exist_ok=True)
for name in ['assets','brand-assets','v2','a','c','compare','previews','oranges']:
 if (ROOT/name).exists():shutil.copytree(ROOT/name,dst/name,dirs_exist_ok=True,copy_function=shutil.copyfile)
for name in ['shared.js','shared.css']:shutil.copyfile(ROOT/name,dst/name)
s=(ROOT/'v2/c/index.html').read_text()
entity={'@context':'https://schema.org','@type':'Restaurant','@id':origin+'/#restaurant','name':'伍貳居所','url':origin+'/','description':'橘二代位於苗栗泰安清安村的老屋餐廳，供應客家火鍋與義式手作冰淇淋。','telephone':'+886-37-941-068','image':[origin+'/v2/assets/frank-table.webp'],'logo':origin+'/brand-assets/orange-logo.png','address':{'@type':'PostalAddress','streetAddress':'清安村13鄰二十份1號','addressLocality':'泰安鄉','addressRegion':'苗栗縣','addressCountry':'TW'},'servesCuisine':['客家料理','火鍋','義式手作冰淇淋'],'openingHoursSpecification':[{'@type':'OpeningHoursSpecification','dayOfWeek':['Monday','Thursday','Friday','Saturday','Sunday'],'opens':'10:00','closes':'20:00'}],'sameAs':['https://lin.ee/qrXVp1U','https://www.facebook.com/p/伍貳居所-61569992565634/','https://www.instagram.com/52hungry.house/']}
head=f'''<link rel="canonical" href="{origin}/">
<meta property="og:type" content="website"><meta property="og:locale" content="zh_TW"><meta property="og:site_name" content="伍貳居所・橘二代"><meta property="og:title" content="伍貳居所｜苗栗泰安客家火鍋與手作冰淇淋"><meta property="og:description" content="在泰安老屋吃客家銅鍋，飯後來一份水果冰淇淋。查看餐點、用餐須知與外送方案，來電預約聚餐。"><meta property="og:url" content="{origin}/"><meta property="og:image" content="{origin}/v2/assets/frank-table.webp"><meta property="og:image:alt" content="伍貳居所老屋旁的戶外餐桌"><meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(entity,ensure_ascii=False)}</script>
'''
s=s.replace('</head>',head+'</head>')
# C remains an unindexed review alias; the production root alone becomes indexable.
(dst/'v2/c/index.html').write_text(s)
if args.production:s=s.replace('content="noindex,nofollow"','content="index,follow,max-image-preview:large"')
(dst/'index.html').write_text(s)
# Independent orange brand page, using its own canonical and metadata.
orange=(ROOT/'oranges/index.html').read_text()
orange_entity={'@context':'https://schema.org','@type':'WebPage','@id':origin+'/oranges/#webpage','url':origin+'/oranges/','name':'橘二代｜苗栗大湖茂谷柑・年節禮盒與品牌故事','inLanguage':'zh-Hant','about':{'@type':'Brand','name':'橘二代','logo':origin+'/oranges/assets/logo-320.webp'}}
orange_head=f'''<link rel="canonical" href="{origin}/oranges/"><meta property="og:type" content="website"><meta property="og:locale" content="zh_TW"><meta property="og:title" content="橘二代｜一盒橘子，一份好心意"><meta property="og:description" content="認識苗栗大湖茂谷柑與手作木盒故事，查看年節禮盒預訂、運費及出貨須知。"><meta property="og:url" content="{origin}/oranges/"><meta property="og:image" content="{origin}/oranges/assets/hero-1280.webp"><meta name="twitter:card" content="summary_large_image"><script type="application/ld+json">{json.dumps(orange_entity,ensure_ascii=False)}</script>'''
orange=orange.replace('</head>',orange_head+'</head>')
if args.production:orange=orange.replace('content="noindex,nofollow"','content="index,follow,max-image-preview:large"')
(dst/'oranges/index.html').write_text(orange)
(dst/'robots.txt').write_text('User-agent: *\nAllow: /\n'+(f'\nSitemap: {origin}/sitemap.xml\n' if args.production else '# Preview: pages carry noindex until domain launch.\n'))
urls=f'<url><loc>{origin}/</loc></url><url><loc>{origin}/oranges/</loc></url>' if args.production else '<!-- Preview: no indexable URLs. Populated by the production build. -->'
(dst/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>')
(dst/'404.html').write_text('''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>找不到頁面｜伍貳居所</title><style>body{background:#fefcfa;color:#162b15;font:18px/1.8 system-ui;padding:12vh 8vw}a{color:#cf4615;display:inline-block;padding:12px 0;margin-right:24px}</style><h1>這個頁面搬家了。</h1><p>回到伍貳居所首頁，查看餐點、地址與訂位資訊。</p><a href="/">回首頁</a><a href="tel:037941068">電話訂位</a></html>''')
headers='/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n'
if not args.production:headers+='  X-Robots-Tag: noindex, nofollow\n'
else:
 for route in ['/v2/*','/a/*','/c/*','/compare/*','/previews/*']:headers+=route+'\n  X-Robots-Tag: noindex, nofollow\n'
(dst/'_headers').write_text(headers)
print(json.dumps({'output':str(dst),'origin':origin,'production':args.production,'line':'https://lin.ee/qrXVp1U'},ensure_ascii=False))
