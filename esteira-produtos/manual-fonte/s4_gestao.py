# -*- coding: utf-8 -*-
from common import *

SQ = '<span class="sq"></span>'

ETAPAS = [  # obra-exemplo simulada (R$ 300 mil, 4 meses): orçado, contratado, pago, medido a pagar, projeção
    ('Serviços preliminares, demolição e caçamba', 18000, 17200, 17200, 0, 17200),
    ('Infraestrutura hidráulica e elétrica', 42000, 43500, 22900, 3200, 43500),
    ('Alvenaria, estrutura e reboco', 38000, 37000, 25900, 0, 37000),
    ('Cobertura e impermeabilização', 45000, 46800, 18000, 5400, 46800),
    ('Revestimentos e pisos', 60000, 8405.65, 0, 0, 60000),
    ('Forro e pintura', 25000, 0, 0, 0, 25000),
    ('Esquadrias, louças, metais e marmoraria', 42000, 12600, 6300, 0, 42000),
    ('Limpeza e entrega', 5000, 0, 0, 0, 5000),
]
CONTING = 25000

MEDEIROS = [('ART', 407.10), ('Caçamba', 5664.00), ('Nivelamento', 15074.97), ('Demolição', 14254.40), ('Infraestrutura hidráulica', 14562.20),
            ('Poço de infiltração', 7736.08), ('Alvenarias e estrutura', 28173.21), ('Calçada', 3904.74), ('Impermeabilização', 5298.20),
            ('Cobertura', 42432.50), ('Infraestrutura elétrica', 21103.12), ('Forro', 3622.13), ('Revestimento', 42196.63),
            ('Marmoraria', 8516.18), ('Pintura', 19137.71), ('Esquadrias', 19821.64), ('Limpeza', 1416.00)]

def comercial():
    blocos = [
        ('O problema', '<p>Obra estoura prazo e orçamento quando ninguém coordena compras, equipes e decisões. O dono vira refém do empreiteiro, paga adiantado por serviço que não foi feito e só descobre o custo real no fim.</p>'),
        ('Para quem é', '<p>Reforma ou construção com projeto, ou com disposição de pagar o planejamento, verba definida e quem decide participando das reuniões.</p>'),
        ('Como trabalhamos', ul(['Planejamento antes da obra: estudo dos projetos, orçamento, cronograma e plano de compras, apresentados e aprovados por você.',
            'Compras e contratações em seu nome, com 2 ou 3 propostas em cada ordem de compra. Você escolhe e paga direto ao fornecedor.',
            'Mão de obra paga só depois da medição do que foi executado.',
            'Relatório toda semana, com fotos, medições e decisões pendentes; fechamento financeiro todo mês: previsto, contratado, pago e custo para terminar.',
            'Coordenador de campo em visitas programadas e engenheiro responsável pelas decisões técnicas, com ART.'])),
        ('O que não fazemos', ul(['Não recebemos o dinheiro da obra nem compramos com dinheiro nosso.', 'Não fazemos empreitada com preço fechado de obra.',
            'Não alteramos o projeto sem o arquiteto.', 'Não começamos sem planejamento aprovado.'])),
        ('O que você decide', '<p>Cada compra, cada contratação e qualquer mudança de escopo, sempre com o impacto em custo e prazo antes.</p>'),
        ('Prazo e prorrogação', '<p>O cronograma é aprovado no planejamento. Atraso causado por nós não gera cobrança. Mudança pedida por você ou causa externa documentada geram mês de prorrogação com valor reduzido, previsto no contrato.</p>'),
    ]
    preco = ('<table><tr><td>Honorário</td><td class="v">mensal e fixo</td></tr><tr><td>Pagamento</td><td class="v">no início de cada mês</td></tr></table>'
             '<p>Definido pela equipe e pela frequência de campo que a sua obra exige, com o equivalente em percentual do orçamento para você comparar. O planejamento é pago antes: estudo de viabilidade, orçamento executivo ou o primeiro mês.</p>')
    prox = '<p>Reunião presencial com quem decide. Traga o projeto e a faixa de investimento. Você sai da reunião com a data da proposta.</p>'
    return client_page('Frente 4 · página comercial', 'Gestão de Obra',
        'Sua obra coordenada por engenheiro, com compras que você aprova, pagamento só do que foi medido e prestação de contas toda semana. O dinheiro da obra fica com você.',
        blocos, preco, prox)

