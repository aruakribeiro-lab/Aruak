# -*- coding: utf-8 -*-
"""Gera o documento do produto Plano para Terminar a Obra (mesmo estilo do manual)."""
from common import *
from plano_calc import *

SQ = '<span class="sq"></span>'
SEC = 'Produto novo · Plano para Terminar a Obra'


def capa():
    return f'''<section class="cover" style="height:auto">
<div class="band"><div class="brand">ENTRE COLUNAS · ENGENHARIA DE PREVISIBILIDADE</div>
<h1>Plano para Terminar a Obra</h1>
<p class="lead">O produto pago de entrada para quem está construindo ou reformando e chega pelo Raio-X da Obra em Andamento. Dois níveis: a Conferência da Medição, para decidir a próxima parcela, e o Plano para Terminar, para saber quanto falta, em que ordem e se o dinheiro chega até a mudança.</p>
<p class="lead" style="margin-top:6mm;font-size:9.5pt">Versão 1.0 · 02/11/2026 · Goiânia · circulação interna · complementa o Manual operacional das seis frentes</p></div>
<div class="meta">
<h2>Onde fica na esteira</h2>
{table(['Degrau', 'O que o cliente compra', 'Preço', 'Saída natural'], [
        ['Raio-X da Obra em Andamento (Scanner)', 'Os quatro indicadores e a classificação da obra, na hora', 'Grátis', 'Código SCN-OBRA no WhatsApp'],
        ['<b>Conferência da Medição</b>', 'Saber se a próxima parcela corresponde ao que foi executado', brl(CM_PRECO), 'Plano para Terminar, com abatimento'],
        ['<b>Plano para Terminar</b>', 'Saldo de serviços, orçamento para terminar, sequência até a mudança e plano de caixa', f'{brl(PT_PRECO)} ou {brl(5500)}; {brl(3900)} depois da Conferência', 'A equipe atual termina com o plano, ou a Gestão da conclusão'],
        ['Gestão de Obra (frente 4)', 'Coordenação da conclusão por honorário mensal', 'Mensal e fixo', 'Fechamento e indicação'],
    ], 'sm', widths=['26%', '38%', '18%', '18%'])}
<div class="two">
<div><h2>Por que este é o próximo produto</h2>
<p>O Raio-X já está publicado e manda para cá quem está com a obra andando e com medo de o dinheiro acabar. Hoje a esteira só oferece a essa pessoa a Gestão de Obra, que é uma venda longa e de valor alto, ou a Pré-obra, que só serve antes de começar. <b>Obra em andamento não tinha porta de entrada paga.</b></p>
<p>Os dois níveis usam o que a Entre Colunas já faz: vistoria com ART, orçamento por etapa com cotação e fechamento financeiro do método de gestão. Não exigem sistema novo nem contratação.</p></div>
<div><h2>O que este documento decide</h2>
<p>Preços, entregas, horas, margem, roteiro de venda, mensagens, checklist de campo e critérios de teste até 18/12. Tudo o que é proposta está marcado {tag('P')} e vale como regra de trabalho até o Aruak confirmar ou mudar. As perguntas que dependem dele estão na última página.</p>
<p class="small">Premissas do manual: tributos de 8%, hora do Aruak a R$ 100 e meta de R$ 200 disponíveis por hora, técnico a R$ 60/h, administrativo a R$ 35/h, R$ 50 por ida, ART de R$ 108,39 até R$ 15 mil, custo de aquisição pelo Scanner de R$ 35 por venda.</p></div>
</div>
<p class="small">{RT} · {CONTATO}</p>
</div></section>'''


