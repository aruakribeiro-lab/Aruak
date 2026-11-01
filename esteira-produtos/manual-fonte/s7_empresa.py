# -*- coding: utf-8 -*-
from common import *

# horas de equipe por unidade, por função: (coord/Yan, técnico ou orçamentista, engenheiro, júnior, adm)
ROLE = {
    id(G_MES_A): (32, 0, 0, 0, 6), id(RR): (0, 8, 0, 0, 2), id(ORC): (0, 20, 0, 0, 2), id(EVF): (0, 8, 0, 0, 1),
    id(L3000): (0, 0, 0, 0, 1), id(V1200): (0, 0, 0, 0, 0.5), id(V1200S): (0, 0, 0, 0, 0.5), id(VI['meio'][0]): (0, 0, 0, 0, 0.5),
    id(ESS_SUP): (6.25, 0, 0, 0, 3), id(G_B): (48, 0, 0, 0, 6), id(RR_DEL): (0, 12, 0, 0, 2), id(ORC_SR): (0, 24, 0, 0, 2),
    id(ESS_DEL): (6.25, 0, 0, 0, 3), id(COMP_DEL): (11, 0, 0, 0, 3), id(G_C): (48, 0, 10, 0, 8), id(RR_ENG): (0, 12, 5, 0, 2),
    id(ORC_ENG): (0, 24, 5, 0, 2), id(EVF_ENG): (0, 8, 5, 0, 1), id(VIS_ENG): (0, 0, 4, 0, 0.5), id(VIST_JR): (0, 0, 0, 3.92, 1),
    id(ESS_JR): (6.25, 0, 0, 1.5, 3), id(COMP_JR): (11, 0, 0, 2, 3),
}

def roles(itens):
    s = [0.0] * 5
    for e, q, _ in itens:
        for i, v in enumerate(ROLE[id(e)]):
            s[i] += v * q
    return [r2(x) for x in s]

