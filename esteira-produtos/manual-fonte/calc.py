# -*- coding: utf-8 -*-
"""Todas as contas do manual. Cada número exibido sai daqui."""
T = 0.08          # tributos [A]
AR = 100.0        # remuneração interna da hora do Aruak [D]
META = 200.0      # meta de disponível por hora do Aruak [P]
ADM = 35.0        # hora administrativa [E]
TEC = 60.0        # hora técnica [E]
IDA = 50.0        # deslocamento por ida [E]
ART1 = 108.39     # ART Tabela A até R$ 15 mil [R]
ART2 = 285.59     # ART Tabela A acima de R$ 15 mil [R]
ARTM = 23.80      # ART anual do condomínio alocada por mês (285,59/12)
ARTROT1 = 4.27    # ART de rotina até R$ 1.000 (só se o CREA-GO aceitar)
ARTROT2 = 6.38    # ART de rotina até R$ 2.000

def r2(x): return round(x + 1e-9, 2)

class E:
    """Economia de um contrato: receita, horas do Aruak e custos."""
    def __init__(s, nome, receita, h_aruak, custos, aquis=0.0, extra=None):
        s.nome = nome; s.receita = receita; s.h = h_aruak
        s.custos = custos          # lista de (descrição, valor)
        s.aquis = aquis; s.extra = extra or {}
    @property
    def trib(s): return r2(s.receita * T)
    @property
    def ccustos(s): return r2(sum(v for _, v in s.custos))
    @property
    def disp(s): return r2(s.receita - s.trib - s.ccustos - s.aquis)
    @property
    def ph(s): return r2(s.disp / s.h) if s.h else None
    @property
    def saldo(s): return r2(s.disp - s.h * AR)
    @property
    def pmin(s): return r2((META * s.h + s.ccustos + s.aquis) / (1 - T))

# ---------- 1. Scanner ----------
SC_CONTATO = r2(0.25 * ADM)            # 8,75
SC_VENDA20 = r2(SC_CONTATO * 5)        # 43,75
SC_VENDA_INC = r2(SC_CONTATO * 4)      # 35,00

# ---------- 2. Visita, laudo, vistoria ----------
def visita(preco=1200, aquis=0.0, h=4.5):
    return E('Visita', preco, h, [('Administrativo 0,5 h', 0.5*ADM), ('Uma ida', IDA), ('ART', ART1)], aquis)
V750 = visita(750); V1200 = visita(); V1200S = visita(aquis=SC_VENDA_INC); V1200S2 = visita(aquis=SC_VENDA20)
V1200_6h = visita(h=6.0)

def laudo(preco=3000, h=8.25, adm=1.0, idas=1, aquis=0.0):
    return E('Laudo', preco, h, [('Administrativo %s h' % adm, adm*ADM), ('Idas', idas*IDA), ('ART', ART1)], aquis)
L3000 = laudo(); L3000_10 = laudo(h=10.25); L3000S = laudo(aquis=SC_VENDA_INC)
L3700 = laudo(3700, 11.25, 1.5, 2)

# percurso visita + laudo com abatimento integral (a visita substitui a vistoria do laudo)
PERC = E('Visita + laudo com abatimento', 3000, 4.5 + 4.75,
         [('Administrativo 1,5 h', 1.5*ADM), ('Uma ida', IDA), ('Duas ART', 2*ART1)])
PERC_NOVA = E('Idem com nova vistoria', 3000, 4.5 + 4.75 + 3.0,
              [('Administrativo 1,5 h', 1.5*ADM), ('Duas idas', 2*IDA), ('Duas ART', 2*ART1)])
PERC_NOVA_50 = E('Nova vistoria, abatimento de 50%', 3600, 4.5 + 4.75 + 3.0,
              [('Administrativo 1,5 h', 1.5*ADM), ('Duas idas', 2*IDA), ('Duas ART', 2*ART1)])

VIST = {  # faixa: (preço V, horas V, preço C, horas C, campo informado)
    'ate100': (840, 3.75, 1080, 5.50, '1 h'),
    'meio':   (1150, 4.42, 1500, 6.50, '1 h 40'),
    'acima':  (1400, 5.25, 1950, 7.75, '2 h 30'),
}
def vist(preco, h, idas=1, art=ART1, aquis=0.0):
    return E('Vistoria', preco, h, [('Administrativo 0,5 h', 0.5*ADM), ('Idas', idas*IDA), ('ART', art)], aquis)