def comercial():
    blocos = [
        ('O problema', '<p>A obra anda, o dinheiro sai e ninguém consegue dizer quanto falta. A equipe pede a próxima parcela, a data de entrega muda e você decide no escuro, sem saber se o que pagou corresponde ao que foi feito.</p>'),
        ('Conferência da Medição', '<p>Para quando a próxima parcela está chegando. O engenheiro lê o contrato, o orçamento e a última medição, confere na obra serviço por serviço e entrega uma nota com o que confere, o que diverge e o que pedir à equipe antes de pagar. Visita em até 3 dias úteis e nota em até 2 dias úteis depois da visita.</p>'),
        ('Plano para Terminar', '<p>Para quando você precisa saber quanto falta. Você recebe o estado de cada etapa com fotos, a conferência do pago com o executado, a lista do que falta com quantidades, o orçamento para terminar com o preço da sua equipe e cotações, as datas até a mudança e os pagamentos mês a mês diante do dinheiro que você tem. Prazo: 10 dias úteis.</p>'),
        ('Com a sua equipe', '<p>O plano é feito para a equipe atual terminar, com metas por escrito e pagamento pelo que foi medido. Não é auditoria nem acusação: os achados vão para você, com evidência, e você decide como conversar. Se quiser, apresentamos o plano junto com a equipe.</p>'),
        ('O que não está incluído', '<p>Gestão ou fiscalização da execução, projeto, laudo de defeitos ou perícia e negociação com a equipe em seu nome. Se aparecer um problema estrutural, avisamos no mesmo dia e indicamos o caminho.</p>'),
        ('O plano é seu', '<p>Você pode terminar com a sua equipe, com outra ou com a gente. Se quiser que a Entre Colunas assuma a gestão da conclusão, a proposta vem junto, para você decidir com os números na mesa.</p>'),
    ]
    preco = (f'<table><tr><td>Conferência da Medição</td><td class="v">{brl(CM_PRECO)}</td></tr>'
             f'<tr><td>Plano para Terminar, com contrato, orçamento e comprovantes</td><td class="v">{brl(PT_PRECO)}</td></tr>'
             f'<tr><td>Plano para Terminar, obra sem documentos organizados ou recebida já iniciada</td><td class="v">{brl(5500)}</td></tr>'
             f'<tr><td>Plano contratado até 30 dias depois da Conferência</td><td class="v">{brl(3900)}</td></tr></table>'
             '<p>Obras de até R$ 600 mil de valor total; acima, sob cotação. Conferência paga antes do agendamento. Plano: 50% na contratação e 50% na apresentação.</p>')
    prox = '<p>Conversa de 20 minutos por vídeo ou telefone, a partir do Raio-X. Tenha à mão o contrato, a última medição e o próximo pagamento pedido. Você sai sabendo qual entrega faz sentido e quando fica pronta.</p>'
    return client_page('Produto novo · página comercial', 'Plano para Terminar a Obra',
        'Antes do próximo pagamento, saiba o que já foi entregue, quanto custa terminar e se o seu dinheiro chega até a mudança.',
        blocos, preco, prox, 'Vistoria com ART. A nota e o plano registram o que foi observado na data da visita.')


