# -*- coding: utf-8 -*-
from common import *

SQ = '<span class="sq"></span>'

def com_visita():
    blocos = [
        ('O problema', '<p>O conserto voltou, a mancha cresce, ninguém sabe dizer de onde vem a água, ou cada orçamento propõe uma solução diferente. Gastar antes de saber a causa costuma sair caro.</p>'),
        ('Para quem é', '<p>Morador ou proprietário que vai agir, contratando o conserto, e precisa saber o que fazer primeiro. Não precisa apresentar documento a terceiros.</p>'),
        ('O que você recebe', ul(['Uma visita de até 1h30, com medidor de umidade, trena e registro fotográfico.',
            'Nota técnica de uma página em até 2 dias úteis: o que foi observado, o que não foi possível verificar e por quê, a causa provável quando houver evidência, o que fazer e o que evitar agora, e o próximo passo.',
            'Um esclarecimento por mensagem ou áudio.', 'A nota é sua, mesmo se você contratar outra pessoa para o conserto.'])),
        ('O que não está incluído', ul(['Abertura de forro ou revestimento, ensaios, outra unidade ou segunda visita.',
            'Não é laudo e não serve para apresentar a construtora, condomínio, seguradora ou Justiça. Para isso existe o Laudo Técnico.',
            'Quando uma visita não basta para concluir, a nota diz o porquê e qual investigação seria necessária. A decisão é sua.'])),
        ('Como funciona', ol(['Conversa rápida para definir a pergunta da visita.', 'Pagamento e agendamento.',
            'Visita com alguém no local que dê acesso aos ambientes.', 'Nota técnica em até 2 dias úteis.'])),
        ('Quem assina', '<p>' + RT + ', com ART registrada no CREA-GO.</p>'),
    ]
    preco = ('<table><tr><td>Visita Diagnóstica</td><td class="v">R$ 1.200</td></tr><tr><td>Pagamento</td><td class="v">antes do agendamento</td></tr></table>'
             '<p>Se em até 30 dias você contratar o laudo sobre o mesmo problema e a visita servir como a vistoria do laudo, o valor da visita é abatido. Se o laudo exigir nova vistoria, metade é abatida.</p>')
    prox = '<p>Mande três fotos (de longe, de perto e da parede ou teto ao lado) e a sua pergunta em uma frase.</p><p>Respondemos com dois horários.</p>'
    return client_page('Frente 2 · modalidade A · página comercial', 'Visita Diagnóstica',
        'Antes de gastar com conserto, um engenheiro vai ao imóvel e te diz por escrito o que foi observado e qual providência faz sentido agora.',
        blocos, preco, prox)

def com_laudo():
    blocos = [
        ('O problema', '<p>Você precisa mostrar o que está acontecendo, a causa ou o estado do imóvel a alguém que vai decidir, e a palavra do morador ou um orçamento não bastam.</p>'),
        ('Usos mais comuns', ul(['Problema construtivo para apresentar à construtora ou ao condomínio.', 'Negociação com vizinho ou seguradora.',
            'Instrução de processo judicial.', 'Usucapião e regularização, com proposta própria.'])),
        ('O que você recebe', ul(['Análise dos documentos disponíveis: projeto, contrato, fotos, laudos anteriores.',
            'Vistoria de até 2 horas, com registro fotográfico e medições.',
            'Laudo com a pergunta, o método, as evidências, a conclusão possível e os seus limites, em até 5 dias úteis após a vistoria.',
            'ART registrada no CREA-GO, uma rodada de esclarecimentos e a apresentação do laudo.'])),
        ('O que não está incluído', ul(['Ensaios e laboratório, contratados e pagos diretamente por você.',
            'Segunda vistoria, outros imóveis, quesitos, pareceres complementares e audiência, cobrados por hora técnica.',
            'Laudo com conclusão definida antes da vistoria.', 'Processo com perito nomeado: assistência técnica, com proposta própria.'])),
        ('Como funciona', ol(['Conversa de 15 minutos para definir a pergunta, os documentos e para quem o laudo vai.', 'Proposta de uma página e 50% na contratação.',
            'Vistoria agendada.', 'Laudo, apresentação e 50% na entrega.'])),
        ('Quem assina', '<p>' + RT + '.</p>'),
    ]
    preco = ('<table><tr><td>Laudo delimitado: uma pergunta, um imóvel, uma vistoria</td><td class="v">a partir de R$ 3.000</td></tr>'
             '<tr><td>Laudo ampliado: mais de uma vistoria ou de um sistema</td><td class="v">a partir de R$ 3.700</td></tr>'
             '<tr><td>Serviços adicionais</td><td class="v">R$ 350 por hora técnica</td></tr></table>'
             '<p>50% na contratação e 50% na entrega. Ensaios pagos diretamente ao laboratório.</p>')
    prox = '<p>Marque uma conversa de 15 minutos com o Aruak. Você sai dela com a pergunta do laudo definida e a proposta no mesmo dia.</p>'
    return client_page('Frente 2 · modalidade B · página comercial', 'Laudo Técnico com ART',
        'Um documento técnico para apresentar a quem precisa decidir: construtora, condomínio, vizinho, seguradora, advogado ou Justiça.',
        blocos, preco, prox)

