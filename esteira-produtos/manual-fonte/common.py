# -*- coding: utf-8 -*-
"""Estilo e utilitários de formatação do manual."""
from calc import *

NB = ' '

def n(v, d=2):
    s = f"{abs(v):,.{d}f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    return ('-' if v < 0 else '') + s

def brl(v, cents='auto'):
    if v is None:
        return '—'
    if cents == 'auto':
        d = 0 if abs(v - round(v)) < 0.005 else 2
    else:
        d = 2 if cents else 0
    s = n(abs(v), d)
    return ('−' if v < -0.004 else '') + 'R$' + NB + s

def hh(v):
    s = f"{v:.2f}".rstrip('0').rstrip('.').replace('.', ',')
    return s + NB + 'h'

def pct(v, d=1):
    return n(v * 100, d) + '%'

def esc(s):
    return s

def table(head, rows, cls='', widths=None, foot=None):
    h = ''.join(f'<th{(" style=\"width:%s\"" % widths[i]) if widths else ""}>{x}</th>' for i, x in enumerate(head))
    body = ''
    for r in rows:
        if isinstance(r, tuple) and len(r) == 2 and r[0] == '__cls__':
            continue
        cls_r = ''
        if isinstance(r, dict):
            cls_r = f' class="{r.get("cls", "")}"'
            r = r['cells']
        body += f'<tr{cls_r}>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    f = ''
    if foot:
        f = '<tfoot><tr>' + ''.join(f'<td>{c}</td>' for c in foot) + '</tr></tfoot>'
    return f'<table class="t {cls}"><thead><tr>{h}</tr></thead><tbody>{body}</tbody>{f}</table>'

def box(label, html, cls='box'):
    lab = f'<div class="lab">{label}</div>' if label else ''
    return f'<div class="{cls}">{lab}{html}</div>'

def kicker(section, internal=True):
    right = 'CIRCULAÇÃO INTERNA' if internal else ''
    return f'<div class="kick"><span>ENTRE COLUNAS&nbsp;&nbsp;/&nbsp;&nbsp;{section}</span><span class="r">{right}</span></div>'

def page(section, title, sub, body, internal=True, cls=''):
    return (f'<section class="pg {cls}">{kicker(section, internal)}'
            f'<h1>{title}</h1>' + (f'<p class="sub">{sub}</p>' if sub else '') + body + '</section>')

def ul(items, cls=''):
    return f'<ul class="{cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'

def ol(items, cls=''):
    return f'<ol class="{cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'

def tag(t):
    return f'<span class="tg">[{t}]</span>'

def msg(text):
    """Mensagem de WhatsApp: parágrafos separados por linha em branco."""
    ps = [p.strip() for p in text.strip().split('\n\n')]
    return '<div class="wa">' + ''.join(f'<p>{p}</p>' for p in ps) + '</div>'

def ind_table(itens, show_min=True):
    """itens: (rótulo, E, medidos)"""
    head = ['Cenário', 'Receita', 'Disponível', 'Horas do Aruak', 'Disponível por hora', 'Saldo parcial (Aruak a R$ 100/h)']
    if show_min:
        head.append('Preço para R$ 200/h')
    head.append('Contratos medidos')
    rows = []
    for lab, e, med in itens:
        r = [lab, brl(e.receita), brl(e.disp), hh(e.h), brl(e.ph), brl(e.saldo)]
        if show_min:
            r.append(brl(e.pmin))
        r.append(med)
        rows.append(r)
    w = ['27%', '8%', '10%', '8%', '10%', '13%', '11%', '13%'] if show_min else None
    return table(head, rows, 'num', widths=w)

CONTATO = 'WhatsApp (62) 98170-8669'
RT = 'Eng. Aruak Junqueira · CREA 1014776589 D/GO'
WA = 'https://wa.me/5562981708669?text=Fiz%20o%20Scanner.%20C%C3%B3digo%3A%20SCN-'

def client_page(frente, titulo, promessa, blocos, preco_html, proximo_html, rodape=""):
    """Página comercial: pode ser apresentada ao cliente."""
    grid = ''.join(f'<div class="cb"><h3>{t}</h3>{h}</div>' for t, h in blocos)
    return (f'<section class="pg client">'
            f'<div class="ctop"><div><b>ENTRE COLUNAS</b><span>Engenharia de Previsibilidade</span></div>'
            f'<div class="cr">{RT}<br>{CONTATO}</div></div>'
            f'<div class="cfr">{frente}</div>'
            f'<h1 class="ct">{titulo}</h1><p class="cprom">{promessa}</p>'
            f'<div class="cgrid">{grid}</div>'
            f'<div class="cbottom"><div class="cprice"><h3>Investimento</h3>{preco_html}</div>'
            f'<div class="cnext"><h3>Próximo passo</h3>{proximo_html}</div></div>'
            + (f'<p class="cfoot">{rodape}</p>' if rodape else '') +
            '</section>')