def ficha():
    of = table(['', 'Conferência da Medição', 'Plano para Terminar'], [
        ['Quando cabe', 'Parcela pedida com vencimento em 4 dias úteis ou mais; dúvida concreta sobre uma medição; obra andando',
         'Raio-X em Replanejamento prioritário ou Dados insuficientes; falta dinheiro no custo máximo; obra lenta, parada ou em troca de equipe'],
        ['Pergunta respondida', '“Posso pagar essa parcela?”', '“Quanto falta, em que ordem, até quando e o dinheiro chega?”'],
        ['Entrega', 'Nota serviço a serviço (medido, observado, situação, o que pedir à equipe) e devolutiva de 30 minutos',
         'Registro da situação, conciliação, saldo de serviços, orçamento para terminar (mínimo e máximo), sequência e cronograma até a mudança, plano de caixa, regra de medição para a equipe, apresentação'],
        ['Preço e prazo', f'{brl(CM_PRECO)} · visita em até 3 dias úteis, nota em até 2', f'{brl(PT_PRECO)} com documentos, {brl(5500)} sem · 10 dias úteis · {brl(3900)} depois da Conferência'],
        ['Pular para', 'Parcela em menos de 4 dias úteis: orientar a pagar só o que está medido e comprovado, ou combinar nova data, e conferir a parcela seguinte',
         'Trinca aumentando: Visita Diagnóstica antes. Processo judicial: laudo ou assistência técnica. Quer alguém conduzindo: Gestão, com o Plano como vistoria de entrada'],
    ], 'sm', widths=['15%', '40%', '45%'])
    resp = table(['Papel', 'Pessoa'], [
        ['Triagem do SCN-OBRA, agenda e lista de documentos', 'Gabriela'],
        ['Conversa de 20 minutos, visita, conciliação, revisão e apresentação', 'Aruak'],
        ['Quantitativos e cotações', 'Apoio técnico a R$ 60/h, o mesmo da Pré-obra <span class="tg">[pendente de decisão]</span>'],
        ['Proposta, cobrança, termo e nota fiscal', 'Gabriela'],
        ['Registro', 'Placar (venda), Painel de Obras (horas), Mais Controle (recebimentos)'],
    ], 'sm', widths=['52%', '48%'])
    h_cm = table(['Conferência da Medição ' + tag('E'), 'Aruak', 'Equipe'],
        [[a, hh(b) if b else '—', c or '—'] for a, b, c in CM_HORAS] + [{'cls': 'tot', 'cells': ['Total', hh(CM_H), '1 h adm']}], 'sm', widths=['62%', '13%', '25%'])
    h_pt = table(['Plano para Terminar, com apoio ' + tag('E'), 'Aruak', 'Técnico', 'Adm'],
        [[a, hh(b) if b else '—', hh(c) if c else '—', hh(d) if d else '—'] for a, b, c, d in PT_HORAS] +
        [{'cls': 'tot', 'cells': ['Total', hh(PT_A), hh(PT_T), hh(PT_ADM)]}], 'sm', widths=['58%', '14%', '14%', '14%'])
    seq = ol(['O SCN-OBRA chega pelo WhatsApp. A Gabriela responde com a mensagem do nível do Raio-X e agenda a conversa.',
              'Conversa de 20 minutos (roteiro adiante). Escolha da oferta pela tabela de decisão e proposta de uma página no mesmo dia.',
              'Pagamento (Conferência integral; Plano 50%) e envio da lista de documentos.',
              'Leitura dos documentos antes da visita. O que faltar vira premissa escrita.',
              'Visita com o checklist de campo e fotos datadas por etapa. No Plano, o técnico vai junto.',
              'Técnico: saldo de serviços, quantitativos e cotações. Pedido por escrito à equipe atual do preço para terminar, por etapa.',
              'Aruak: conciliação, revisão técnica, sequência, cronograma, plano de caixa e regra de medição.',
              'Apresentação na obra, com a equipe se o cliente quiser; uma rodada de ajuste; termo de recebimento; 50% restantes.',
              'Retorno em 30 dias: a obra seguiu o plano? Gestão contratada? Indicação?'])
    p1 = page(SEC + ' · ficha interna', 'Ficha interna · duas ofertas',
        'A Conferência resolve a próxima parcela. O Plano resolve o caminho até a mudança. Os dois começam pela mesma conversa.',
        '<h2>Duas ofertas separadas</h2>' + of +
        '<div class="two-flow"><div><h2>Responsáveis</h2>' + resp + '</div><div>'
        '<h2>Sequência de execução e aceite</h2>' + seq + '</div></div>'
        '<p><b>Aceite:</b> apresentação feita e termo de recebimento assinado. Item que estava visível na obra e faltou no saldo de serviços é corrigido sem custo. '
        '<b>Conferência:</b> a nota vale como entrega; a devolutiva de 30 minutos é marcada no envio.</p>')
    global HORAS
    HORAS = '<div class="two-flow"><div>' + h_cm + '</div><div>' + h_pt + '</div></div>'
    return p1