def ficha():
    resp = table(['Papel', 'Pessoa'], [
        ['Venda e proposta', 'Aruak; Ivan na abertura de oportunidades, se aceitar'],
        ['Planejamento: orçamento, cronograma, plano de compras', 'Aruak, com apoio técnico <span class="tg">[a designar]</span>'],
        ['Coordenação de campo', 'Yan ' + tag('P') + ' se confirmar 32 h por mês por obra e atribuição; senão, técnico contratado antes da venda'],
        ['Cotações e ordens de compra', 'Coordenador prepara; cliente aprova'], ['Medições', 'Coordenador mede; Aruak valida acima de R$ 5.000'],
        ['Relatório semanal', 'Coordenador escreve; Gabriela envia na sexta'],
        ['Fechamento financeiro mensal', 'Gabriela, com a controladoria (Vicente, se aceitar), até o 5º dia útil'],
        ['Decisões técnicas, ART e diálogo com o arquiteto', 'Aruak'], ['Honorários, NF e cobrança', 'Gabriela; Flávia nos pagamentos'],
    ], 'sm', widths=['42%', '58%'])
    horas = table(['Por obra e por mês ' + tag('E'), 'Horas'], [
        ['<b>Aruak</b>: 4 visitas técnicas de 2,5 h', '10 h'], ['Aruak: decisões e reunião quinzenal com o cliente', '4 h'],
        ['Aruak: revisão do relatório e do fechamento', '3 h'], ['Aruak: arquiteto e Diagnóstico e Soluções', '3 h'],
        ['<b>Coordenador</b>: 8 visitas de 3 h com trajeto', '24 h'], ['Coordenador: ordens de compra e cotações', '4 h'], ['Coordenador: medições e diário de obra', '4 h'],
        ['<b>Administrativo</b>: relatório, fechamento, NF, documentos', '6 h'],
        ['<b>Venda</b>: 8 h por proposta ÷ 30% de conversão', '26,67 h por contrato'],
    ], 'sm', widths=['76%', '24%'])
    seq = ol(['Qualificação com as seis perguntas e nota de entrada de 9 ou mais, sem eliminatório.', 'Reunião presencial com quem decide.',
              'Planejamento pago: Pré-obra ou o primeiro mês antecipado.', 'Contrato e primeiro honorário.',
              'Apresentação do planejamento e termo de recebimento do planejamento.', 'Mobilização: placas, carta aos vizinhos, quadro de gestão à vista, mapa de fotos.',
              'Rotina semanal: visitas, ordens de compra, medições, relatório de sexta.', 'Fechamento financeiro até o 5º dia útil de cada mês.',
              'Entrega: vistoria com o cliente, termo de recebimento com ressalvas, manual do proprietário.', 'Pós-obra de 90 dias.'])
    campo = box('Quem conduz o campo quando o Aruak está vendendo ' + tag('P'), ''.join([
        '<p><b>Agenda fixa.</b> Coordenador na obra às terças e quintas de manhã e na sexta para medir. Aruak em uma visita técnica semanal em dia fixo e na reunião quinzenal com o cliente. Os dias de venda do Aruak ficam protegidos na agenda.</p>',
        '<p><b>O coordenador decide sozinho:</b> compra pelo cartão pré-pago do cliente até R$ 500; mudança de sequência sem custo; liberação de medição até R$ 5.000 conforme a planilha aprovada; parar qualquer serviço por segurança.</p>',
        '<p><b>Precisa do Aruak:</b> medição acima de R$ 5.000; estrutura, impermeabilização, instalações elétricas e de gás, demolição de parede; qualquer mudança de escopo, preço ou prazo. <b>Precisa do cliente:</b> toda ordem de compra e todo aditivo.</p>',
        '<p><b>Escalonamento.</b> Dúvida técnica vai ao Aruak por WhatsApp com foto, local, pergunta e prazo; resposta em até 4 horas úteis. Risco: parar o serviço e ligar.</p>',
        '<p><b>O coordenador nunca</b> faz o papel de mestre, promete data fora do cronograma, paga com dinheiro da empresa ou dá parecer estrutural. Ausência dele: o Aruak cobre ou a visita é remarcada em até 48 horas, registrada no Painel de Obras.</p>',
        '<p><b>Capacidade.</b> Sem coordenador nomeado e horas reservadas no Painel de Obras, não se vende nova gestão. Um coordenador em tempo integral sustenta até 3 obras simultâneas ' + tag('E') + '.</p>']))
    p1 = page('Frente 4 · ficha interna', 'Gestão de Obra · ficha interna', 'O proprietário contrata a coordenação da rotina, das compras, das medições e das decisões sobre custo e prazo.',
        '<div class="two"><div><h2>Responsáveis</h2>' + resp + '</div><div><h2>Horas por pessoa</h2>' + horas + '</div></div>' + campo + '<h2>Sequência de execução</h2>' + seq)
    riscos = table(['Risco', 'Tratamento'], [
        ['Meses de prorrogação sem honorário', 'Regra de extensão por causa documentada no relatório semanal'],
        ['Coordenador sem horas', 'Não vender sem nome e agenda no Painel de Obras'],
        ['Cliente atrasa decisões ou pagamentos', 'Relatório com data-limite e impacto de cada decisão'],
        ['Empreiteiro sem capacidade', 'Empreiteiros-núcleo e pagamento só por medição'],
        ['Aruak volta a ser mestre de obras', 'Alçadas escritas e agenda fixa'],
        ['Pagamento adiantado ao empreiteiro', 'Proibido: só o medido é pago'],
        ['Projeto incompleto ou incompatível', 'Diagnóstico e Soluções por escrito ao arquiteto; hora técnica'],
        ['Obra com financiamento bancário', 'Simular o caixa medição a medição antes de aceitar'],
    ], 'sm', widths=['42%', '58%'])
    ind = ind_table([('Obra de R$ 300 mil em 4 meses, honorário de R$ 12.350 ' + tag('S'), G_RES['B'][0], '0'),
                     ('Mesma obra, 6 meses por alteração do cliente', G_RES['B'][2], '0'),
                     ('Mesma obra, 6 meses por atraso nosso', G_RES['B'][1], '0'),
                     ('Um mês de obra (venda rateada em 4 meses)', G_MES_A, '0')])
    cx_mes = r2(G_MENSAL - G_COORD_H * TEC - G_ADM_H * ADM - G_IDAS * IDA - G_MENSAL * T)
    crit = table(['Na primeira obra, medido mês a mês', 'Decisão'], [
        ['Aruak até 22 h por mês, coordenador até 36 h, honorário recebido até o dia 5 e nenhum dinheiro do cliente no caixa da empresa', '<b>Manter</b> o modelo e abrir a segunda obra com o mesmo coordenador'],
        ['Horas 20% acima do previsto ou honorário atrasado', '<b>Ajustar</b> carga, frequência de campo ou valor na próxima proposta'],
        ['Coordenador não sustenta a rotina, ou 2 meses de prorrogação sem pagamento', '<b>Suspender</b> novas vendas de gestão até resolver a equipe'],
    ], 'sm', widths=['64%', '36%'])
    filtro = box('Filtro de entrada revisto ' + tag('P'), f'<p>O filtro antigo de R$ 60 mil e mais de uma semana deixa entrar obra pequena demais para o custo do coordenador. Proposta: obra com custo direto a partir de cerca de R$ 150 mil, ou cliente que aceite o honorário mínimo de {brl(G_PISO)} por mês. Obra menor vai para Acompanhamento por visitas ou Reparo Rápido.</p>')
    p2 = page('Frente 4 · ficha interna', 'Gestão de Obra · aceite, riscos e dinheiro', 'O dinheiro da obra não passa pela Entre Colunas. O honorário é recebido antes de a equipe trabalhar o mês.',
        '<h2>Aceite</h2><p>Termo de recebimento do planejamento assinado antes da obra; medições assinadas; relatório enviado toda sexta; fechamento mensal aprovado pelo cliente; termo de recebimento da obra com ressalvas e manual do proprietário (ABNT NBR 14037); pós-obra de 90 dias.</p>'
        '<div class="two"><div><h2>Riscos</h2>' + riscos + '</div><div><h2>Pagamento, aquisição e caixa</h2>'
        '<p>Honorário mensal antecipado até o dia 5; o primeiro na assinatura paga o planejamento; prorrogação conforme a regra; NF mensal. Fornecedores e mão de obra são pagos pelo cliente, direto.</p>'
        '<p>Aquisição: arquitetos sem reserva técnica, Pré-obra, clientes antigos e Scanner (código GESTÃO). Custo: cerca de 26,67 h do Aruak por contrato ganho ' + tag('E') + '.</p>'
        f'<p>Caixa livre do contrato num mês típico: {brl(G_MENSAL)} recebidos menos coordenador, administrativo, idas e tributos = <b>{brl(cx_mes)}</b>, antes de remunerar o Aruak. ART de {brl(ART2, True)} no primeiro mês. Pico negativo: R$ 0.</p></div></div>'
        '<h2>Margem</h2>' + ind + '<h2>Critério para manter, ajustar ou suspender</h2>' + crit + filtro)
    return p1 + p2

