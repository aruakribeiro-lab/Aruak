# -*- coding: utf-8 -*-
"""Contas do produto Plano para Terminar a Obra (nível 1: Conferência da Medição; nível 2: Plano para Terminar)."""
from calc import *

# ---------- Nível 1 · Conferência da Medição ----------
CM_PRECO = 1800.0
CM_HORAS = [  # (etapa, Aruak, equipe)
    ('Conversa a partir do Raio-X e qualificação', 0.5, ''),
    ('Proposta, pagamento e agendamento', 0.0, '0,5 h adm'),
    ('Leitura de contrato, orçamento, medição e comprovantes', 1.5, ''),
    ('Visita à obra conferindo os serviços medidos, com trajeto', 2.5, ''),
    ('Nota de conferência serviço a serviço', 1.5, '0,5 h adm (formatação e envio)'),
    ('Devolutiva por videochamada (30 min)', 0.5, ''),
]
CM_H = sum(a for _, a, _ in CM_HORAS)  # 6,5
CM_CUSTOS = [('Administrativo 1 h', 1.0 * ADM), ('Uma ida', IDA), ('ART', ART1)]
CM = E('Conferência da Medição', CM_PRECO, CM_H, CM_CUSTOS)
CM_S = E('Conferência via Scanner', CM_PRECO, CM_H, CM_CUSTOS, SC_VENDA_INC)
CM_ADV = E('Conferência, documentos bagunçados (+2 h)', CM_PRECO, CM_H + 2, CM_CUSTOS, SC_VENDA_INC)
CM_1500 = E('Conferência a R$ 1.500', 1500.0, CM_H, CM_CUSTOS, SC_VENDA_INC)

# ---------- Nível 2 · Plano para Terminar ----------
PT_PRECO = 4500.0
PT_HORAS = [  # (etapa, Aruak, técnico, adm)
    ('Conversa a partir do Raio-X, proposta e fechamento', 1.0, 0, 0.5),
    ('Leitura de contrato, orçamento, medições e comprovantes', 1.5, 0, 0),
    ('Levantamento na obra: estado de cada etapa, medidas, fotos, pendências', 3.0, 3, 0),
    ('Saldo de serviços e quantitativos do que falta', 0, 8, 0),
    ('Cotações (2 fontes nos itens mais caros) e preço da equipe atual', 0, 8, 0),
    ('Conciliação do pago com o executado', 1.5, 0, 0),
    ('Revisão técnica, sequência, cronograma até a mudança e plano de caixa', 3.0, 0, 0),
    ('Apresentação na obra e uma rodada de ajuste', 2.5, 0, 1.0),
]
PT_A = sum(x[1] for x in PT_HORAS)    # 12,5
PT_T = sum(x[2] for x in PT_HORAS)    # 19
PT_ADM = sum(x[3] for x in PT_HORAS)  # 1,5
PT_IDAS = 2
def pt(preco=PT_PRECO, a=PT_A, t=PT_T, adm=PT_ADM, idas=PT_IDAS, aquis=SC_VENDA_INC, nome='Plano para Terminar'):
    custos = [('Técnico %s h' % str(t).replace('.', ','), t * TEC), ('Administrativo %s h' % str(adm).replace('.', ','), adm * ADM),
              ('Idas', idas * IDA), ('ART', ART1)]
    return E(nome, preco, a, custos, aquis)
PT = pt()
PT_SEM = pt(a=PT_A + PT_T, t=0, nome='Plano sem apoio técnico')
PT_ADV = pt(a=r2(PT_A * 1.3), t=r2(PT_T * 1.3), adm=r2(PT_ADM * 1.3), nome='Plano, obra sem documentos (+30%)')
PT_POS = pt(3900.0, a=PT_A - 3.0, nome='Plano depois da Conferência (R$ 3.900)')  # sem leitura de documentos e conciliação já feitas
PT_POS_ADV = pt(3900.0, a=r2((PT_A - 3.0) * 1.3), t=r2(PT_T * 1.3), adm=r2(PT_ADM * 1.3), nome='Idem, obra sem documentos (+30%)')

# Percurso completo do cliente que começa pela Conferência
PERC_CP = r2(CM_PRECO + 3900.0)  # 5.700

# Caixa do Plano: 50% na contratação, 50% na apresentação. Saídas antes da 2ª parcela: ART e primeira ida; técnico pago na entrega.
PT_SAIDAS_ANTES = r2(ART1 + IDA)
PT_CAIXA_1 = r2(PT_PRECO * 0.5 - PT_SAIDAS_ANTES - r2(PT_PRECO * 0.5 * T))

if __name__ == '__main__':
    for e in (CM, CM_S, CM_ADV, CM_1500, PT, PT_SEM, PT_ADV, PT_POS, PT_POS_ADV):
        print(f'{e.nome:45s} rec {e.receita:8.2f} custos {e.ccustos:8.2f} aquis {e.aquis:5.2f} disp {e.disp:8.2f} h {e.h:5.2f} ph {e.ph:7.2f} saldo {e.saldo:8.2f} pmin {e.pmin:8.2f}')
    print('caixa 1a parcela', PT_CAIXA_1, 'percurso', PERC_CP)

PT_5500 = pt(5500.0, a=r2(PT_A * 1.3), t=r2(PT_T * 1.3), adm=r2(PT_ADM * 1.3), nome='Plano a R$ 5.500, obra sem documentos (+30%)')