HORAS = ''


def dinheiro():
    ind = ind_table([
        ('Conferência ' + brl(CM_PRECO) + ', via Scanner', CM_S, '0'), ('Conferência a ' + brl(1500) + ', via Scanner', CM_1500, '0'),
        ('Plano ' + brl(PT_PRECO) + ', com apoio técnico', PT, '0'), ('Plano ' + brl(PT_PRECO) + ', Aruak faz o trabalho técnico', PT_SEM, '0'),
        ('Plano ' + brl(PT_PRECO) + ', obra sem documentos (+30% de horas)', PT_ADV, '0'), ('Plano ' + brl(5500) + ', obra sem documentos (+30%)', PT_5500, '0'),
        ('Plano ' + brl(3900) + ' depois da Conferência', PT_POS, '0'),
    ])
    contas = (f'<p class="small">Conferência: {brl(CM.receita)} − {brl(CM_S.trib)} de tributos − {brl(CM.ccustos, True)} (1 h administrativa, uma ida, ART) − R$ 35 de aquisição pelo Scanner = '
              f'{brl(CM_S.disp, True)}; ÷ {hh(CM_H)} = {brl(CM_S.ph, True)}/h. '
              f'Plano: {brl(PT.receita)} − {brl(PT.trib)} − {brl(PT.ccustos, True)} ({hh(PT_T)} de técnico, {hh(PT_ADM)} administrativas, duas idas, ART) − R$ 35 = {brl(PT.disp, True)}; ÷ {hh(PT_A)} = {brl(PT.ph, True)}/h. '
              f'Depois da Conferência, o Aruak não relê os documentos nem refaz a conciliação: {hh(PT_POS.h)} e {brl(PT_POS.ph, True)}/h. O percurso completo do cliente soma {brl(PERC_CP)}.</p>')
    crit = table(['Critério até 18/12', 'Como medir', 'Decisão'], [
        ['Venda', 'Conferências ou Planos pagos com origem no Raio-X', '3 Conferências ou 1 Plano: seguir. Nenhum: rever as mensagens de resposta ao SCN-OBRA antes de mudar preço'],
        ['Entrega rentável', 'Disponível por hora medido de R$ 200 ou mais, nota ou plano no prazo, termo assinado', 'Abaixo da meta: apoio técnico, escopo ou preço'],
        ['Ponte', 'Plano que vira Gestão da conclusão, ou obra que termina seguindo o plano com a equipe atual', '1 caso: abrir divulgação do Raio-X para obras em andamento em janeiro'],
    ], 'sm', widths=['16%', '44%', '40%'])
    p_a = page(SEC + ' · ficha interna', 'Horas e margem',
        'Com apoio técnico, os dois níveis passam da meta. Sem apoio, o Plano não paga: nesse caso só se vende a Conferência.',
        '<h2>Horas por pessoa</h2>' + HORAS + '<h2>Margem por cenário</h2>' + ind)
    return p_a + page(SEC + ' · ficha interna', 'Caixa, regras de preço e critérios',
        'O contrato nunca fica negativo, e cada preço tem um piso que paga a meta.',
        '<h2>Como as contas foram feitas</h2>' + contas + '<div class="two-flow"><div><h2>Pagamento e caixa</h2>'
        f'<p><b>Conferência:</b> pagamento integral antes do agendamento, como na Visita Diagnóstica. O contrato nunca fica negativo.</p>'
        f'<p><b>Plano:</b> 50% na contratação e 50% na apresentação. Antes da segunda parcela saem só a ART e a primeira ida; o técnico é pago na entrega. '
        f'Caixa depois da primeira parcela: {brl(PT_CAIXA_1, True)}.</p>'
        '<h2>Regras de preço ' + tag('P') + '</h2>' +
        ul(['Abaixo de R$ 1.800 a Conferência não paga a meta (R$ 1.500 dá ' + brl(CM_1500.ph, True) + '/h).',
            'Obra sem contrato, sem orçamento ou recebida de outra equipe: R$ 5.500, porque as horas crescem cerca de 30%.',
            'O abatimento de R$ 600 vale só até 30 dias depois da Conferência, enquanto os documentos e a conciliação ainda servem.',
            'O Plano não é abatido da Gestão, como na Pré-obra: o ganho do cliente é começar a gestão com o levantamento pronto.']) +
        '</div><div><h2>Aquisição</h2><p>Raio-X do Scanner (código SCN-OBRA), clientes antigos e arquitetos com cliente em obra. O custo de venda está nas horas da conversa e nos R$ 35 de triagem.</p>'
        + box('Por que não é só vender a Gestão', '<p>Quem está no meio da obra já foi decepcionado por alguém. Pedir que essa pessoa entregue a conclusão a uma nova empresa, no primeiro contato, é pedir confiança que ainda não existe. '
              'A Conferência e o Plano entregam evidência antes, e a decisão sobre a gestão passa a ser tomada com números.</p>') +
        '</div></div><h2>Critério para manter, ajustar ou suspender</h2>' + crit)