def medeiros():
    tot = r2(sum(v for _, v in MEDEIROS))
    half = (len(MEDEIROS) + 1) // 2
    t1 = table(['Etapa (cronograma Resolve)', 'Valor'], [[a, brl(b, True)] for a, b in MEDEIROS[:half]], 'sm num', widths=['64%', '36%'])
    t2 = table(['Etapa (cronograma Resolve)', 'Valor'], [[a, brl(b, True)] for a, b in MEDEIROS[half:]], 'sm num', widths=['64%', '36%'],
               foot=['Soma das etapas', brl(tot, True)])
    sabe = box('O que se sabe ' + tag('A'), '<p>Obra da Família Medeiros, pela Resolve, em 2022: orçamento 000041 de 17/05/2022, obra 22.003, <b>R$ 253.320,82</b>, cronograma físico-financeiro quinzenal de junho de 2022 a fevereiro de 2023 (9 meses planejados). Foi o uso anterior do método de administração do BORA pelo Aruak.</p>')
    falta = table(['Dado a reconstruir', 'Onde procurar', 'O que muda'], [
        ['Honorários efetivamente recebidos', 'Contrato da Resolve, extratos de 2022 e 2023, notas fiscais', 'Se o método pagou a equipe'],
        ['Duração real', 'Cronograma, conversas da obra, termo de entrega', 'Peso da prorrogação'],
        ['Horas do Aruak', 'Agenda, conversas, deslocamentos', 'Disponível por hora real'],
        ['Quem sustentava o campo', 'Memória do Aruak e da equipe da época', 'Quem pode ser o coordenador agora'],
    ], 'sm', widths=['30%', '40%', '30%'])
    ensina = box('O que o caso já ensina, antes da reconstrução ' + tag('S'),
        f'<p>Se a Medeiros fosse cobrada hoje com fixo de R$ 5.000 por 9 meses e taxa média de 9,8%, o cliente pagaria {brl(MED_A, True)}, ou {pct(MED_A / MED_OBRA)} da obra: caro demais. Com um honorário dimensionado para uma carga mensal menor (Aruak 10 h, coordenador 24 h, 6 h administrativas, 9 idas), o mínimo para a meta seria {brl(MED_LEVE, True)} por mês, ou {brl(MED_LEVE_TOT, True)} em 9 meses ({pct(MED_LEVE_TOT / MED_OBRA)} da obra).</p>'
        '<p><b>Lição:</b> a duração pesa mais que o valor da obra. Obra longa pede carga mensal menor e honorário dimensionado pela equipe, não o fixo de uma obra de 4 meses.</p>')
    ex = table(['Obra-exemplo usada nos modelos ' + tag('S'), 'Orçado'], [[e[0], brl(e[1])] for e in ETAPAS] + [['Contingência do cliente (10%)', brl(CONTING)]], 'sm num',
               widths=['70%', '30%'], foot=['Custo direto pago pelo cliente', brl(sum(e[1] for e in ETAPAS) + CONTING)])
    return page('Frente 4 · caso Medeiros', 'Família Medeiros e a obra-exemplo', 'O caso real mostra a estrutura de uma obra administrada; a obra-exemplo simulada mostra como preencher os modelos.',
        sabe + '<div class="two"><div>' + t1 + '</div><div>' + t2 + '</div></div>' + '<p class="small">A soma das etapas dá R$ 253.320,81; o orçamento registra R$ 253.320,82. A diferença de R$ 0,01 é arredondamento do documento original.</p>' + '<h2>Os quatro dados que faltam</h2>' + falta + ensina +
        '<div class="two"><div>' + ex + '</div><div><p class="small" style="margin-top:2mm">Casa térrea em reforma geral, R$ 300 mil de custo direto, 4 meses (16 semanas), com etapas agrupadas no padrão da Medeiros. Os modelos das próximas páginas mostram o mês 2 dessa obra.</p></div></div>')