def com_vistoria():
    blocos = [
        ('Vai receber um imóvel novo', '<p>O que não estiver registrado na entrega das chaves fica mais difícil de cobrar depois. A vistoria percorre ambiente por ambiente com checklist, e o relatório fotográfico vai pronto para a construtora.</p>'),
        ('Vai comprar um imóvel usado', '<p>Antes de assinar, vale ver o que não aparece na visita do corretor: umidade, instalações antigas, reformas sem projeto. O relatório mostra o que precisa de reparo para você negociar com informação.</p>'),
        ('O que você recebe', ul(['Checklist por ambiente e por sistema: pisos e revestimentos, paredes e tetos, esquadrias, instalações hidráulicas e elétricas, louças e metais, impermeabilização visível.',
            'Relatório fotográfico com ART em até 2 dias úteis.', 'Na Completa: uma revisita para conferir as correções e a atualização do relatório.'])),
        ('O que não está incluído', ul(['Ensaios destrutivos, abertura de paredes ou forros, teste de estanqueidade prolongado e áreas sem acesso seguro.',
            'Revisitas além da prevista no pacote, com valor próprio.', 'Áreas comuns do condomínio.'])),
        ('Experiência', '<p>Mais de 100 vistorias entregues.</p>'),
        ('Como funciona', ol(['Envie a metragem privativa, o endereço e a data das chaves ou da assinatura.', 'Confirmamos o horário com o pagamento.', 'Relatório em até 2 dias úteis.'])),
    ]
    preco = ('<table><tr><td><b>Área privativa</b></td><td class="v">Vistoria</td><td class="v">Completa</td></tr>'
             '<tr><td>Até 100 m²</td><td class="v">R$ 840</td><td class="v">R$ 1.080</td></tr>'
             '<tr><td>Acima de 100 e abaixo de 250 m²</td><td class="v">R$ 1.150</td><td class="v">R$ 1.500</td></tr>'
             '<tr><td>250 m² ou mais</td><td class="v">R$ 1.400</td><td class="v">R$ 1.950</td></tr></table>'
             '<p>Pagamento na confirmação do agendamento. A revisita da Completa vale para o mesmo imóvel, em até 60 dias.</p>')
    prox = '<p>Mande a metragem, o endereço e a data das chaves ou da assinatura. Respondemos com o valor e dois horários.</p>'
    return client_page('Frente 2 · modalidade C · página comercial', 'Vistoria de Recebimento ou de Compra',
        'Receba ou compre o imóvel sabendo o que precisa ser corrigido, com tudo registrado por escrito.',
        blocos, preco, prox)