def comparativa():
    rows = [
        ['1 Scanner', 'Triagem gratuita', 'Grátis', '0', '15 min adm por contato', '—', '—', '—', brl(SC_VENDA20, True) + ' por venda (R$ 35 se o vencedor já está no produto)', '0', 'Em teste'],
        ['2 Visita', 'Visita Diagnóstica', brl(1200), hh(V1200.h), '0,5 h adm', brl(V1200.disp), brl(V1200.ph), brl(V1200.saldo), '100% antes; pico R$ 0', '0', 'Em teste'],
        ['2 Laudo', 'Laudo delimitado', brl(3000), hh(L3000.h), '1 h adm', brl(L3000.disp), brl(L3000.ph), brl(L3000.saldo), '50% e 50%; pico R$ 0', '0', 'Vendido'],
        ['2 Vistoria', '100 a 250 m²', brl(1150), hh(VI['meio'][0].h), '0,5 h adm', brl(VI['meio'][0].disp), brl(VI['meio'][0].ph), brl(VI['meio'][0].saldo), 'Na confirmação; pico R$ 0', '0', 'Vendido'],
        ['3 Reparo Rápido', 'Banheiro ' + tag('S'), brl(RR.receita), hh(RR.h), '8 h técnico + 2 h adm + aplicador', brl(RR.disp), brl(RR.ph), brl(RR.saldo), '50/40/10; menor acumulado ' + brl(min(a for _, _, _, a in RR_FLUXO), True), '0', 'Sob consulta'],
        ['4 Gestão', 'Obra de R$ 300 mil, 4 meses ' + tag('S'), brl(G_TOTAL_A), hh(G_RES['B'][0].h), '32 h coord. + 6 h adm por mês', brl(G_RES['B'][0].disp), brl(G_RES['B'][0].ph), brl(G_RES['B'][0].saldo), 'Mensal antecipado; pico R$ 0', '0', 'Sob consulta'],
        ['5 Pré-obra', 'Orçamento executivo', brl(5000), hh(ORC.h), '20 h técnico + 2 h adm', brl(ORC.disp), brl(ORC.ph), brl(ORC.saldo), '50% e 50%; pico R$ 0', '0', 'Em teste'],
        ['5 Pré-obra', 'Estudo de viabilidade', brl(2500), hh(EVF.h), '8 h técnico + 1 h adm', brl(EVF.disp), brl(EVF.ph), brl(EVF.saldo), '50% e 50%; pico R$ 0', '0 (Cleber: histórico)', 'Em teste'],
        ['6 Condomínio', 'Implantação avulsa', brl(2600), hh(IMPL_AV.h), '8 h Yan + 2 h adm', brl(IMPL_AV.disp), brl(IMPL_AV.ph), brl(IMPL_AV.saldo), '50% e 50%; pico R$ 0', '0', 'Em teste'],
        ['6 Condomínio', 'Essencial, Aruak no campo', brl(1600) + '/mês', hh(ESS_AR.h), '3 h adm', brl(ESS_AR.disp), brl(ESS_AR.ph), brl(ESS_AR.saldo), 'Mensal; pico R$ 0', '0', 'Em teste'],
        ['6 Condomínio', 'Essencial, Yan no campo', brl(1600) + '/mês', hh(ESS_DEL.h), '6,25 h Yan + 3 h adm', brl(ESS_DEL.disp), brl(ESS_DEL.ph), brl(ESS_DEL.saldo), 'Mensal; pico R$ 0', '0', 'Após passagem'],
        ['6 Condomínio', 'Completo, Aruak no campo', brl(2200) + '/mês', hh(COMP_AR.h), '3 h adm', brl(COMP_AR.disp), brl(COMP_AR.ph), brl(COMP_AR.saldo), 'Mensal; pico R$ 0', '0', 'Em teste'],
    ]
    t = table(['Frente', 'Oferta', 'Preço', 'Horas do Aruak', 'Equipe', 'Disponível', 'Por hora do Aruak', 'Saldo parcial', 'Recebimento e caixa', 'Medidos', 'Estágio'], rows, 'sm',
              widths=['9%', '13%', '8%', '7%', '12%', '8%', '8%', '8%', '14%', '6%', '7%'])
    leit = box('Como ler a tabela', '<p>Nenhum produto tem horas medidas em contrato ainda: a coluna “medidos” é o placar que precisa mudar até 18/12. Por hora do Aruak, os que mais rendem são os que usam equipe (gestão, orçamento com apoio, condomínio com o Yan, reparo). Os que mais dependem do Aruak (visita, vistoria pequena, condomínio com ele no campo) ficam perto ou abaixo da meta de R$ 200/h e não escalam sem delegação.</p>')
    return page('Estrutura da empresa', 'Comparativo das seis frentes', 'Mesmas premissas para todas as ofertas: 8% de tributos, Aruak a R$ 100/h no saldo, meta de R$ 200/h, técnico a R$ 60/h, administrativo a R$ 35/h.',
        t + leit)

def patamar_table():
    P = {'P1': (P1, P1_ITENS), 'P2': (P2, P2_ITENS), 'P3': (P3, P3_ITENS), 'P4': (P4, P4_ITENS)}
    rows = []
    lab = {'rec': 'Receita própria do mês', 'trib': '(−) Tributos', 'cus': '(−) Custos diretos (equipe alocada, terceiros, ART, idas, aquisição)',
           'lb': '= Lucro bruto (disponível antes do Aruak)', 'h': 'Horas do Aruak no mês', 'rem': '(−) Remuneração do Aruak (h × R$ 100)',
           'saldo': '= Saldo dos produtos', 'estr': '(−) Estrutura não alocada ' + tag('E'), 'resv': '(−) Reservas de pós-entrega ' + tag('P'), 'cx': '= Caixa livre do mês, antes da dívida'}
    for k in ('rec', 'trib', 'cus', 'lb', 'h', 'rem', 'saldo', 'estr', 'resv', 'cx'):
        r = [lab[k], 'R$ 30.000 ' + tag('A') if k == 'lb' else ('a apurar' if k in ('rec', 'h', 'rem', 'saldo', 'estr', 'cx') else '—')]
        for p in ('P1', 'P2', 'P3', 'P4'):
            v = P[p][0][k]
            if k == 'h':
                r.append(hh(v))
            elif k in ('trib', 'cus', 'rem', 'estr', 'resv'):
                r.append(brl(-v, False))
            else:
                r.append(brl(v, False))
        cls = 'tot' if k in ('lb', 'saldo', 'cx') else ''
        rows.append({'cls': cls, 'cells': r})
    return table(['Linha', 'Hoje', 'Patamar 1', 'Patamar 2', 'Patamar 3', 'Patamar 4'], rows, 'sm num', widths=['36%', '12%', '13%', '13%', '13%', '13%'])