VI = {k: (vist(v[0], v[1]), vist(v[2], v[3], 2)) for k, v in VIST.items()}
VI_ROT = {'ate100': vist(840, 3.75, art=ARTROT1), 'meio': vist(1150, 4.42, art=ARTROT2), 'acima': vist(1400, 5.25, art=ARTROT2)}
VI_S = vist(1150, 4.42, aquis=SC_VENDA_INC)
# diferença da Completa pequena
DIF240 = r2(240*(1-T) - IDA)                 # 170,80
DIF240_MIN = round(DIF240 / META * 60)       # 51 min
# revisita avulsa no preço da meta
REV_H = {'ate100': 1.75, 'meio': 2.08, 'acima': 2.50}
REV_MIN = {k: r2((META*h + IDA + 0.25*ADM) / (1-T)) for k, h in REV_H.items()}

# ---------- 3. Reparo Rápido (Alexandre, simulado) ----------
RR_PRECO = 19400
RR_TETO = r2(RR_PRECO * (1 - T - 0.25))       # 12.998
RR_ITENS = [
    ('Sistema de microcimento, material com 5% de perdas', 3150.00, 'Cotação do fabricante ou distribuidor'),
    ('Aplicação do sistema (aplicador identificado)', 4560.00, 'Proposta escrita do aplicador'),
    ('Preparação da base e reassentamento de até 10% de peças', 700.00, 'Pedreiro ou aplicador'),
    ('Ralos, cantos e impermeabilização exigida pelo fabricante', 650.00, 'Ficha técnica do sistema'),
    ('Metais e acessórios previstos no escopo', 1400.00, 'Duas lojas'),
    ('Proteção dos ambientes vizinhos e limpeza final', 350.00, 'Lista de materiais'),
    ('Frete e descarte', 300.00, 'Transportadora ou caçamba'),
    ('Coordenação técnica, 8 h a R$ 60', 480.00, 'Agenda do coordenador'),
    ('Administrativo, 2 h a R$ 35', 70.00, 'Compras, NF e cobrança'),
    ('Deslocamentos, 6 idas a R$ 50', 300.00, 'Medição, início, verificações e entrega'),
    ('ART, contrato acima de R$ 15 mil', ART2, 'Tabela A do CREA-GO'),
]
RR_BASE_CONT = 3150 + 4560 + 700 + 650
RR_CONT = r2(RR_BASE_CONT * 0.08)
RR_ITENS.append(('Contingência: 8% de sistema, aplicação, base e ralos', RR_CONT, 'Reserva até a liberação'))
RR = E('Reparo Rápido', RR_PRECO, 10.5, [(a, b) for a, b, _ in RR_ITENS])
RR_S = E('Reparo Rápido via Scanner', RR_PRECO, 10.5, [(a, b) for a, b, _ in RR_ITENS], SC_VENDA_INC)
# caixa do reparo (dia, descrição, valor)
RR_CAIXA = [
    (0, 'Sinal de 50% na assinatura', 9700.00),
    (0, 'ART', -ART2),
    (2, 'Material do sistema, metais e proteção', -(3150 + 1400 + 350)),
    (5, 'Aplicador: 30% na mobilização', -1368.00),
    (7, 'Preparação da base', -700.00),
    (8, 'Ralos e impermeabilização', -650.00),
    (12, '40% no fim dos trabalhos no local', 7760.00),
    (12, 'Aplicador: 70% no fim', -3192.00),
    (12, 'Frete e descarte', -300.00),
    (19, '10% na liberação para uso', 1940.00),
    (30, 'Equipe interna e deslocamentos (folha do mês)', -(480 + 70 + 300)),
    (40, 'Tributos sobre o recebido', -RR.trib),
]
def caixa(lancs):
    acc = 0.0; out = []; minimo = 0.0
    for d, desc, v in lancs:
        acc = r2(acc + v); out.append((d, desc, v, acc)); minimo = min(minimo, acc)
    return out, minimo
RR_FLUXO, RR_PICO = caixa(RR_CAIXA)
RR_FINAL = RR_FLUXO[-1][3]
assert abs(RR_FINAL - RR_CONT - RR.disp) < 0.01, (RR_FINAL, RR_CONT, RR.disp)