def ficha():
    qual = table(['Pergunta do cliente', 'Oferta', 'Quando recomendar', 'Recusar ou mudar de produto quando'], [
        ['“Qual providência faz sentido agora?”', 'Visita Diagnóstica', 'Vai agir e não precisa de documento para terceiro', 'Há risco imediato (orientar segurança primeiro); quer conclusão por foto'],
        ['“Que conclusão consigo sustentar sobre este problema?”', 'Laudo delimitado', 'Precisa mostrar a alguém; o problema voltou depois de conserto', 'Quer laudo com a conclusão pronta; a pergunta não pode ser delimitada'],
        ['Idem, com mais de um sistema, unidade ou ensaio', 'Laudo ampliado', 'Duas vistorias ou mais, abertura, ensaio ou especialista', 'Perito nomeado em processo: assistência técnica'],
        ['“O que a construtora precisa corrigir?” ou “o que pesa na compra?”', 'Vistoria ou Completa', 'Entrega de chaves marcada ou compra em negociação', 'Quer vistoria de áreas comuns ou laudo de desempenho'],
    ], 'sm', widths=['27%', '15%', '28%', '30%'])
    resp = table(['Papel', 'Visita', 'Laudo', 'Vistoria'], [
        ['Vende e define a pergunta', 'Gabriela (condição padrão); Aruak se houver dúvida', 'Aruak', 'Gabriela'],
        ['Executa o campo e o documento', 'Aruak', 'Aruak', 'Aruak; júnior só após contratação ' + tag('P')],
        ['Revisa e assina', 'Aruak', 'Aruak', 'Aruak'],
        ['Agenda, cobra, emite NF, registra', 'Gabriela', 'Gabriela', 'Gabriela'],
        ['Lança no Mais Controle', 'Gabriela e Flávia', 'Gabriela e Flávia', 'Gabriela e Flávia'],
    ], 'sm', widths=['28%', '24%', '24%', '24%'])
    hv = table(['Visita Diagnóstica', 'Aruak', 'Equipe', 'Origem'], [
        ['Conversa comercial e pergunta técnica', '0,5 h', '—', tag('E')], ['Agendamento e cobrança', '—', '0,25 h adm', tag('E')],
        ['Trajeto, ida e volta', '1 h', '—', tag('E')], ['Campo', '1,5 h', '—', tag('A')],
        ['Nota técnica', '1,25 h', '—', tag('A') + ' 1 a 1,5 h'], ['Retorno e esclarecimento', '0,25 h', '—', tag('E')],
        ['NF e Placar', '—', '0,25 h adm', tag('E')], {'cls': 'tot', 'cells': ['Total', '4,5 h', '0,5 h', '']},
    ], 'sm', widths=['52%', '14%', '18%', '16%'])
    hl = table(['Laudo delimitado', 'Aruak', 'Equipe', 'Origem'], [
        ['Pergunta, documentos e proposta', '0,75 h', '—', tag('E')], ['Trajeto, ida e volta', '1 h', '—', tag('E')],
        ['Vistoria', '2 h', '—', tag('A')], ['Montagem do laudo', '3 h', '—', tag('A')],
        ['Revisão, emissão e ART', '0,5 h', '—', tag('E')], ['Apresentação e esclarecimento', '1 h', '—', tag('E')],
        ['Proposta, cobrança, ART e NF', '—', '1 h adm', tag('E')], {'cls': 'tot', 'cells': ['Total', '8,25 h', '1 h', '']},
        ['Estudo de documentos e hipóteses', 'não incluído', '', '<span class="tg">[pendente]</span>'],
    ], 'sm', widths=['52%', '14%', '18%', '16%'])
    hvi = table(['Vistoria (horas do Aruak)', 'Até 100 m²', '100 a 250 m²', '250 m² ou mais', 'Origem'], [
        ['Conversa comercial', '0,5', '0,5', '0,5', tag('E')], ['Trajeto, ida e volta', '1', '1', '1', tag('E')],
        ['Campo', '1', '1,67', '2,5', tag('A')], ['Relatório', '1', '1', '1', tag('A')], ['Envio e retorno', '0,25', '0,25', '0,25', tag('E')],
        {'cls': 'tot', 'cells': ['Vistoria', '3,75 h', '4,42 h', '5,25 h', '']},
        ['Revisita da Completa: trajeto, metade do campo e atualização', '+1,75', '+2,08', '+2,5', tag('E')],
        {'cls': 'tot', 'cells': ['Completa', '5,5 h', '6,5 h', '7,75 h', '']},
    ], 'sm num', widths=['46%', '13%', '14%', '14%', '13%'])
    seq = table(['Etapa', 'Visita', 'Laudo', 'Vistoria'], [
        ['1. Entrada', 'Código do Scanner ou indicação; 3 fotos e pergunta', 'Conversa de 15 min com o Aruak', 'Metragem, endereço, data das chaves'],
        ['2. Condição', 'R$ 1.200 por escrito, dois horários', 'Proposta de 1 página', 'Valor da tabela e dois horários'],
        ['3. Dinheiro antes do campo', '100% antes de agendar', '50% na contratação', 'Pagamento na confirmação ' + tag('P')],
        ['4. Campo', 'Checklist de visita', 'Checklist de laudo e documentos', 'Checklist de vistoria'],
        ['5. Documento', 'Nota de 1 página em 2 dias úteis', 'Laudo em 5 dias úteis', 'Relatório em 2 dias úteis ' + tag('P')],
        ['6. Aceite', 'Nota enviada e retorno em até 7 dias', 'Apresentação e termo de recebimento', 'Relatório enviado e recebimento confirmado'],
        ['7. Próximo degrau', 'Reparo, laudo ou investigação', 'Reparo, gestão ou assistência', 'Revisita, reparo ou laudo'],
    ], 'sm', widths=['20%', '27%', '27%', '26%'])
    riscos = table(['Risco', 'Como tratar'], [
        ['Visita virar laudo de graça', 'Nota de 1 página com limites escritos; documento para terceiro é laudo'],
        ['Conclusão sem evidência', 'Causa só como provável, possível ou a investigar, com o grau escrito'],
        ['Revisita não paga na Completa pequena', 'Vender a Completa até 100 m² só com revisitas agrupadas'],
        ['Horas do laudo maiores que as estimadas', 'Reconstruir o último laudo; se passar de 10,25 h, rever o preço mínimo'],
        ['Aruak é o único engenheiro', 'Janelas fixas de campo; 8 vistorias por mês abrem a análise do júnior'],
        ['Contratação remota com pagamento antecipado', 'Cláusula de agendamento, arrependimento e cancelamento (Vicente, CDC art. 49)'],
    ], 'sm', widths=['40%', '60%'])
    caixa = table(['Modalidade', 'Recebe', 'Paga antes de receber tudo', 'Pico negativo'], [
        ['Visita', '100% antes do agendamento', 'ART e ida (' + brl(ART1 + IDA, True) + ')', 'R$ 0'],
        ['Laudo', '50% na contratação (R$ 1.500), 50% na entrega', 'ART e ida (' + brl(ART1 + IDA, True) + '), cobertas pela entrada', 'R$ 0'],
        ['Vistoria', 'Na confirmação do agendamento ' + tag('P'), 'ART e idas', 'R$ 0'],
    ], 'sm', widths=['16%', '36%', '34%', '14%'])
    ind = ind_table([
        ('Visita R$ 750, indicação (preço anterior)', V750, '0'), ('Visita R$ 1.200, indicação', V1200, '0'),
        ('Visita R$ 1.200, Scanner (+R$ 35)', V1200S, '0'), ('Visita R$ 1.200 se consumir 6 h', V1200_6h, '0'),
        ('Laudo R$ 3.000', L3000, '0 (vendido, horas não medidas)'), ('Laudo R$ 3.000 com mais 2 h de estudo', L3000_10, '0'),
        ('Laudo ampliado R$ 3.700 (2 idas, 1,5 h adm)', L3700, '0'),
        ('Vistoria até 100 m², R$ 840', VI['ate100'][0], '0 (mais de 100 feitas)'), ('Completa até 100 m², R$ 1.080', VI['ate100'][1], '0'),
        ('Vistoria 100 a 250 m², R$ 1.150', VI['meio'][0], '0'), ('Completa 100 a 250 m², R$ 1.500', VI['meio'][1], '0'),
        ('Vistoria 250 m² ou mais, R$ 1.400', VI['acima'][0], '0'), ('Completa 250 m² ou mais, R$ 1.950', VI['acima'][1], '0'),
    ])
    crit = table(['Produto', 'Teste e prazo', 'Manter', 'Ajustar', 'Suspender ou repensar'], [
        ['Visita', '5 casos qualificados até 30/11', '2 ou mais pagos e horas reais de até 5 h', '1 pago, ou horas acima de 6 h: nota mais curta, sem 2º esclarecimento, ou só por indicação', '0 pagos com objeção de preço: Scanner leva direto ao laudo ou reparo; 0 sem objeção: revisar a mensagem'],
        ['Laudo', 'Reconstruir o último laudo pago até 06/11', 'Horas reais até 10,25 h', 'Acima de 10,25 h: preço mínimo de ' + brl(L3000_10.pmin, True) + ' para a meta', 'Se o estudo não couber, vender só o ampliado'],
        ['Vistoria', 'Cronometrar 3 vistorias comparáveis até 30/11', 'Pequena acima de R$ 150/h medidos', 'Agrupar por prédio, checklist digital, Gabriela no agendamento e na entrega', 'Completa até 100 m² fora de agrupamento'],
    ], 'sm', widths=['10%', '20%', '20%', '27%', '23%'])
    p1 = page('Frente 2 · ficha interna', 'Visita, Laudo e Vistoria · ficha interna', 'A escolha da modalidade depende da pergunta do cliente, das evidências necessárias e da finalidade do documento.',
        '<h2>Qual oferta para cada pergunta</h2>' + qual + '<h2>Responsáveis</h2>' + resp +
        '<h2>Horas por pessoa</h2><div class="two"><div>' + hv + '</div><div>' + hl + '</div></div>' + hvi)
    p2 = page('Frente 2 · ficha interna', 'Visita, Laudo e Vistoria · operação e dinheiro', 'Sequência, aceite, riscos, caixa, margem e regra de decisão de cada modalidade.',
        '<h2>Sequência de execução e aceite</h2>' + seq + '<div class="two"><div><h2>Riscos</h2>' + riscos + '</div><div><h2>Pagamento e caixa</h2>' + caixa +
        '<p class="small"><b>Aquisição:</b> indicação direta sem custo atribuído (a meia hora comercial do Aruak já está nas horas); Scanner, R$ 35 a R$ 43,75 por venda; clientes antigos e construtoras, sem custo de mídia.</p></div></div>'
        '<h2>Margem: as três contas por modalidade</h2>' + ind +
        '<p class="small">Premissas: 8% de tributos, ART de R$ 108,39 por serviço (hoje há ART para cada laudo ' + tag('A') + '), R$ 50 por ida, administrativo a R$ 35/h. Caixa livre de cada contrato: igual ao disponível depois de pagar ART e idas, porque o dinheiro entra antes do campo.</p>'
        '<h2>Critério para manter, ajustar ou suspender</h2>' + crit)
    return p1 + p2