def cenario():
    rows = []
    for e, q, d in P1_ITENS:
        rows.append([d, str(q), brl(e.receita * q), brl(r2(e.disp * q)), hh(r2(e.h * q))])
    rows.append(['Gestão da empresa, Scanner e reunião semanal', '', '—', '—', hh(4)])
    t = table(['Carteira do mês ' + tag('S'), 'Qtd.', 'Receita', 'Lucro bruto', 'Horas do Aruak'], rows, 'sm num', widths=['52%', '7%', '14%', '14%', '13%'],
              foot=['Total', '', brl(P1['rec']), brl(P1['lb']), hh(P1['h'])])
    ro = roles(P1_ITENS)
    cap = table(['Quem', 'Horas no mês', 'Cabe na equipe atual?'], [
        ['Aruak', hh(P1['h']), 'Sim, até 120 h ' + tag('P') + '; sobra folga para imprevistos e para a dívida'],
        ['Yan: coordenação da obra e condomínio', hh(ro[0]), 'Só se ele confirmar cerca de 40 h livres por mês'],
        ['Apoio técnico: orçamento, viabilidade e cotações do reparo', hh(ro[1]), 'Não existe hoje: freelancer pago por entrega <span class="tg">[pendente]</span>'],
        ['Administrativo (Gabriela), sem contar o Scanner', hh(ro[4]), 'Sim'],
    ], 'sm', widths=['40%', '16%', '44%'])
    sem = r2(P1['h'] + 20 + 6 + 3)
    nota = (f'<p><b>Leitura.</b> Com a mesma agenda, a mesma equipe e o mesmo caixa, as seis frentes produzem cerca de <b>{brl(P1["lb"])}</b> de lucro bruto com {hh(P1["h"])} do Aruak: a mesma ordem de grandeza dos R$ 30 mil de hoje. O ganho do primeiro patamar não é volume: é lucro medido por produto, nenhum dinheiro de cliente no caixa da empresa e menos horas do Aruak no canteiro. '
            f'Sem apoio técnico, o orçamento, a viabilidade e as cotações voltam para o Aruak e a agenda vai a cerca de {hh(sem)}: estoura o limite.</p>'
            '<p class="small">Nenhum produto pede dinheiro antes de receber: visita, laudo, vistoria, pré-obra e condomínio recebem antes do campo; o reparo compra só depois do sinal; a gestão recebe o honorário antes do mês. A dívida antiga fica em controle separado e não é paga com dinheiro de contrato em andamento.</p>')
    return page('Estrutura da empresa', 'Cenário mensal com a mesma agenda, equipe e caixa', 'Uma carteira possível para um mês do primeiro patamar, sem somar capacidades máximas incompatíveis.',
        t + cap + nota)

