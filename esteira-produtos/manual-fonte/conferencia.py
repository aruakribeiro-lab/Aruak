# -*- coding: utf-8 -*-
"""Conferência independente: recalcula os números-chave sem usar calc.py e procura cada um no texto do PDF."""
import re, subprocess, sys
from pypdf import PdfReader
pdf = sys.argv[1]
txt = subprocess.check_output(['pdftotext', pdf, '-']).decode()
flat = re.sub(r'\s+', ' ', txt).replace(' ', ' ')
def f(v, d=2):
    s = f"{v:,.{d}f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    return 'R$ ' + s
checks = {}
# Visita (consolidado p.4)
disp = 1200*0.92 - 0.5*35 - 50 - 108.39
checks['visita disp/h 206,25'] = f(disp/4.5)
checks['visita saldo 478,11'] = f(disp - 450)
checks['visita Scanner 198,47'] = f((disp-35)/4.5)
checks['visita Scanner saldo 443,11'] = f(disp-35-450)
checks['visita 750 114,25'] = f((750*0.92 - 0.5*35 - 50 - 108.39)/4.5)
checks['visita 750 saldo 64,11'] = f(750*0.92 - 0.5*35 - 50 - 108.39 - 450)
checks['piso visita 1.169,45'] = f((900 + 17.5 + 50 + 108.39)/0.92)
checks['piso visita Scanner 1.207,49'] = f((900 + 17.5 + 50 + 108.39 + 35)/0.92)
# Laudo
dl = 3000*0.92 - 35 - 50 - 108.39
checks['laudo 311,10'] = f(dl/8.25); checks['laudo saldo 1.741,61'] = f(dl - 825); checks['laudo 250,40'] = f(dl/10.25)
checks['laudo piso 2.003,68'] = f((1650 + 35 + 50 + 108.39)/0.92)
# Vistoria e completa pequena
checks['dif completa 170,80'] = f(240*0.92 - 50)
checks['vistoria pequena 159,18'] = f((840*0.92 - 17.5 - 50 - 108.39)/3.75)
checks['vistoria média 199,57'] = f((1150*0.92 - 17.5 - 50 - 108.39)/4.42)
checks['vistoria grande 211,83'] = f((1400*0.92 - 17.5 - 50 - 108.39)/5.25)
# Reparo
checks['teto reparo 12.998'] = 'R$ 12.998'
# Gestão
checks['gestão 49.400'] = 'R$ 49.400'; checks['gestão 16,47%'] = '16,47%'; checks['gestão Bora 53.668'] = 'R$ 53.668'; checks['gestão 17,89%'] = '17,89%'
# Pré-obra
do = 5000*0.92 - 200 - 1200 - 70
checks['orçamento disp 3.130'] = 'R$ 3.130'; checks['orçamento 313'] = 'R$ 313'; checks['orçamento saldo 2.130'] = 'R$ 2.130'; checks['orçamento sem apoio saldo 1.330'] = 'R$ 1.330'
assert abs(do - 3130) < 0.01 and abs(do + 1200 - 3000 - 1330) < 0.01
# Condomínio
dc = 2200*0.92 - 105 - 100 - 23.80
checks['completo 179,52'] = f(dc/10); checks['completo saldo 795,20'] = f(dc - 1000); checks['completo piso 2.422,61'] = f((2000 + 105 + 100 + 23.80)/0.92)
checks['essencial 448,20'] = f(1600*0.92 - 23.80 - 1000); checks['essencial 23,20'] = f(1600*0.92 - 23.80 - 1000 - 375 - 50)
# Scanner
checks['scanner 8,75'] = 'R$ 8,75'; checks['scanner 43,75'] = 'R$ 43,75'
ok = 0
for k, v in checks.items():
    if v in flat: ok += 1
    else: print('FALTA NO PDF:', k, '->', v)
print(f'{ok}/{len(checks)} valores do consolidado conferidos no PDF')
# estrutura
r = PdfReader(pdf)
tops = [(r.get_destination_page_number(i)+1, re.sub(r'\s+', ' ', i.title)) for i in r.outline if not isinstance(i, list)]
titles = [t for _, t in tops]
fichas = ['Scanner da Obra · ficha interna', 'Visita, Laudo e Vistoria · ficha interna', 'Reparo Rápido · ficha interna', 'Gestão de Obra · ficha interna', 'Pré-obra com Arquitetos · ficha interna', 'Engenheiro do Condomínio · ficha interna']
norm = lambda s: re.sub(r'\s+', '', s)
for fi in fichas:
    print('ficha', 'OK ' if any(norm(fi) == norm(t) for t in titles) else 'FALTA', fi)
com = re.findall(r'(FRENTE \d[^\n]*PÁGINA COMERCIAL)', txt)
print('páginas comerciais:', len(com))
print('última seção:', titles[-1], '| página', tops[-1][0], 'de', len(r.pages))
print('exemplos simulados marcados [S]:', flat.count('[S]'))