CSS = r"""
@page { size: A4; margin: 14mm 15mm 17mm 15mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "DejaVu Sans", "Liberation Sans", Arial, sans-serif; font-size: 8.9pt; color: #1f2a30; line-height: 1.42; margin: 0; background: #fff; }
.pg { break-before: page; }
.pg:first-child { break-before: auto; }
.kick { display: flex; justify-content: space-between; font-size: 7.2pt; font-weight: 700; letter-spacing: .06em; color: #1b6b57; text-transform: uppercase; border-top: 3.2mm solid #1b6b57; padding-top: 3mm; margin-bottom: 2mm; }
.kick .r { color: #7a868c; font-weight: 600; }
h1 { font-family: "DejaVu Serif", "Liberation Serif", serif; font-weight: 400; font-size: 20pt; line-height: 1.15; margin: 2mm 0 1.2mm; color: #1f2a30; }
.sub { font-size: 9.6pt; color: #55636b; margin: 0 0 3.5mm; }
h2 { font-size: 11pt; color: #1b6b57; margin: 4.5mm 0 1.8mm; break-after: avoid; }
h3 { font-size: 9.3pt; margin: 3mm 0 1.2mm; break-after: avoid; color: #1f2a30; }
p { margin: 0 0 2mm; }
ul, ol { margin: 0 0 2.2mm; padding-left: 5mm; }
li { margin: 0 0 .8mm; }
table.t { border-collapse: collapse; width: 100%; margin: 1.5mm 0 3mm; font-size: 7.9pt; line-height: 1.32; }
table.t th { background: #1c2b33; color: #fff; text-align: left; font-weight: 700; padding: 1.5mm 1.8mm; vertical-align: bottom; }
table.t td { border-bottom: 1px solid #d6dcd9; padding: 1.3mm 1.8mm; vertical-align: top; }
table.t tbody tr:nth-child(even) td { background: #f4f6f5; }
table.t tr { break-inside: avoid; }
table.t thead { display: table-header-group; }
table.t tfoot td { font-weight: 700; background: #e8f2ee; border-top: 1.5px solid #1b6b57; }
table.num td:not(:first-child), table.num th:not(:first-child) { text-align: right; }
table.num td:last-child, table.num th:last-child { text-align: right; }
table.l2 td:nth-child(2), table.l2 th:nth-child(2) { text-align: left !important; }
table.t tr.tot td { font-weight: 700; background: #e8f2ee !important; border-top: 1.5px solid #1b6b57; }
table.t tr.hl td { background: #fbf3e4 !important; }
table.sm { font-size: 7.4pt; }
table.form td { height: 6.5mm; }
.box { background: #e8f2ee; border-radius: 1.8mm; padding: 2.6mm 3.6mm; margin: 2mm 0 3mm; break-inside: avoid; }
.box p:last-child, .box ul:last-child, .box ol:last-child { margin-bottom: 0; }
.lab { font-size: 6.9pt; font-weight: 700; color: #1b6b57; letter-spacing: .06em; text-transform: uppercase; margin-bottom: 1mm; }
.warn { background: #fbf3e4; border-left: 3px solid #c08a2c; padding: 2.4mm 3.4mm; margin: 2mm 0 3mm; break-inside: avoid; }
.warn .lab { color: #8a5d12; }
.red { background: #fbeceb; border-left: 3px solid #b3261e; padding: 2.4mm 3.4mm; margin: 2mm 0 3mm; break-inside: avoid; }
.red .lab { color: #b3261e; }
.tg { font-size: 6.6pt; font-weight: 700; color: #6b5a2a; background: #f4ecd6; border-radius: 1mm; padding: 0 1mm; white-space: nowrap; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; break-inside: avoid; }
.two-flow { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; }
.three { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; }
.nb { break-inside: avoid; }
.wa { background: #f3f7f2; border: 1px solid #cfe0cc; border-radius: 2mm; padding: 2.4mm 3.2mm; margin: 1.5mm 0 3mm; font-size: 8.5pt; break-inside: avoid; }
.wa p { margin: 0 0 1.6mm; }
.wa p:last-child { margin: 0; }
.small { font-size: 7.6pt; color: #55636b; }
.mono { font-family: "DejaVu Sans Mono", monospace; font-size: 7.2pt; word-break: break-all; }
.pill { display: inline-block; font-size: 6.8pt; font-weight: 700; padding: .3mm 2mm; border-radius: 3mm; white-space: nowrap; }
.p-v { background: #d9efe0; color: #1d6b2a; } .p-t { background: #fbecc9; color: #7a5a00; } .p-c { background: #e1e8ef; color: #2b4a66; } .p-i { background: #ececec; color: #555; }
.step { display: grid; grid-template-columns: 7mm 1fr; gap: 2mm; margin-bottom: 1.5mm; break-inside: avoid; }
.step b.nn { background: #1b6b57; color: #fff; border-radius: 50%; width: 6mm; height: 6mm; display: flex; align-items: center; justify-content: center; font-size: 7.5pt; }
.toc td { font-size: 8.6pt; padding: 1.1mm 1.8mm; }
.toc td:last-child { text-align: right; width: 14mm; }
.toc tr.lvl1 td { font-weight: 700; background: #e8f2ee !important; }
.check td:first-child { width: 6mm; }
.sq { display: inline-block; width: 3mm; height: 3mm; border: 1px solid #55636b; vertical-align: -0.4mm; }
/* capa */
.cover { height: 262mm; display: flex; flex-direction: column; justify-content: flex-start; }
.cover .meta { margin-top: 12mm; }
.cover .band { background: #1b6b57; color: #fff; padding: 12mm 12mm 10mm; border-radius: 0 0 2mm 2mm; }
.cover .brand { font-size: 8.5pt; letter-spacing: .14em; font-weight: 700; color: #cfe7de; }
.cover h1 { color: #fff; font-size: 32pt; margin: 8mm 0 3mm; }
.cover .lead { font-size: 11.5pt; color: #e3f1ec; max-width: 150mm; }
.cover .meta { padding: 0 2mm; }
.cover .who { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; margin: 6mm 0; }
.cover .who div { border-top: 2.5px solid #1b6b57; padding-top: 2mm; font-size: 8.6pt; }
.cover .who b { display: block; font-size: 10pt; margin-bottom: 1mm; }
/* página comercial */
.client { font-size: 9.9pt; line-height: 1.46; }
.ctop { display: flex; justify-content: space-between; align-items: flex-end; border-top: 3.2mm solid #1c2b33; padding-top: 3mm; }
.ctop b { display: block; letter-spacing: .14em; font-size: 10pt; }
.ctop span { font-size: 7.6pt; color: #55636b; letter-spacing: .04em; }
.ctop .cr { text-align: right; font-size: 7.4pt; color: #55636b; }
.cfr { font-size: 7pt; color: #9aa4a8; text-transform: uppercase; letter-spacing: .08em; margin-top: 4mm; }
h1.ct { font-size: 27pt; margin: 1mm 0 2.5mm; }
.cprom { font-size: 12pt; color: #1b6b57; margin: 0 0 4mm; line-height: 1.35; font-family: "DejaVu Serif", serif; }
.cgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 5mm 7mm; }
.cb { border-top: 1.5px solid #1b6b57; padding-top: 1.6mm; }
.cb h3 { margin: 0 0 1.5mm; font-size: 10.2pt; color: #1b6b57; }
.cb ul { padding-left: 4mm; }
.cbottom { display: grid; grid-template-columns: 1.15fr 1fr; gap: 7mm; margin-top: 6mm; }
.cprice { background: #1c2b33; color: #fff; border-radius: 2mm; padding: 3mm 4mm; }
.cprice h3, .cnext h3 { margin: 0 0 1.5mm; font-size: 9.4pt; }
.cprice h3 { color: #9fd3c1; }
.cprice table { width: 100%; border-collapse: collapse; font-size: 9.2pt; }
.cprice td { padding: .9mm 0; border-bottom: 1px solid #3b4a52; vertical-align: top; }
.cprice td.v { text-align: right; font-weight: 700; white-space: nowrap; padding-left: 3mm; }
.cprice p { margin: 1.5mm 0 0; font-size: 8.6pt; color: #d5dde0; }
.cnext { background: #e8f2ee; border-radius: 2mm; padding: 3mm 4mm; }
.cfoot { font-size: 7.2pt; color: #7a868c; margin-top: 3mm; }
table.map td { padding: .9mm 1.6mm; } table.map tr.tot td { padding-top: 1.4mm; }
"""