def exemplo():
    real_h = 4.3
    ex = V1200S
    regs = table(['Campo do registro', 'Previsto', 'Realizado ' + tag('S')], [
        ['Cliente e origem', 'Helena, apto 802, Setor Bueno · SCN-DIAGNOSTICO', 'Código recebido 04/11 14h10; 1ª resposta 14h40'],
        ['Pergunta técnica', 'De onde vem a mancha no teto do banheiro e o que fazer agora?', 'Confirmada com as palavras da cliente'],
        ['Condição', 'R$ 1.200 antes do agendamento', 'PIX em 05/11; visita em 10/11 às 9h'],
        ['Horas do Aruak', '4,5 h', '4,3 h: comercial 0,25 · trajeto 0,9 · campo 1,4 · nota 1,5 · retorno 0,25'],
        ['Horas da equipe', '0,5 h adm', '0,5 h adm'],
        ['Saídas', 'ART R$ 108,39 · ida R$ 50 · aquisição R$ 35 · tributos R$ 96', 'Iguais; ART paga em 05/11, depois do PIX'],
        ['Disponível', brl(ex.disp, True), brl(ex.disp, True)],
        ['Disponível por hora do Aruak', brl(ex.ph, True), brl(r2(ex.disp / real_h), True)],
        ['Saldo parcial', brl(ex.saldo, True), brl(r2(ex.disp - real_h * AR), True)],
        ['Caixa livre do contrato', 'Positivo desde o PIX', brl(r2(1200 - ART1 - IDA - 0.5 * ADM - 96), True) + ' depois de ART, ida, adm e tributos'],
        ['Entrega e aceite', 'Nota até 12/11', 'Nota enviada 11/11; retorno da cliente em 13/11'],
        ['Próximo degrau', 'Reparo, laudo ou investigação', 'Origem provável no box do apto 902; laudo oferecido caso o vizinho conteste'],
    ], 'sm', widths=['22%', '34%', '44%'])
    perc = table(['Percurso visita + laudo, mesmo problema', 'Receita', 'Horas do Aruak', 'Disponível por hora', 'Saldo parcial'], [
        ['Abatimento integral, a visita substitui a vistoria do laudo', brl(PERC.receita), hh(PERC.h), brl(PERC.ph), brl(PERC.saldo)],
        ['Abatimento integral, mas o laudo exige nova vistoria', brl(PERC_NOVA.receita), hh(PERC_NOVA.h), brl(PERC_NOVA.ph), brl(PERC_NOVA.saldo)],
        ['Nova vistoria com abatimento de 50% (R$ 600)', brl(PERC_NOVA_50.receita), hh(PERC_NOVA_50.h), brl(PERC_NOVA_50.ph), brl(PERC_NOVA_50.saldo)],
    ], 'num', widths=['44%', '13%', '14%', '15%', '14%'])
    comp_rows = []
    for lab, ind, sc in (('Visita R$ 1.200', V1200, V1200S), ('Laudo R$ 3.000', L3000, L3000S), ('Vistoria 100 a 250 m², R$ 1.150', VI['meio'][0], VI_S)):
        sc2 = r2((ind.disp - SC_VENDA20) / ind.h)
        comp_rows.append([lab, brl(ind.ph), brl(ind.saldo), brl(sc.ph), brl(sc.saldo), brl(sc2), brl(ind.pmin), brl(sc.pmin)])
    vs4 = r2(V1200S.disp / 4.0)
    comp = table(['Oferta', 'Indicação: por hora', 'Indicação: saldo', 'Scanner R$ 35: por hora', 'Scanner R$ 35: saldo', 'Scanner R$ 43,75: por hora', 'Preço meta: indicação', 'Preço meta: Scanner'], comp_rows, 'num sm',
                 widths=['22%', '10%', '10%', '11%', '11%', '12%', '12%', '12%'])
    corpo = ('<h2>Exemplo preenchido: registro de uma visita ' + tag('S') + '</h2>' + regs +
             '<h2>Abatimento da visita no laudo</h2>' + perc +
             box('Regra ' + tag('P'), '<p>Abatimento integral só quando a visita substitui a vistoria do laudo. Se o laudo exigir nova vistoria, abater metade da visita (R$ 600). Precificar à parte qualquer documento ou estudo novo.</p>') +
             '<h2>Indicação direta × Scanner</h2>' + comp +
             f'<p>O Scanner custa entre R$ 35 e R$ 43,75 por venda e reduz o disponível por hora em poucos reais. Ele compensa quando traz vendas que não viriam por indicação e quando tira do Aruak a conversa comercial: se a Gabriela fizer a triagem e o Aruak deixar de gastar a meia hora comercial, a visita do Scanner passa a {brl(vs4, True)} por hora dele, acima da indicação direta.</p>')
    return page('Frente 2 · exemplo e canais', 'Exemplo preenchido e comparação de canais', 'Como a visita aparece no registro do contrato e quanto o canal muda o resultado.', corpo)