def patamares():
    tab = patamar_table()
    provas = table(['Para passar de', 'O que precisa estar provado (com números do Placar, do Painel de Obras e do Mais Controle)', 'Quem precisa existir'], [
        ['Hoje para o Patamar 1 (≈ R$ 30 mil, com outra qualidade)', 'Cada produto em teste com pelo menos 2 contratos medidos nos três indicadores · Scanner com 30 formulários e custo por cliente pago · primeira gestão com honorário recebido em dia por 2 meses · nenhum dinheiro de cliente no caixa · Trípoli decidido · os R$ 30 mil de hoje abertos por produto', 'Equipe atual, apoio técnico por entrega, papéis aceitos em 03/11'],
        ['Patamar 1 para o 2 (≈ R$ 60 mil)', 'Coordenador conduz 2 obras por 8 semanas sem o Aruak na rotina (até 12 h dele por obra e mês) · regra de prorrogação aplicada sem disputa · 3 estudos de pré-obra pagos e 1 convertido em gestão · Yan aprovado na regra de passagem em 2 condomínios e 4 condomínios pagando · 3 meses seguidos de caixa livre positivo depois da estrutura · canal com contratos pagos e custo de aquisição conhecido', '2º coordenador contratado depois da 3ª obra; orçamentista fixo em meio período'],
        ['Patamar 2 para o 3 (≈ R$ 100 mil)', 'Engenheiro de obras decide a parte técnica em 4 obras · custo de aquisição de cada gestão abaixo de R$ 3.000 · margem medida em 6 obras · fechamento mensal por produto até o 5º dia útil por 6 meses seguidos · júnior aprovado em vistorias e condomínios', 'Engenheiro de obras, 4 coordenadores, júnior, 2 administrativos'],
        ['Patamar 3 para o 4 (≈ R$ 200 mil)', '10 ou mais obras simultâneas com desvio de custo até 5% e de prazo até 10% · base recorrente (condomínios e empresas) acima de R$ 25 mil de lucro bruto · dívida renegociada e em amortização · rotatividade baixa da equipe', 'Cerca de 16 pessoas: 2 engenheiros, 8 coordenadores, júniores, orçamentista, administrativo e comercial'],
    ], 'sm', widths=['20%', '58%', '22%'])
    com = '<p class="small"><b>Composição dos patamares ' + tag('S') + ':</b> 2 = 5 obras em gestão, 2 reparos, 2 orçamentos, 1 viabilidade, 1 laudo, 1 visita e 5 condomínios com o Yan; 3 = 10 obras, 4 reparos, 3 orçamentos, 2 viabilidades, 2 laudos, 2 visitas, 8 vistorias com júnior e 12 condomínios; 4 = 22 obras, 6 reparos, 5 orçamentos, 3 viabilidades, 2 laudos, 4 visitas, 16 vistorias e 25 condomínios. Em todos, o Aruak fica abaixo de 120 h por mês.</p>'
    vol = box('O que os R$ 200 mil exigem', '<p>Na administração, o dinheiro da obra não entra na receita da Entre Colunas: a escala se mede em obras simultâneas e horas de coordenação, não em faturamento. Com obras de R$ 300 mil em 4 meses, o patamar 4 pede cerca de 22 obras ao mesmo tempo (perto de R$ 20 milhões por ano de obra administrada) ou o equivalente em obras maiores. É um destino de alguns anos; os patamares mostram a ordem das provas, não um calendário.</p>')
    div = []
    for p in ('P2', 'P3', 'P4'):
        cx = {'P2': P2, 'P3': P3, 'P4': P4}[p]['cx']; m = r2(650000 / (cx / 2)) if cx > 0 else None
        div.append(f'{p[1]}: {brl(cx / 2, False)} por mês, cerca de {int(round(m))} meses')
    divida = box('Dívida de R$ 650 mil', f'<p>No patamar 1, depois de remunerar o Aruak e de uma estrutura estimada de R$ 15 mil, sobram {brl(P1["cx"], False)} por mês: quase nada para a dívida. Por isso ela precisa de plano próprio já (credores, juros, prazos e renegociação), sem usar dinheiro de contrato em andamento. Se metade do caixa livre de cada patamar fosse para o principal, sem considerar juros: patamar {"; patamar ".join(div)}.</p>', 'warn')
    return page('Estrutura da empresa', 'Do lucro bruto de R$ 30 mil aos R$ 200 mil', 'Cada patamar separa receita, lucro bruto, remuneração do Aruak, saldo dos produtos e caixa livre. Avança-se quando as provas da tabela de baixo existirem.',
        tab + com + '<h2>Resultados intermediários que precisam ser comprovados</h2>' + provas + vol + divida)