# ---------- 4. Gestão de Obra ----------
G_OBRA = 300000.0; G_MESES = 4
G_TAXA = 0.098; G_TAXA_VAL = r2(G_OBRA * G_TAXA)         # 29.400
G_FIXO = 5000.0; G_FIXO_BORA = 6067.18
G_TOTAL_A = r2(G_FIXO * G_MESES + G_TAXA_VAL)           # 49.400
G_TOTAL_BORA = r2(6067 * G_MESES + G_TAXA_VAL)           # 53.668
G_MENSAL = r2(G_TOTAL_A / G_MESES)                       # 12.350
G_PRORROG = r2(G_MENSAL * 0.6)                           # 7.410
G_H_AR = 20.0; G_H_COM = 26.67                           # 8 h por proposta ÷ 30%
G_COORD_H = 32.0; G_ADM_H = 6.0; G_IDAS = 12
G_MES_CUSTO = r2(G_COORD_H*TEC + G_ADM_H*ADM + G_IDAS*IDA)  # 2.730
G_PISO = r2((G_H_AR*META + G_MES_CUSTO + ART2/G_MESES) / (1-T))
def gestao(receita, meses):
    return E('Gestão', receita, G_H_AR*meses + G_H_COM,
             [('Equipe e idas', G_MES_CUSTO*meses), ('ART', ART2)])
G_CASOS = {
  'A': ('Fixo R$ 5.000 + taxa média de 9,8%', [G_TOTAL_A, G_TOTAL_A, r2(G_FIXO*6 + G_TAXA_VAL), G_TOTAL_A]),
  'B': ('Honorário mensal R$ 12.350, prorrogação a R$ 7.410', [G_TOTAL_A, G_TOTAL_A, r2(G_TOTAL_A + 2*G_PRORROG), r2(G_TOTAL_A + 2*G_PRORROG)]),
  'C': ('16,47% sobre o custo, mínimo de R$ 5.000 compensável', [G_TOTAL_A, G_TOTAL_A, G_TOTAL_A, G_TOTAL_A]),
}
G_COLS = ['4 meses, no prazo', '6 meses, atraso da Entre Colunas', '6 meses, alteração do cliente', '6 meses, causa externa']
G_RES = {k: [gestao(v, 4 if i == 0 else 6) for i, v in enumerate(vals)] for k, (_, vals) in G_CASOS.items()}
# mês-tipo da obra (para o cenário mensal)
G_MES_A = E('Gestão, obra-mês', G_MENSAL, G_H_AR + 6.67, [('Equipe e idas', G_MES_CUSTO), ('ART alocada', r2(ART2/4))])
# Medeiros: o que custaria hoje
MED_OBRA = 253320.82; MED_MESES = 9
MED_A = r2(G_FIXO*MED_MESES + MED_OBRA*G_TAXA)
MED_LEVE = r2((10*META + 24*TEC + 6*ADM + 9*IDA + ART2/MED_MESES) / (1-T))
MED_LEVE_TOT = r2(MED_LEVE*MED_MESES)

# ---------- 5. Pré-obra ----------
ORC = E('Orçamento executivo com apoio', 5000, 10, [('Técnico 20 h', 20*TEC), ('Administrativo 2 h', 2*ADM), ('Outros diretos (ART, uma ida, impressão)', 200.0)])
ORC_SEM = E('Orçamento executivo sem apoio', 5000, 30, [('Administrativo 2 h', 2*ADM), ('Outros diretos', 200.0)])
ORC_ADV = E('Orçamento, +30% de horas, com apoio', 5000, 13, [('Técnico 26 h', 26*TEC), ('Administrativo 2,6 h', 2.6*ADM), ('Outros diretos', 200.0)])
ORC_ADV_SEM = E('Orçamento, +30% de horas, sem apoio', 5000, 39, [('Administrativo 2,6 h', 2.6*ADM), ('Outros diretos', 200.0)])
EVF = E('Viabilidade com apoio', 2500, 6, [('Técnico 8 h', 8*TEC), ('Administrativo 1 h', ADM), ('Uma ida', IDA), ('ART', ART1)])
EVF_SEM = E('Viabilidade sem apoio', 2500, 12, [('Administrativo 1 h', ADM), ('Uma ida', IDA), ('ART', ART1)])
ORC_SR = E('Orçamento com orçamentista sênior', 5000, 6, [('Técnico 24 h', 24*TEC), ('Administrativo 2 h', 2*ADM), ('Outros diretos', 200.0)])