def triagem():
    dec = table(['Resultado do Raio-X', 'Sinal na mensagem', 'Oferta'], [
        ['Conferir antes da próxima decisão', 'Valor a conciliar, medição sem registro ou próximo pagamento por adiantamento ou motivo pouco claro', 'Conferência da Medição'],
        ['Replanejamento prioritário', 'Falta dinheiro no custo mínimo ou caixa negativo nos 30 dias', 'Plano para Terminar'],
        ['Dados insuficientes', 'Sem medição e sem custo para terminar', f'Plano ({brl(5500)} se não houver documentos). Se o cliente só quer decidir a parcela: Conferência'],
        ['Obra parada ou em troca de prestadores', 'Classificação vermelha por situação', f'Plano a {brl(5500)} como vistoria de entrada; se o cliente quer alguém conduzindo, apresentar a Gestão junto'],
        ['Acompanhamento regular', 'Números fecham, entregas em dia', 'Nada a vender agora. Mandar a folha de três colunas e oferecer a Conferência antes da próxima parcela grande'],
        ['Qualquer nível com trinca aumentando', 'Sinal técnico marcado', 'Visita Diagnóstica antes de tudo'],
    ], 'sm', widths=['24%', '40%', '36%'])
    rot = ol(['O que fez você procurar agora?',
              'Qual é o próximo pagamento: de quanto, para quando e o que ele paga?',
              'O que existe por escrito: contrato, orçamento, medições, comprovantes?',
              'Quem está tocando a obra e como está a relação com essa equipe?',
              'Até quando você precisa se mudar ou entregar, e o que acontece se passar dessa data?',
              'Quem decide junto com você?',
              'Se o plano mostrar que falta dinheiro, o que é mais viável: deixar acabamentos para depois, rever escopo ou buscar outro recurso?'])
    docs = ul(['Contrato ou proposta aceita de cada equipe', 'Orçamento original e aditivos aprovados', 'Medições e recibos ou comprovantes de pagamento',
               'Notas e pedidos de material pagos', 'Projeto atualizado, se houver', 'Lista de pendências que o cliente já conhece', 'Fotos antigas da obra, se houver'])
    fech = msg('''Pelo que você me contou, o que faz sentido agora é [a Conferência da Medição / o Plano para Terminar]. Fica pronto em [prazo] e o investimento é [valor].

Posso te mandar a proposta agora?''')
    return page(SEC + ' · venda', 'Da triagem à proposta',
        'O código SCN-OBRA chega com a classificação e os números. A oferta sai da tabela, e a conversa confirma.',
        '<h2>Tabela de decisão</h2>' + dec +
        '<div class="two"><div><h2>Roteiro da conversa de 20 minutos</h2><p class="small">Uma pergunta por vez. Anotar as respostas na nota de qualificação do Placar.</p>' + rot +
        '<h3>Fechamento</h3>' + fech + '<p class="small">Toda conversa termina com sim, não ou data.</p></div>'
        '<div><h2>Documentos para pedir</h2>' + docs +
        box('Antes de vender', '<p>Confirmar: obra de até R$ 600 mil, apoio técnico disponível no período (para o Plano), data do próximo pagamento (para a Conferência) e nenhum sinal de risco estrutural.</p>') +
        box('Recusar ou adiar', ul(['Cliente quer laudo para processar a equipe: é laudo ou assistência técnica, com proposta própria.', 'Cliente quer que a Entre Colunas cobre a equipe por ele.', 'Obra acima de R$ 600 mil sem cotação própria.']), 'warn') +
        '</div></div>')


