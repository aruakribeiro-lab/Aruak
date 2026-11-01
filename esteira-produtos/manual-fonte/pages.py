# -*- coding: utf-8 -*-
import json, sys, re
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
res = {}
def walk(items):
    for it in items:
        if isinstance(it, list):
            continue  # só o primeiro nível (h1)
        t = re.sub(r'\s+', '', it.title)
        try:
            res.setdefault(t, r.get_destination_page_number(it) + 1)
        except Exception:
            pass
walk(r.outline)
toc = json.load(open('toc.json'))
out = {}
for lvl, lab, key in toc:
    k = re.sub(r'\s+', '', key)
    if k in res: out[key] = res[k]
    else: print('NAO ACHEI', key)
json.dump(out, open('pages.json', 'w'), ensure_ascii=False)
print(len(r.pages), 'paginas;', len(out), 'de', len(toc), 'entradas')