# ---------- 6. Condomínio ----------
YAN_ESS = 6.25; YAN_COMP = 11.0
def cond(preco, h, yan_h=0.0, adm_h=3.0, idas=1, art=ARTM, nome='Cond'):
    c = [('Administrativo %s h' % adm_h, adm_h*ADM), ('Idas', idas*IDA), ('ART alocada', art)]
    if yan_h: c.append(('Yan %s h' % yan_h, yan_h*TEC))
    return E(nome, preco, h, c)
ESS_AR = cond(1600, 6.5, nome='Essencial, Aruak no campo')
ESS_SUP = cond(1600, 5.0, YAN_ESS, nome='Essencial, supervisão (Aruak e Yan)')
ESS_DEL = cond(1600, 2.0, YAN_ESS, nome='Essencial, Yan no campo')
COMP_AR = cond(2200, 10.0, idas=2, nome='Completo, Aruak no campo')
COMP_SUP = cond(2200, 8.0, YAN_COMP, idas=2, nome='Completo, supervisão')
COMP_DEL = cond(2200, 3.0, YAN_COMP, idas=2, nome='Completo, Yan no campo')
ESS_448 = r2(1600*(1-T) - ARTM - 5*META)      # 448,20
ESS_23 = r2(ESS_448 - YAN_ESS*TEC - IDA)       # 23,20
IMPL_AV = E('Implantação avulsa (Aruak + Yan)', 2600, 8, [('Yan 8 h', 8*TEC), ('Administrativo 2 h', 2*ADM), ('Duas idas', 2*IDA), ('ART', ART1)])
IMPL_AV_SO = E('Implantação avulsa (só Aruak)', 2600, 14, [('Administrativo 2 h', 2*ADM), ('Duas idas', 2*IDA), ('ART', ART1)])
IMPL_CUSTO_Y = 8*TEC + 2*ADM + 2*IDA     # 650 dentro da assinatura
IMPL_CUSTO_S = 2*ADM + 2*IDA              # 170 só Aruak
def assin(meses, plano='ess', via='yan'):
    mens = 1600 if plano == 'ess' else 2200
    receita = 2600 + mens*meses
    if via == 'yan':
        h = 8.0; c = IMPL_CUSTO_Y
        for m in range(1, meses+1):
            if plano == 'ess':
                sup = m <= 3
                h += 5.0 if sup else 2.0
                c += YAN_ESS*TEC + 3*ADM + IDA
            else:
                sup = m <= 3
                h += 8.0 if sup else 3.0
                c += YAN_COMP*TEC + 3*ADM + 2*IDA
    else:
        h = 14.0; c = IMPL_CUSTO_S
        for m in range(1, meses+1):
            if plano == 'ess':
                h += 6.5; c += 3*ADM + IDA
            else:
                h += 10.0; c += 3*ADM + 2*IDA
    return E('Assinatura %d meses' % meses, receita, h, [('Equipe, idas e administrativo', r2(c)), ('ART anual', ART2)])
CMP = {
  'av_y': IMPL_AV, 'av_s': IMPL_AV_SO,
  **{('ess_y', m): assin(m, 'ess', 'yan') for m in (3, 6, 12)},
  **{('ess_s', m): assin(m, 'ess', 'so') for m in (3, 6, 12)},
  **{('comp_y', m): assin(m, 'comp', 'yan') for m in (3, 6, 12)},
}
EMPRESA = E('Engenheiro da Empresa', 3000, 7, [('Administrativo 2 h', 2*ADM), ('Uma ida', IDA), ('ART alocada', ARTM)])
TIPTOY_TRIB = r2(1800*T)

