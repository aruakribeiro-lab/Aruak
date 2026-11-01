# -*- coding: utf-8 -*-
import json, os, sys, importlib
from common import *
import s0_intro
SECS = ['s1_scanner', 's2_diag', 's3_reparo', 's4_gestao', 's5_preobra', 's6_condo', 's7_empresa', 's8_acoes', 's9_duvidas']
mods = []
for s in SECS:
    if os.path.exists(s + '.py'):
        mods.append(importlib.import_module(s))

TOC = []  # (nível, rótulo, título h1 para busca)
def toc_html(pages):
    rows = []
    for lvl, lab, key in TOC:
        pg = str(pages.get(key, '')) if pages else ''
        rows.append({'cls': 'lvl1' if lvl == 1 else '', 'cells': [lab, pg]})
    return page('Sumário', 'Sumário', 'As páginas comerciais podem ser impressas isoladamente para apresentar ao cliente.',
                table(['Seção', 'Página'], rows, 'toc', widths=['88%', '12%']))

GROUP_TITLES = {'Orientação': 'Antes de começar', 'Frente 1': 'Frente 1 · Scanner da Obra', 'Frente 2': 'Frente 2 · Visita Diagnóstica, Laudo e Vistoria',
    'Frente 3': 'Frente 3 · Reparo Rápido', 'Frente 4': 'Frente 4 · Gestão de Obra', 'Frente 5': 'Frente 5 · Pré-obra com Arquitetos',
    'Frente 6': 'Frente 6 · Engenheiro do Condomínio', 'Estrutura da empresa': 'Estrutura da empresa', 'Quadro de ações': 'Quadro de ações', 'Fechamento': 'Fechamento'}

def collect_toc(html):
    import re
    last = None
    for m in re.finditer(r'<section class="pg[^"]*">(.*?)</section>', html, re.S):
        sec = m.group(1)
        h = re.search(r'<h1[^>]*>(.*?)</h1>', sec, re.S)
        if not h: continue
        title = re.sub('<[^>]+>', '', h.group(1)).strip()
        fr = re.search(r'<div class="cfr">(.*?)</div>', sec)
        kk = re.search(r'<div class="kick"><span>(.*?)</span>', sec)
        src = fr.group(1) if fr else re.sub('<[^>]+>|&nbsp;', ' ', kk.group(1)) if kk else ''
        g = re.search(r'Frente (\d)', src)
        if g: group = 'Frente ' + g.group(1)
        elif 'Estrutura' in src: group = 'Estrutura da empresa'
        elif 'Quadro' in src: group = 'Quadro de ações'
        elif 'Fechamento' in src: group = 'Fechamento'
        else: group = 'Orientação'
        if group != last:
            TOC.append((1, GROUP_TITLES[group], title)); last = group
        lab = f'{title} · página comercial' if fr else title
        TOC.append((2, lab, title))

def main(pages_file=None):
    pages = json.load(open(pages_file)) if pages_file and os.path.exists(pages_file) else {}
    body_parts = [s0_intro.como_usar(), s0_intro.premissas(), s0_intro.mapa()]
    for m in mods:
        body_parts.append(m.build())
    body = ''.join(body_parts)
    TOC.clear()
    collect_toc(body)
    html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Manual operacional das seis frentes</title><style>' + CSS +
            '</style></head><body>' + s0_intro.capa() + toc_html(pages) + body + '</body></html>')
    open('manual.html', 'w').write(html)
    json.dump([[l, a, k] for l, a, k in TOC], open('toc.json', 'w'), ensure_ascii=False, indent=0)
    print('ok', len(html), 'toc', len(TOC))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