def oc_medicao():
    props = [('A · Loja A', 89.90, '10 dias', 'Boleto em 30 dias', 'Lote único garantido'),
             ('B · Loja B', 94.50, '5 dias', 'PIX à vista', '—'),
             ('C · Loja C', 86.00, '20 dias', 'PIX à vista', 'Entrega depois da data de necessidade')]
    q = 93.5
    oc = table(['Proposta', 'Preço por m²', 'Total (93,5 m²)', 'Entrega', 'Pagamento', 'Observação'],
               [[a, brl(b, True), brl(r2(b * q), True), c, d, e] for a, b, c, d, e in props], 'sm', widths=['14%', '13%', '15%', '11%', '17%', '30%'])
    cab = table(['Ordem de Compra nº 007 ' + tag('S'), ''], [
        ['Obra e etapa', 'Obra-exemplo · Revestimentos e pisos'], ['Item', 'Porcelanato 90×90 retificado acetinado, piso social: 85 m² + 10% de perdas = 93,5 m²'],
        ['Necessário na obra até', '15/12 (semana 9)'], ['Preparada por', 'Coordenador de campo, 03/12'],
    ], 'sm', widths=['30%', '70%'])
    dec = (f'<p><b>Recomendação:</b> proposta A. É a mais barata entre as que chegam a tempo e garante lote único. A C custa {brl(r2((89.90 - 86.00) * q), True)} menos, mas entrega depois da data de necessidade e atrasaria o piso em cerca de uma semana. A B custa {brl(r2((94.50 - 89.90) * q), True)} mais.</p>'
           '<p><b>Decisão do cliente:</b> “Aprovo a proposta A” · data · assinatura ou mensagem de WhatsApp. <b>Pagamento:</b> direto do cliente ao fornecedor, com nota fiscal em nome do cliente. <b>Recebimento:</b> coordenador confere quantidade, lote, tonalidade e quebras.</p>'
           '<p class="small">No honorário mensal não há taxa por ordem de compra. Se o contrato for de fixo mais taxa, a ordem informa a taxa da etapa: pisos, 10% = ' + brl(r2(0.10 * 89.90 * q), True) + '.</p>')
    itens = [('Alvenaria de vedação', 'm²', 120, 45, 1.00, 1.00), ('Chapisco e reboco', 'm²', 380, 32, 0.40, 0.75), ('Contrapiso', 'm²', 150, 28, 0.0, 0.50),
             ('Assentamento de revestimento de parede', 'm²', 110, 55, 0, 0), ('Assentamento de piso', 'm²', 150, 60, 0, 0), ('Rodapé', 'm', 119, 10, 0, 0)]
    rows = []; tot = acum = lib = 0
    for s, u, qq, p, a0, a1 in itens:
        v = qq * p; va = r2(v * a1); vl = r2(v * (a1 - a0)); tot += v; acum += va; lib += vl
        rows.append([s, u, n(qq, 0), brl(p), brl(v), pct(a0, 0), pct(a1, 0), brl(va), brl(vl)])
    med = table(['Serviço', 'Un.', 'Qtd.', 'Preço un.', 'Total', 'Acum. anterior', 'Acum. atual', 'Valor acumulado', 'Liberar agora'], rows, 'sm num',
                widths=['27%', '5%', '7%', '9%', '10%', '10%', '9%', '11%', '12%'],
                foot=['Total do contrato de mão de obra', '', '', '', brl(tot), '', pct(acum / tot), brl(acum), brl(lib)])
    medc = (f'<p class="small">Medição nº 03 ' + tag('S') + f' · empreiteiro-núcleo de alvenaria e revestimento · semana 6. Pago antes: {brl(acum - lib)}. A liberar: <b>{brl(lib)}</b>, acima de R$ 5.000: validação do Aruak. '
            'Checklist de aceite: prumo e nível com régua de 2 m, esquadro, espessura do reboco, limpeza, fotos 12 a 18. Reprovado e refeito antes da medição: reboco do banheiro 2. '
            'Assinaturas: coordenador (mediu), Aruak (validou), empreiteiro (ciente), cliente (autoriza o pagamento direto).</p>')
    return page('Frente 4 · modelos', 'Ordem de compra e medição', 'Toda compra passa por ordem com propostas comparadas e aprovação do cliente. Só o que foi medido é pago.',
        '<h2>Ordem de compra</h2>' + cab + oc + dec + '<h2>Medição</h2>' + med + medc)