def mensagens():
    m_red = msg('''Olá, [nome]! Aqui é a Gabriela, da Entre Colunas. Recebi o seu Raio-X da obra, obrigada por mandar os números.

Pelo que você informou, o dinheiro que está reservado não cobre o que falta para terminar. Isso tem solução, mas a decisão precisa vir antes dos próximos pagamentos.

O Aruak, nosso engenheiro, pode conversar com você por 20 minutos para entender a obra e dizer o que faz sentido fazer agora.

Você prefere amanhã às [hora] ou [dia] às [hora]?''')
    m_conf = msg('''Olá, [nome]! Aqui é a Gabriela, da Entre Colunas. Recebi o seu Raio-X.

Vi que existe um pagamento de [valor] pedido para [data] e uma parte do que já foi pago ainda precisa ser conferida com o que foi entregue.

Antes de pagar, o Aruak pode conferir a última medição na obra, serviço por serviço. Para isso a visita precisa acontecer até [data limite].

Posso marcar uma conversa de 20 minutos com ele hoje às [hora] ou amanhã às [hora]?''')
    m_ins = msg('''Olá, [nome]! Aqui é a Gabriela, da Entre Colunas. Recebi o seu Raio-X da obra.

Ainda faltam duas informações para saber se o dinheiro chega até o fim: a medição do que foi feito e o custo para terminar. É muito comum, e dá para levantar.

Se quiser começar sozinho, peça à equipe uma folha com três colunas: serviço que falta, valor que ainda será pago e data prevista.

Se preferir que a gente levante isso com você, o Aruak conversa 20 minutos e explica como funciona. Qual horário fica melhor?''')
    m_ok = msg('''Olá, [nome]! Aqui é a Gabriela, da Entre Colunas. Recebi o seu Raio-X e os números da sua obra fecham. Isso é raro, parabéns pelo controle.

Para continuar assim, mantenha a medição antes de cada pagamento e atualize o custo para terminar uma vez por mês.

Se aparecer uma parcela grande e você quiser uma segunda opinião antes de pagar, é só me chamar aqui.''')
    m_prop = msg('''[Nome], segue a proposta do [Plano para Terminar / da Conferência da Medição], com o que você recebe, o prazo e o investimento.

Para confirmar, basta responder aqui com o seu aceite e fazer o PIX [da entrada / do valor]. Em seguida eu mando a lista de documentos e marco a visita.

Você consegue me dar uma posição até [dia]?''')
    m_ent = msg('''[Nome], o seu Plano para Terminar está pronto. O Aruak quer apresentar na obra, porque fica mais fácil mostrar cada etapa no lugar.

Se quiser, a sua equipe pode participar da segunda metade da reunião, quando passamos as metas e a forma de medição.

Fica bom [dia] às [hora]?''')
    return page(SEC + ' · venda', 'Mensagens prontas',
        'Respostas ao SCN-OBRA por classificação, envio da proposta e entrega. Sem travessão, parágrafos curtos e o próximo passo no fim.',
        '<div class="two"><div><h3>Replanejamento prioritário</h3>' + m_red + '<h3>Conferir antes da próxima decisão</h3>' + m_conf +
        '<h3>Dados insuficientes</h3>' + m_ins + '</div><div><h3>Acompanhamento regular</h3>' + m_ok + '<h3>Envio da proposta</h3>' + m_prop +
        '<h3>Plano pronto</h3>' + m_ent +
        box('Prazo de resposta ' + tag('P'), '<p>Responder ao SCN-OBRA no mesmo dia útil. Quando o Raio-X traz um pagamento com data em até 5 dias, responder em até 2 horas no horário comercial.</p>') +
        '</div></div>')