def agenda_checklist():
    regras = ol([
        'Confirmar a pergunta técnica em uma linha, repetida com as palavras do cliente.',
        'Receber antes do campo: visita 100%; laudo 50%; vistoria na confirmação do horário.',
        'Combinar quem estará no local e o acesso necessário: teto, ralo, quadro, área técnica, chaves e documentos da construtora.',
        'Campo em janelas fixas do Aruak, agrupando visitas e vistorias por região ou prédio ' + tag('P') + '.',
        'Na véspera, lembrar o que será verificado e pedir para não limpar, pintar nem consertar antes.',
        'Reagendamento: uma vez sem custo, com 24 horas de aviso. Arrependimento e cancelamento conforme a cláusula que o Vicente vai redigir para contratação pelo WhatsApp (CDC, art. 49) <span class="tg">[pendente]</span>.',
        'Fora de Goiânia: acrescentar deslocamento por quilômetro <span class="tg">[pendente de decisão]</span>.',
    ])
    m1 = msg('''[Nome], pagamento recebido, obrigada. A visita está confirmada para [dia] às [hora], no [endereço].

O Aruak vai olhar [o teto do banheiro e o apartamento de cima, se tiver acesso]. Peço que alguém esteja no local e que nada seja limpo ou pintado até lá.

Qualquer imprevisto, me avisa com 24 horas que eu remarco sem custo.''')
    m2 = msg('''[Nome], boa tarde. Amanhã às [hora] o Aruak passa aí para a vistoria.

Deixa separado, se tiver, o manual do proprietário e a planta do apartamento. Se for possível, peça para a construtora liberar a energia e a água antes do horário.

Até amanhã.''')
    chk_v = table(['', 'Visita e laudo: o que conferir', 'Registro'], [
        [SQ, 'Antes de sair: medidor de umidade, trena laser, lanterna, régua de fissuras, celular carregado, ficha com a pergunta técnica', 'Ficha aberta'],
        [SQ, 'Ao chegar: reler a pergunta com o cliente; perguntar quando começou, o que já tentaram, se piora com chuva ou com uso', 'Histórico em 3 linhas'],
        [SQ, 'Percorrer do sintoma para a origem provável: ambiente afetado, vizinho de cima e do lado, prumadas, ralos, registros, cobertura e fachada quando acessíveis', 'Croqui com pontos numerados'],
        [SQ, 'Medir umidade em grade, com uma leitura de referência em área seca; medir abertura e extensão de fissuras e manchas', 'Tabela de leituras'],
        [SQ, 'Fotografar geral, médio e detalhe, com régua ou escala, na numeração do croqui', 'Fotos numeradas'],
        [SQ, 'Anotar o que não foi possível ver e por quê (sem acesso, sem abertura, sem autorização)', 'Lista de limitações'],
        [SQ, 'Laudo: conferir e fotografar documentos recebidos; registrar quem acompanhou', 'Lista de documentos'],
        [SQ, 'Antes de sair: só orientação de segurança; nenhuma conclusão verbal definitiva; combinar data da nota ou do laudo', 'Data combinada'],
    ], 'sm check', widths=['5%', '70%', '25%'])
    chk_vi = table(['', 'Vistoria: sistemas a percorrer em cada ambiente', 'Como verificar'], [
        [SQ, 'Pisos e revestimentos', 'Percussão (som cavo), planicidade, rejunte, caimento para o ralo, peças trincadas ou manchadas'],
        [SQ, 'Paredes, tetos e pintura', 'Fissuras, prumo e esquadro visíveis, manchas, acabamento'],
        [SQ, 'Esquadrias e vidros', 'Abrir e fechar, vedação, ferragens, riscos, folgas'],
        [SQ, 'Hidráulica', 'Abrir todos os pontos, vazamentos, escoamento, sifões, registros, pressão'],
        [SQ, 'Elétrica', 'Tomadas com testador, identificação do quadro, disjuntores, DR quando houver, iluminação'],
        [SQ, 'Louças, metais e bancadas', 'Fixação, vedação, funcionamento, acabamento'],
        [SQ, 'Impermeabilização visível', 'Box, sacadas, áreas de serviço: sinais de umidade e caimento'],
        [SQ, 'Compra de usado, além do acima', 'Idade das instalações, reformas sem projeto ou ART, umidade, cobertura acessível, histórico do condomínio'],
        [SQ, 'Documentos', 'Manual do proprietário, termo de garantia, plantas e projetos recebidos'],
    ], 'sm check', widths=['5%', '32%', '63%'])
    corpo = ('<div class="two"><div><h2>Agendamento</h2>' + regras + '</div><div><h3>Confirmação depois do pagamento</h3>' + m1 +
             '<h3>Lembrete da véspera (vistoria)</h3>' + m2 + '</div></div><h2>Checklist de campo</h2>' + chk_v + chk_vi)
    return page('Frente 2 · agendamento e campo', 'Agendamento e checklist de campo', 'Dinheiro antes do campo, pergunta escrita antes da visita e evidência registrada antes de qualquer conclusão.', corpo)

