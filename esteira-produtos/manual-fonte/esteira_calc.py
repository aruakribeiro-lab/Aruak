# -*- coding: utf-8 -*-
"""Contas dos produtos novos e das comissões da esteira em seis itens."""
from calc import *
from plano_calc import *

def com(e, taxa):
    """Mesmo contrato com comissão de parceiro (percentual do preço) no lugar do custo de aquisição do Scanner."""
    return E(e.nome + ' com comissão', e.receita, e.h, e.custos, r2(e.receita * taxa))

# Segurança do trabalho (empresa de até 20 funcionários, uma unidade) [P]
PGR = E('PGR', 2200.0, 9.0, [('Administrativo 1 h', ADM), ('Uma ida', IDA), ('ART', ART1)])
LTCAT = E('LTCAT', 3800.0, 14.0, [('Administrativo 1 h', ADM), ('Duas idas', 2 * IDA), ('Aluguel de equipamento de medição', 300.0), ('ART', ART1)])
SST_PAC = E('PGR + LTCAT', 5400.0, 20.0, [('Administrativo 1,5 h', 1.5 * ADM), ('Duas idas', 2 * IDA), ('Aluguel de equipamento de medição', 300.0), ('Duas ART', 2 * ART1)])
# Regularização (até 150 m²) [P]
REG_DIAG = E('Diagnóstico de regularização', 1200.0, 4.5, [('Administrativo 1 h', ADM), ('Uma ida', IDA), ('Certidões', 80.0)])
REG = E('Regularização completa até 150 m²', 5000.0, 12.0, [('Desenhista técnico 12 h', 12 * TEC), ('Administrativo 3 h', 3 * ADM), ('Três idas', 3 * IDA), ('ART', ART1)])
# Assistência técnica de parte [P]
ASSIST = E('Assistência técnica', 6000.0, 19.0, [('Administrativo 2 h', 2 * ADM), ('Duas idas', 2 * IDA), ('ART', ART1)])
# EIV e EIT: análise de enquadramento [P]
EIV_ENQ = E('Análise de enquadramento EIV/EIT', 800.0, 3.0, [('Administrativo 0,5 h', 0.5 * ADM)])
# Fiscalização de obra (modelo gestor, sem coordenar compras) [P]
FISC_H = 10.0
FISC = E('Fiscalização, por mês', 3500.0, FISC_H, [('Técnico 8 h', 8 * TEC), ('Administrativo 4 h', 4 * ADM), ('Cinco idas', 5 * IDA), ('ART alocada (4 meses)', r2(ART2 / 4))])
# Escola e empresa
ESCOLA = E('Engenheiro da Escola', 1800.0, 5.0, [('Administrativo 2 h', 2 * ADM), ('Uma ida', IDA), ('ART alocada', ARTM)])

if __name__ == '__main__':
    for e in (PGR, LTCAT, SST_PAC, REG_DIAG, REG, ASSIST, EIV_ENQ, FISC, ESCOLA, ESS_AR, COMP_AR, EMPRESA, V1200, L3000, VI['ate100'][0], VI['meio'][0], VI['acima'][0], VI['ate100'][1], VI['meio'][1], VI['acima'][1], EVF, ORC, CM, PT):
        print(f'{e.nome:40s} {e.receita:8.0f} h {e.h:5.2f} ph {e.ph:7.2f} pmin {e.pmin:8.2f}')
    print('--- comissões')
    for e, t in ((L3000, .10), (L3000, .15), (VI['ate100'][0], .10), (VI['ate100'][0], .15), (VI['meio'][0], .10), (VI['meio'][0], .15), (VI['acima'][0], .15), (VI['meio'][1], .15), (REG, .10), (EVF, .10), (ORC, .10), (G_MES_A, .04), (FISC, .04), (PT, .04), (CM, .10)):
        c = com(e, t); print(f'{e.nome:40s} {int(t*100)}% com {c.aquis:8.2f} ph {e.ph:7.2f} -> {c.ph:7.2f}')