def execucao():
    chk = table(['', 'Em cada etapa da obra'], [[SQ, x] for x in [
        'Estado: pronta, em andamento ou não começou, com foto geral datada',
        'Qualidade visível: prumo, nível, esquadro, revestimento oco, fissuras, umidade, fiação provisória',
        'Medidas e quantidades do que falta, para o saldo de serviços',
        'Material na obra: contagem, estado e foto, para a conciliação',
        'Serviço refeito ou a refazer e quem ficou responsável',
        'Frentes que dependem de decisão ou compra do proprietário',
        'Segurança: escoramento, aberturas sem proteção, instalação provisória. Risco estrutural: parar e avisar o cliente por escrito no mesmo dia',
    ]], 'sm check', widths=['6%', '94%'])
    nota = table(['Serviço medido', 'Quantidade medida', 'Observado na obra', 'Situação', 'O que pedir à equipe'], [
        ['Exemplo: reboco interno, pavimento térreo', '180 m²', '150 m² executados; 30 m² só chapiscados', 'Diverge', 'Retirar 30 m² da medição ou concluir antes do pagamento'],
        ['Exemplo: tubulação elétrica do térreo', 'Etapa inteira', 'Executada; caixas sem fixação em 2 cômodos', 'Confere com pendência', 'Fixar as caixas antes do reboco'],
    ], 'sm', widths=['22%', '13%', '27%', '13%', '25%'])
    plano = ol(['<b>Resumo para decidir:</b> classificação, quanto falta, em que faixa e o que decidir primeiro.',
                '<b>Situação recebida:</b> estado de cada etapa, com fotos datadas e pendências.',
                '<b>Pago e executado:</b> conciliação com base nos documentos entregues, e o que ficou sem documento.',
                '<b>Saldo de serviços:</b> o que falta, com quantidades.',
                '<b>Orçamento para terminar:</b> preço da equipe atual por etapa e cotações nos itens mais caros, mínimo e máximo.',
                '<b>Sequência e cronograma até a mudança:</b> ordem das etapas, datas e compras críticas com prazo de pedido.',
                '<b>Plano de caixa:</b> pagamentos mês a mês diante dos recursos; se faltar, o que pode ficar para depois.',
                '<b>Regra de medição para a equipe:</b> metas semanais por escrito, pagamento só do medido e aceito, extras aprovados com valor antes. Condições da gestão, se o cliente pedir.'])
    return page(SEC + ' · execução', 'Campo e entregáveis',
        'O mesmo checklist serve para os dois níveis. A Conferência olha só os serviços da medição; o Plano olha a obra inteira.',
        '<h2>Checklist da visita</h2>' + chk +
        '<h2>Modelo da nota de conferência</h2><p class="small">Uma linha por serviço da medição. Situação: confere, confere com pendência, diverge ou não verificável. Fechar com o total medido, o total que confere e a recomendação para a parcela.</p>' + nota +
        '<div class="two-flow"><div><h2>Sumário do Plano para Terminar</h2>' + plano + '</div><div>' +
        box('Como escrever os achados ' + tag('P'), ul(['Fato, medida e foto. Sem adjetivo sobre a equipe.', 'O que não foi possível verificar fica escrito como não verificável, nunca como defeito.',
            'Valor sem documento fica marcado como informado pelo cliente.', 'A nota registra a data da visita e não garante vícios ocultos.'])) +
        box('Com a equipe atual', '<p>A Entre Colunas não fala com a equipe em nome do cliente sem combinar antes. Quando o cliente pede a apresentação conjunta, a primeira metade é só com ele (números e achados) e a segunda com a equipe (metas e forma de medição).</p>') +
        '</div></div>')