def relatorio_fechamento():
    rel = table(['Relatório semanal · semana 6 de 16 · 30/11 a 04/12 ' + tag('S'), ''], [
        ['Situação', '<span class="pill p-t">Atenção</span> Cobertura com 2 dias de atraso por chuva; cronograma geral mantido'],
        ['Feito na semana', 'Reboco interno em 75%; contrapiso em 50%; infraestrutura elétrica em 60%; telhas da área gourmet trocadas (aditivo 01)'],
        ['Medições liberadas', 'Medição 03, alvenaria e revestimento: R$ 6.356 · Medição 02, elétrica: R$ 3.200, a pagar até 07/12'],
        ['Compras', 'OC-007 porcelanato: aprovar até 04/12 · OC-008 metais: em cotação'],
        ['Decisões pendentes do cliente', 'Metais até 09/12 (sem isso, louças e metais atrasam 1 semana) · OC-007 até 04/12 (sem isso, o piso da sala começa na semana 10)'],
        ['Próximos 7 dias', 'Concluir reboco; iniciar revestimento dos banheiros; passar cabos'],
        ['Riscos e problemas', 'Previsão de chuva por 3 dias · Diagnóstico e Soluções 02 enviado ao arquiteto (viga interfere no forro da cozinha), resposta até 08/12'],
        ['Dinheiro do cliente', 'Pago até agora: R$ 90.300 · Medido a pagar: R$ 8.600 · Previsão das próximas 2 semanas: R$ 21.000'],
        ['Visitas', 'Coordenador em 01/12 e 03/12 · Aruak em 30/11 · reunião com o cliente em 04/12'],
        ['Fotos', 'Mapa de fotos com os mesmos ângulos do projeto, fotos 1 a 24'],
    ], 'sm', widths=['22%', '78%'])
    rows = []; TT = [0] * 6
    for nome, orc, con, pag, apag, proj in ETAPAS:
        term = r2(proj - pag - apag); dev = r2(proj - orc)
        rows.append([nome, brl(orc), brl(con), brl(pag), brl(apag), brl(term), brl(proj), brl(dev)])
        for i, v in enumerate((orc, con, pag, apag, term, proj)): TT[i] += v
    fech = table(['Etapa', 'Orçado', 'Contratado', 'Pago pelo cliente', 'Medido a pagar', 'Custo para terminar', 'Projeção', 'Desvio'], rows, 'sm num',
                 widths=['26%', '9%', '11%', '10%', '9%', '11%', '11%', '9%'],
                 foot=['Total sem contingência', brl(TT[0]), brl(TT[1]), brl(TT[2]), brl(TT[3]), brl(TT[4]), brl(TT[5]), brl(TT[5] - TT[0])])
    cont = f'<p class="small">Contingência do cliente: {brl(CONTING)} orçados; desvio líquido de {brl(TT[5] - TT[0])} até aqui (hidráulica +R$ 1.500, cobertura +R$ 1.800 do aditivo 01 aprovado, preliminares −R$ 800, alvenaria −R$ 1.000); saldo de contingência {brl(CONTING - (TT[5] - TT[0]))}. Projeção final: {brl(TT[5])} + contingência não usada = {brl(TT[5] + CONTING - (TT[5] - TT[0]))}.</p>'
    hon = table(['Honorários da Entre Colunas', 'Valor'], [
        ['Previstos (4 × R$ 12.350)', brl(G_TOTAL_A)], ['Faturados e recebidos até o mês 2', brl(2 * G_MENSAL)], ['A receber (meses 3 e 4)', brl(2 * G_MENSAL)], ['Prorrogação', 'nenhuma até aqui'],
    ], 'sm num', widths=['70%', '30%'])
    cx_mes = r2(G_MENSAL - G_MES_CUSTO - r2(G_MENSAL * T))
    emp = table(['Visão do controlador (mês 2)', 'Valor'], [
        ['Recebido', brl(G_MENSAL)], ['(−) Coordenador, administrativo e idas', brl(-G_MES_CUSTO)], ['(−) Tributos', brl(-r2(G_MENSAL * 0.08))],
        {'cls': 'tot', 'cells': ['Caixa livre do mês, antes do Aruak', brl(cx_mes)]}, ['(−) 20 h do Aruak a R$ 100', brl(-2000)],
        {'cls': 'tot', 'cells': ['Saldo do mês', brl(cx_mes - 2000)]},
    ], 'sm num', widths=['70%', '30%'])
    return page('Frente 4 · modelos', 'Relatório semanal e fechamento financeiro', 'O cliente recebe o relatório toda sexta e o fechamento até o 5º dia útil do mês seguinte.',
        rel + '<h2>Fechamento financeiro · mês 2 de 4 ' + tag('S') + '</h2>' + fech + cont + '<div class="two"><div>' + hon + '</div><div>' + emp + '</div></div>')