def ivan_vicente():
    iv = table(['Ivan · papel proposto: abertura de oportunidades e canal ' + tag('P'), 'Prazo', 'Evidência'], [
        ['Lista de 10 escritórios de arquitetura e 10 síndicos no avatar, com contato e motivo da escolha', '06/11', 'Placar'],
        ['Conversa marcada com os 2 escritórios do teste de pré-obra', '13/11', 'Placar com data'],
        ['Pergunta fiscal ao contador: 8% por serviço, nota da gestão só sobre o honorário, compensação da Tip Toy (se mantiver a frente financeira combinada em 26/10)', '13/11', 'Resposta escrita'],
        ['1 estudo de pré-obra pago e 2 reuniões com síndicos originados por ele', '18/12', 'Placar e Mais Controle'],
        ['A partir de janeiro: reuniões qualificadas por mês, contratos pagos originados, custo de aquisição por contrato, 100% das oportunidades com origem e motivo de perda', 'Mensal', 'Placar'],
    ], 'sm', widths=['70%', '12%', '18%'])
    vi = table(['Vicente · papel proposto: controladoria e contratos ' + tag('P'), 'Prazo', 'Evidência'], [
        ['Cláusulas de contratação remota de visita, laudo e vistoria: pagamento antecipado, agendamento, arrependimento (CDC, art. 49) e cancelamento', '13/11', 'Minuta'],
        ['Contratos de gestão por honorário mensal com prorrogação, do condomínio sem fidelidade e da Tip Toy com comprovação mensal', '20/11', 'Minutas'],
        ['Outubro e novembro abertos por produto no Mais Controle: receita, custos diretos, lucro bruto, horas, saldo e caixa livre; conferência dos R$ 30 mil', '30/11', 'Mais Controle'],
        ['Mapa da dívida de R$ 650 mil (credor, saldo, juros, vencimento, garantia) e proposta de plano; projeção de caixa de 13 semanas', '18/12', 'Documento'],
        ['A partir de janeiro: fechamento até o 5º dia útil; previsto × realizado por contrato; pico de caixa simulado antes de assinar contrato novo', 'Mensal', 'Mais Controle'],
    ], 'sm', widths=['70%', '12%', '18%'])
    gov = box('Como a parceria se sustenta', '<p>Os 35% em negociação dependem de entregas e de acordo próprio; nada está aceito. Toda sexta, o quadro semanal registra: <b>quem trouxe cliente pagante, quem manteve a margem, quem assumiu rotina e quantas horas deixaram de depender do Aruak</b>. Esses números fundamentam a conversa depois de 18/12. Como o Vicente seria parte do acordo, o contrato de sociedade deve ter revisão jurídica independente. Decisão de sociedade é sempre do Aruak.</p>')
    precisa = ('<p><b>Sem essas entregas, a empresa não passa do patamar 1:</b> o canal (Ivan) é o que traz obras e condomínios sem consumir as horas do Aruak, e a controladoria (Vicente) é o que mostra margem e pico de caixa antes de assinar e o previsto contra o realizado depois. '
               'Alguém também precisa assumir a execução diária: coordenação de campo e suprimentos não estão com nenhum dos dois e continuam pendentes.</p>')
    return page('Estrutura da empresa', 'Ivan e Vicente: entregas para sustentar a parceria', 'Papéis propostos, não aceitos. Cada entrega tem prazo e evidência em um dos três sistemas.',
        iv + vi + precisa + gov)

def build():
    return comparativa() + cenario() + patamares() + ivan_vicente()