# ---------- Estrutura da empresa: patamares ----------
G_B = E('Gestão, coordenador forte', G_MENSAL, 12.0, [('Coordenador 48 h', 48*TEC), ('Administrativo 6 h', 6*ADM), ('14 idas', 14*IDA), ('ART alocada', r2(ART2/4))])
G_C = E('Gestão, engenheiro de obras e canal', G_MENSAL, 1.5, [('Engenheiro 10 h a R$ 100', 1000.0), ('Coordenador 48 h', 48*TEC), ('Administrativo 8 h', 8*ADM), ('14 idas', 14*IDA), ('ART alocada', r2(ART2/4)), ('Aquisição pelo canal', 750.0)])
RR_DEL = E('Reparo, coordenador conduz', RR_PRECO, 6.0, [(a, b) for a, b, _ in RR_ITENS] + [('Técnico +4 h', 4*TEC)])
RR_ENG = E('Reparo, engenheiro conduz', RR_PRECO, 1.0, [(a, b) for a, b, _ in RR_ITENS] + [('Técnico +4 h', 4*TEC), ('Engenheiro 5 h', 500.0)])
ORC_ENG = E('Orçamento, engenheiro revisa', 5000, 1.0, [('Técnico 24 h', 24*TEC), ('Administrativo 2 h', 2*ADM), ('Outros diretos', 200.0), ('Engenheiro 5 h', 500.0)])
EVF_ENG = E('EVF, engenheiro conduz', 2500, 1.0, [('Técnico 8 h', 8*TEC), ('Administrativo 1 h', ADM), ('Uma ida', IDA), ('ART', ART1), ('Engenheiro 5 h', 500.0)])
VIS_ENG = E('Visita, engenheiro conduz', 1200, 0.5, [('Administrativo 0,5 h', 0.5*ADM), ('Uma ida', IDA), ('ART', ART1), ('Engenheiro 4 h', 400.0)], SC_VENDA_INC)
VIST_JR = E('Vistoria 101 a 249 m², júnior no campo', 1150, 0.5, [('Administrativo 1 h', ADM), ('Uma ida', IDA), ('ART', ART1), ('Júnior 3,92 h', r2(3.92*TEC))])
ESS_JR = cond(1600, 0.5, YAN_ESS, nome='Essencial, júnior revisa'); ESS_JR.custos.append(('Júnior 1,5 h', 1.5*TEC))
COMP_JR = cond(2200, 1.0, YAN_COMP, idas=2, nome='Completo, júnior revisa'); COMP_JR.custos.append(('Júnior 2 h', 2*TEC))

def mix(itens, interna_h):
    rec = sum(e.receita*q for e, q, _ in itens)
    trib = sum(e.trib*q for e, q, _ in itens)
    cus = sum((e.ccustos + e.aquis)*q for e, q, _ in itens)
    lb = sum(e.disp*q for e, q, _ in itens)
    h = sum(e.h*q for e, q, _ in itens) + interna_h
    return dict(rec=r2(rec), trib=r2(trib), cus=r2(cus), lb=r2(lb), h=r2(h), rem=r2(h*AR), saldo=r2(lb - h*AR))