def honorarios():
    rows = []
    for k in ('A', 'B', 'C'):
        nome = G_CASOS[k][0]
        res = G_RES[k]
        rows.append([f'<b>{k}.</b> {nome}'] + [f'{brl(e.receita)}<br><span class="small">{brl(e.ph)}/h · saldo {brl(e.saldo)}</span>' for e in res])
    t = table(['Modelo, mesma obra de R$ 300 mil'] + G_COLS, rows, 'sm', widths=['28%', '18%', '18%', '18%', '18%'])
    pc = [f'{pct(G_RES[k][0].receita / G_OBRA, 2)}' for k in 'ABC']
    notas = ul([f'Nos 4 meses do cronograma, os três modelos custam o mesmo ao cliente ({brl(G_TOTAL_A)}, {pc[0]} do custo da obra). O fixo do modelo do BORA (R$ 6.067 por mês) levaria a {brl(G_TOTAL_BORA)}, ou {pct(G_TOTAL_BORA / G_OBRA, 2)}.',
                'A diferença aparece quando a obra passa do prazo. Equipe considerada: Aruak 20 h, coordenador 32 h, 6 h administrativas e 12 idas por mês; ART de R$ 285,59; venda de 26,67 h do Aruak.',
                'No modelo A, pela regra do BORA, o fixo vale só para os meses do cronograma: atraso nosso e causa externa ficam com a Entre Colunas; alteração do cliente gera novo cronograma.',
                'No modelo C, o percentual não muda com o prazo: a prorrogação nunca é paga, qualquer que seja a causa.'])
    rec = box('Recomendação: honorário mensal por equipe e escopo (modelo B) ' + tag('P'), ''.join([
        '<p><b>Por quê.</b> 1) Cobre o maior risco, a prorrogação: com alteração do cliente, B rende ' + brl(G_RES['B'][2].ph) + '/h, contra ' + brl(G_RES['A'][2].ph) + '/h em A e ' + brl(G_RES['C'][2].ph) + '/h em C. 2) O controlador confere um valor, uma data e uma nota por mês. 3) O honorário não cresce com o valor das compras: não há conflito na escolha das propostas. 4) Recebido antes do mês, mantém o caixa positivo desde o primeiro dia. 5) O cliente vê o equivalente em percentual e compara com o mercado (catálogo atual de 15%; exemplo real do BORA, 14,2%).</p>',
        f'<p><b>Como precificar.</b> Honorário mensal maior ou igual ao piso: (horas do Aruak × R$ 200 + equipe + idas + ART rateada) ÷ 0,92. Com a carga desta obra, o piso é {brl(G_PISO, True)} por mês. A proposta de {brl(G_MENSAL)} inclui planejamento, venda e margem. O valor de prorrogação ({brl(G_PRORROG)}, 60% do mensal) fica perto do piso: mantém a equipe sem lucrar com o atraso.</p>',
        '<p><b>Regras para o contrato (Vicente).</b> Duração e frequência de campo escritas; causa de cada dia de atraso registrada no relatório semanal; atraso da Entre Colunas sem cobrança; alteração do cliente com novo cronograma e prorrogação; causa externa documentada com prorrogação; pagamento até o dia 5; encerramento com aviso.</p>',
        '<p><b>Quando usar o fixo mais taxa do BORA.</b> Depois de duas obras medidas e com a controladoria acompanhando a taxa por ordem de compra, em obras com muita variação de escopo. O percentual puro (C) não é recomendado.</p>']))
    return page('Frente 4 · honorários', 'Três formas de cobrar a mesma obra', 'Obra de R$ 300 mil em 4 meses, com dois meses de prorrogação por três causas diferentes. Em cada célula: quanto o cliente paga, o disponível por hora do Aruak e o saldo parcial.',
        t + notas + rec)

def build():
    return comercial() + ficha() + medeiros() + oc_medicao() + relatorio_fechamento() + honorarios()