def riscos_duvidas():
    riscos = table(['Risco', 'Tratamento'], [
        ['Cliente quer usar a nota contra a equipe', 'Nota factual; processo judicial é laudo ou assistência técnica, com proposta própria'],
        ['Equipe não dá preço para terminar', 'Usar as cotações e registrar o pedido feito'],
        ['Documentos ausentes', f'Premissas escritas e preço de {brl(5500)}'],
        ['Sem apoio técnico no período', f'Não vender o Plano: cai para {brl(PT_SEM.ph, True)}/h. Vender só a Conferência'],
        ['Parcela vence antes da visita', 'Não prometer conferência em menos de 4 dias úteis'],
        ['Obra maior que o previsto', 'Acima de R$ 600 mil, sob cotação'],
        ['Cliente leva o plano para outra empresa', 'O plano é dele e foi pago. A Gestão é vendida pelo método, não pela posse do plano'],
    ], 'sm', widths=['36%', '64%'])
    duv = ol([f'<b>Preços.</b> Confirmar {brl(CM_PRECO)} para a Conferência, {brl(PT_PRECO)} e {brl(5500)} para o Plano e {brl(3900)} para quem fez a Conferência.',
              '<b>Apoio técnico.</b> É o mesmo profissional da Pré-obra? Sem ele, só a Conferência entra no catálogo.',
              '<b>ART.</b> Qual atividade registrar na Conferência e no Plano. Incluir na pergunta ao CREA-GO já prevista para 05/11.',
              '<b>Limite de R$ 600 mil.</b> Serve para as obras que você costuma receber?',
              '<b>Apresentação com a equipe.</b> Você quer fazer a segunda metade da reunião com a equipe atual?',
              '<b>Nome.</b> “Plano para Terminar a Obra” e “Conferência da Medição” ficam assim no catálogo e no Scanner?',
              '<b>Assistente.</b> Incluir os dois níveis no arquivo de ofertas do GPT, com os preços confirmados.'])
    return page(SEC + ' · decisão', 'Riscos, teste e decisões pendentes',
        'O teste vai até 18/12, junto com a revisão por produto do manual.',
        '<div class="two"><div><h2>Riscos</h2>' + riscos + box('Achado estrutural', '<p>Trinca ativa, deformação ou armadura exposta: avisar o cliente por escrito no mesmo dia, indicar a Visita Diagnóstica ou o laudo e não seguir com o plano naquele ponto até a avaliação.</p>', 'red') + '</div><div><h2>Decisões do Aruak</h2>' + duv +
        box('Primeira ação', '<p>Escolher entre os clientes e contatos atuais uma obra em andamento e oferecer a Conferência da Medição antes da próxima parcela. É o caso real que mede as horas marcadas como estimadas.</p>') +
        '</div></div>')


def main():
    body = capa() + comercial() + ficha() + dinheiro() + triagem() + mensagens() + execucao() + riscos_duvidas()
    html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Plano para Terminar a Obra</title><style>' + CSS +
            '.client{font-size:9.3pt}.client h1.ct{font-size:24pt}.cgrid{gap:4mm 6mm}</style></head><body>' + body + '</body></html>')
    open('plano.html', 'w').write(html)
    print('ok', len(html))


if __name__ == '__main__':
    main()