P1_ITENS = [
  (G_MES_A, 1, '1 obra em Gestão (honorário mensal)'),
  (RR, 1, '1 Reparo Rápido de banheiro'),
  (ORC, 1, '1 orçamento executivo, com apoio técnico'),
  (EVF, 1, '1 estudo de viabilidade'),
  (L3000, 1, '1 laudo'),
  (V1200, 1, '1 visita por indicação direta'),
  (V1200S, 3, '3 visitas vindas do Scanner'),
  (VI['meio'][0], 5, '5 vistorias de 101 a 249 m²'),
  (ESS_SUP, 1, 'Trípoli no Essencial, em supervisão'),
]
P1 = mix(P1_ITENS, 4.0)
P2_ITENS = [
  (G_B, 5, '5 obras em Gestão, coordenador forte'),
  (RR_DEL, 2, '2 Reparos, coordenador conduz'),
  (ORC_SR, 2, '2 orçamentos, orçamentista sênior'),
  (EVF, 1, '1 estudo de viabilidade'),
  (L3000, 1, '1 laudo'),
  (V1200S, 1, '1 visita do Scanner'),
  (ESS_DEL, 4, '4 condomínios Essencial, Yan no campo'),
  (COMP_DEL, 1, '1 condomínio Completo, Yan no campo'),
]
P2 = mix(P2_ITENS, 6.0)
P3_ITENS = [
  (G_C, 10, '10 obras em Gestão, engenheiro de obras'),
  (RR_ENG, 4, '4 Reparos'),
  (ORC_ENG, 3, '3 orçamentos executivos'),
  (EVF_ENG, 2, '2 estudos de viabilidade'),
  (L3000, 2, '2 laudos (Aruak)'),
  (VIS_ENG, 2, '2 visitas'),
  (VIST_JR, 8, '8 vistorias, júnior no campo'),
  (ESS_JR, 10, '10 condomínios Essencial'),
  (COMP_JR, 2, '2 condomínios Completo'),
]
P3 = mix(P3_ITENS, 30.0)
P4_ITENS = [
  (G_C, 22, '22 obras em Gestão'),
  (RR_ENG, 6, '6 Reparos'),
  (ORC_ENG, 5, '5 orçamentos executivos'),
  (EVF_ENG, 3, '3 estudos de viabilidade'),
  (L3000, 2, '2 laudos (Aruak)'),
  (VIS_ENG, 4, '4 visitas'),
  (VIST_JR, 16, '16 vistorias, júnior no campo'),
  (ESS_JR, 20, '20 condomínios Essencial'),
  (COMP_JR, 5, '5 condomínios Completo'),
]
P4 = mix(P4_ITENS, 30.0)
ESTR = {'P1': 15000.0, 'P2': 24000.0, 'P3': 45000.0, 'P4': 80000.0}   # estrutura não alocada [E]
RESV = {'P1': 1*250 + 1*582, 'P2': 5*250 + 2*582, 'P3': 10*250 + 4*582, 'P4': 22*250 + 6*582}
for k, P in (('P1', P1), ('P2', P2), ('P3', P3), ('P4', P4)):
    P['estr'] = ESTR[k]; P['resv'] = r2(RESV[k]); P['cx'] = r2(P['saldo'] - ESTR[k] - RESV[k])

if __name__ == '__main__':
    def show(e):
        print('%-45s rec %9.2f disp %9.2f h %6.2f ph %8.2f saldo %9.2f pmin %9.2f' % (e.nome, e.receita, e.disp, e.h, e.ph or 0, e.saldo, e.pmin))
    print('Scanner', SC_CONTATO, SC_VENDA20, SC_VENDA_INC)
    for e in (V750, V1200, V1200S, V1200S2, V1200_6h, L3000, L3000_10, L3000S, L3700, PERC, PERC_NOVA, PERC_NOVA_50): show(e)
    for k, (v, c) in VI.items(): show(v); show(c)
    for k, e in VI_ROT.items(): show(e)
    show(VI_S)
    print('dif240', DIF240, DIF240_MIN, 'revisita', REV_MIN)
    print('RR teto', RR_TETO, 'custos', RR.ccustos, 'cont', RR_CONT); show(RR); show(RR_S)
    for f in RR_FLUXO: print('  ', f)
    print('pico', RR_PICO, 'final', RR_FINAL)
    print('Gestao', G_TOTAL_A, G_TOTAL_BORA, G_MENSAL, G_PRORROG, 'piso', G_PISO, 'mes custo', G_MES_CUSTO)
    for k, rs in G_RES.items():
        for c, e in zip(G_COLS, rs): print('  ', k, c, e.receita, e.disp, e.h, e.ph, e.saldo)
    show(G_MES_A)
    print('Medeiros', MED_A, MED_A/MED_OBRA, MED_LEVE, MED_LEVE_TOT, MED_LEVE_TOT/MED_OBRA)
    for e in (ORC, ORC_SEM, ORC_ADV, ORC_ADV_SEM, EVF, EVF_SEM, ORC_SR): show(e)
    for e in (ESS_AR, ESS_SUP, ESS_DEL, COMP_AR, COMP_SUP, COMP_DEL, IMPL_AV, IMPL_AV_SO, EMPRESA): show(e)
    print('ess448', ESS_448, ESS_23)
    for k, e in CMP.items(): print(k, end=' '); show(e)
    for e in (G_B, G_C, RR_DEL, RR_ENG, ORC_ENG, EVF_ENG, VIS_ENG, VIST_JR, ESS_JR, COMP_JR): show(e)
    for k, P in (('P1', P1), ('P2', P2), ('P3', P3), ('P4', P4)): print(k, P)