def devolutiva():
    modelo = table(['Bloco da nota técnica (1 página)', 'Exemplo preenchido ' + tag('S')], [
        ['1. Imóvel, data e quem acompanhou', 'Apto 802, Setor Bueno · 10/11/2026 · acompanhou a proprietária'],
        ['2. A pergunta respondida', 'De onde vem a mancha no teto do banheiro social e o que fazer agora?'],
        ['3. O que foi observado', 'Mancha de cerca de 0,6 m² no forro de gesso sob o box do apto 902. Umidade de 38% no gesso junto ao ralo, contra 12% em área seca do mesmo forro (fotos 3 a 6). No 902, rejunte do box com falhas e ralo sem grelha (fotos 7 e 8, com autorização do vizinho).'],
        ['4. O que não foi possível verificar', 'Interior do forro, sem abertura. Prumada de esgoto, sem acesso.'],
        ['5. Causa provável e grau de certeza', 'Infiltração pelo box do apto 902 (rejunte e ralo). Grau: provável.'],
        ['6. O que fazer agora e o que não fazer', 'Pedir ao vizinho a revisão do rejunte e do ralo. Não pintar nem trocar o gesso antes de sanar a origem e medir a secagem.'],
        ['7. Próximo passo recomendado', 'Se o vizinho contestar ou for preciso formalizar: laudo. Se a origem for sanada: reparo do forro depois de 15 dias, com nova medição de umidade.'],
        ['8. Limites e assinatura', 'Avaliação em visita única, com instrumentos simples, das áreas acessíveis. Não é laudo e não serve para apresentar a terceiros. ' + RT + ' · ART nº [número].'],
    ], 'sm', widths=['30%', '70%'])
    laudo = ol(['<b>Identificação:</b> partes, imóvel, finalidade, data da vistoria e ART.', '<b>Pergunta</b> que o laudo responde, nas palavras combinadas na proposta.',
                '<b>Documentos analisados.</b>', '<b>Método:</b> vistoria, instrumentos e referências técnicas aplicáveis (por exemplo, ABNT NBR 13752 para perícias na construção civil).',
                '<b>Constatações:</b> fotos numeradas, medições e croqui.', '<b>Análise:</b> hipóteses consideradas e por que foram aceitas ou descartadas.',
                '<b>Conclusão e limites:</b> o que se pode afirmar e com que grau de certeza.', '<b>Recomendações</b> e investigações complementares, se houver.',
                '<b>Encerramento:</b> data, assinatura, CREA, ART e anexos.'])
    inv = table(['Situação encontrada na visita', 'O que oferecer', 'Quem paga'], [
        ['Mais de uma origem plausível e evidência insuficiente', 'Teste de estanqueidade ou medições em série: laudo ampliado ou hora técnica', 'Cliente'],
        ['É preciso abrir forro ou revestimento', 'Abertura de inspeção por terceiro, com recomposição', 'Cliente, direto ao terceiro'],
        ['Fissura que pode estar ativa', 'Monitoramento por 30 dias e segunda visita', 'Cliente (adicional)'],
        ['Indício estrutural: fissura inclinada em viga ou pilar, deformação, armadura exposta com perda de seção', 'Orientação imediata de segurança; especialista em estruturas e ensaios', 'Proposta específica'],
        ['Aquecimento ou desarme elétrico', 'Profissional habilitado com equipamento; ninguém abre painel energizado sem NR-10', 'Proposta específica'],
        ['A finalidade passou a ser documental', 'Converter em laudo, com a regra de abatimento', 'Cliente'],
        ['Acesso negado à unidade vizinha ou à cobertura', 'Registrar a limitação e reagendar com autorização', '—'],
    ], 'sm', widths=['40%', '42%', '18%'])
    rev = table(['Situação', 'Condição de revisita'], [
        ['Visita Diagnóstica', 'Não inclui revisita. Nova ida por fato novo: R$ 610 em Goiânia, até 1 h no local, com atualização da nota ' + tag('P')],
        ['Laudo', 'Segunda vistoria por hora técnica (R$ 350/h, em teste) mais deslocamento, ou laudo ampliado'],
        ['Vistoria Completa', 'Uma revisita incluída: mesmo imóvel, em até 60 dias, para conferir os itens do relatório, com até metade do tempo de campo e 48 h de aviso'],
        ['Revisita avulsa de vistoria ' + tag('P'), f'Até 100 m²: R$ 450 · 100 a 250 m²: R$ 520 · 250 m² ou mais: R$ 610 (preços que atingem a meta: {brl(REV_MIN["ate100"], True)}, {brl(REV_MIN["meio"], True)} e {brl(REV_MIN["acima"], True)})'],
        ['Completa até 100 m²', f'Só com revisitas agrupadas (3 ou mais unidades no mesmo empreendimento e na mesma janela). Os R$ 240 a mais, depois de 8% e de uma nova ida, deixam {brl(DIF240, True)}: na meta, pagam {DIF240_MIN} minutos do Aruak. Fora disso, Vistoria e revisita avulsa'],
    ], 'sm', widths=['24%', '76%'])
    corpo = ('<h2>Modelo de devolutiva da visita</h2>' + modelo + '<div class="two"><div><h2>Estrutura do laudo</h2>' + laudo + '</div><div><h2>Revisitas</h2>' + rev + '</div></div>'
             '<h2>Critérios para investigação adicional</h2>' + inv)
    return page('Frente 2 · modelos', 'Devolutiva, laudo, investigação e revisita', 'A nota da visita registra limites; o laudo registra método. Nenhuma investigação extra começa sem preço aprovado.', corpo)

def build():
    return com_visita() + com_laudo() + com_vistoria() + ficha() + exemplo() + agenda_checklist() + devolutiva()
