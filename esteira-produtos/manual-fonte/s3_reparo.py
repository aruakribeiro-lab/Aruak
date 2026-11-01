# -*- coding: utf-8 -*-
from common import *

SQ = '<span class="sq"></span>'

def comercial():
    blocos = [
        ('O problema', '<p>Rejunte escuro que não sai, revestimento datado, metais gastos. Você quer resolver sem quebrar tudo, sem sair de casa e sem uma obra que não termina.</p>'),
        ('Quando cabe', '<p>Um banheiro existente, com o revestimento firme na maior parte, sem vazamento ou infiltração ativa e sem mudança de layout. A visita de medição confirma.</p>'),
        ('O que está incluído', ul(['Visita de medição sem custo, de até 1 hora: medimos o ambiente e testamos o revestimento e a umidade.',
            'Proposta com o sistema especificado pelo fabricante, o aplicador identificado e três datas: início, fim dos trabalhos no local e liberação para uso.',
            'Proteção dos ambientes vizinhos, limpeza final e descarte.', 'Termo de entrega com os cuidados de uso e a garantia do sistema.', 'Engenheiro responsável, com ART.'])),
        ('O que não está incluído', ul(['Demolição, troca de tubulação embutida ou mudança de layout.',
            'Vazamento, infiltração ou mofo ativo: primeiro descobrimos a causa, com a Visita Diagnóstica.',
            'Peças soltas acima de 10% da área: reavaliamos e orçamos; acima de 30%, vira reforma com gestão.', 'Outros ambientes, com proposta própria.'])),
        ('Se aparecer algo escondido', '<p>Paramos aquela parte, fotografamos, mostramos o impacto no preço e na data de uso e só seguimos com a sua autorização por escrito.</p>'),
        ('Como funciona', ol(['Fotos e visita de medição.', 'Proposta apresentada em pessoa.', 'Sinal e compra do material.', 'Execução nas datas combinadas e liberação para uso depois da cura e da verificação.'])),
    ]
    preco = ('<table><tr><td>Preço</td><td class="v">global e fechado, na proposta</td></tr>'
             '<tr><td>Pagamento</td><td class="v">50% · 40% · 10%</td></tr></table>'
             '<p>50% na assinatura, 40% no fim dos trabalhos no local e 10% na liberação para uso. Proposta válida por 15 dias, por causa das cotações.</p>')
    prox = '<p>Mande três fotos do banheiro (geral, piso e parede do box) e marque a visita de medição.</p>'
    return client_page('Frente 3 · página comercial', 'Reparo Rápido de Banheiro',
        'Seu banheiro renovado sem quebradeira, com escopo escrito, preço fechado e as datas de início, de fim dos trabalhos e de volta ao uso definidas na proposta.',
        blocos, preco, prox, 'Reparo Rápido de Cozinha: sob consulta.')

def ficha():
    enq = table(['Condição de enquadramento', 'Como verificar', 'Se não cumprir'], [
        ['Um banheiro existente, sem mudança de layout nem troca de tubulação embutida', 'Visita de medição', 'Reforma por Gestão de Obra'],
        ['Peças soltas até 10% da área de referência (piso mais paredes a revestir)', 'Percussão peça a peça; área das peças com som cavo ÷ área de referência', 'Acima de 10% até 30%: reavaliar e orçar. Acima de 30%: reforma'],
        ['Base dentro do limite de umidade do fabricante', 'Medidor de umidade em grade', 'Visita Diagnóstica antes'],
        ['Sem vazamento, infiltração ou mofo ativo', 'Inspeção, ralos, registros, teto do vizinho de baixo quando possível', 'Visita Diagnóstica antes'],
        ['Condomínio de acordo com horário, elevador e regras', 'Regulamento e comunicação ao síndico (NBR 16280 quando couber)', 'Data só depois da aprovação'],
        ['Data de uso combinada', 'Saber se é o único banheiro da casa', 'Plano alternativo antes de assinar'],
        ['“Demolir e refazer”', '—', '<span class="tg">[pendente de decisão]</span> Fora do preço fechado: cotar depois de avaliação'],
    ], 'sm', widths=['36%', '36%', '28%'])
    resp = table(['Papel', 'Pessoa'], [
        ['Vende, mede e enquadra', 'Aruak'], ['Cotações e suprimentos', '<span class="tg">[pendente de decisão]</span> após a saída do Korran; proposta: Yan cota, Gabriela registra e compra'],
        ['Aplicação', 'Aplicador terceiro, identificado por escrito antes da proposta'], ['Coordenação diária', 'Yan ' + tag('P') + ', se confirmar horas'],
        ['Liberação para uso', 'Aruak'], ['Cobrança e NF', 'Gabriela'], ['Pagamentos e Mais Controle', 'Flávia'],
    ], 'sm', widths=['34%', '66%'])
    horas = table(['Etapa', 'Aruak', 'Equipe'], [
        ['Visita de medição com trajeto', '2,5 h', '—'], ['Enquadramento e proposta', '2 h', '—'], ['Apresentação ao cliente', '1 h', '—'],
        ['Cotações', '—', '3 h técnico'], ['Compra e recebimento do material', '—', '2 h técnico + 2 h adm'],
        ['Início e conferência do material', '1,5 h', '—'], ['Acompanhamento diário', '—', '3 h técnico'],
        ['Verificação intermediária', '1 h', '—'], ['Fim dos trabalhos e liberação', '1,5 h', '—'], ['Pós-entrega em 30 dias', '1 h', '—'],
        {'cls': 'tot', 'cells': ['Total ' + tag('E'), '10,5 h', '8 h técnico + 2 h adm']},
    ], 'sm', widths=['52%', '18%', '30%'])
    seq = ol(['Fotos pelo Scanner ou WhatsApp e visita de medição (até 1 h no local).', 'Ficha de enquadramento preenchida.',
              'Cotações com status: confirmado por escrito, estimado ou impede prometer.',
              'Proposta com composição de custos de até 67% do preço e as três datas.', 'Apresentação em pessoa; assinatura e 50%.',
              'Compra do material só depois do sinal; aprovação do condomínio.', 'Mobilização e proteção; teste final de percussão; preparação da base.',
              'Aplicação conforme a ficha técnica do fabricante, com registro diário e fotos.', 'Fim dos trabalhos no local; 40%.',
              'Cura e verificação: aderência, acabamento, ralos com teste de água, vedação.', 'Termo de liberação para uso; 10%.',
              'Pós-entrega em 30 dias: foto do ambiente em uso e pedido de indicação.'])
    riscos = table(['Risco', 'Tratamento'], [
        ['Aplicador não identificado', 'Impede proposta com preço e data'], ['Umidade ou peças soltas acima do limite', 'Condição oculta ou diagnóstico antes'],
        ['Cura maior que a prevista', 'Data de uso só pela ficha técnica, nunca por estimativa'], ['Único banheiro da casa', 'Plano alternativo combinado antes'],
        ['Material atrasa', 'Início só com material entregue ou data escrita do fornecedor'], ['Garantia do sistema', 'Aplicação conforme o fabricante, com registro'],
        ['Compra antes do sinal', 'Proibida: o dinheiro de um contrato não paga outro'],
    ], 'sm', widths=['42%', '58%'])
    ind = ind_table([('Banheiro do Alexandre, indicação ' + tag('S'), RR, '0'), ('O mesmo, vindo do Scanner (+R$ 35)', RR_S, '0')])
    regra = box('Regra de preço do preço fechado ' + tag('P'),
        f'<p>Todos os custos, inclusive equipe, ART, contingência e aquisição, cabem em até 67% do preço: 8% vão para tributos e 25% ficam preservados para as horas do Aruak, a garantia e o risco. <b>Preço = custos ÷ 0,67.</b> Em R$ 19.400, o teto de custos é {brl(RR_TETO)}. A regra antiga de custo × 1,43 deixaria 22% depois dos tributos.</p>')
    crit = table(['Resultado medido em cada reparo', 'Decisão'], [
        ['Liberação na data prometida, custo até 5% acima do orçado, disponível de R$ 200/h ou mais e nenhum aditivo sem autorização', '<b>Manter</b>; depois de 2 casos medidos, publicar o prazo real'],
        ['Custo de 5% a 15% acima ou liberação até 2 dias depois', '<b>Ajustar</b> composição, contingência ou cronograma'],
        ['Custo mais de 15% acima, liberação mais de 2 dias depois, condição oculta em 2 de 3 casos ou garantia acionada em 90 dias', '<b>Suspender</b> o preço fechado e rever o enquadramento'],
    ], 'sm', widths=['64%', '36%'])
    p1 = page('Frente 3 · ficha interna', 'Reparo Rápido · ficha interna', 'Único preço global fechado da execução. Só sai com sistema especificado, aplicador identificado, três datas e orçamento com contingência.',
        '<h2>Enquadramento</h2>' + enq + '<div class="two"><div><h2>Responsáveis</h2>' + resp + '</div><div><h2>Horas por pessoa</h2>' + horas + '</div></div>'
        '<h2>Sequência de execução</h2>' + seq)
    p2 = page('Frente 3 · ficha interna', 'Reparo Rápido · aceite, riscos e dinheiro', 'O aceite tem duas etapas: fim dos trabalhos no local e liberação para uso.',
        '<h2>Aceite</h2><p><b>Fim dos trabalhos:</b> termo com fotos, sem material ou entulho no imóvel. <b>Liberação para uso:</b> termo assinado pelo cliente, com checklist (aderência por percussão em pontos marcados, ausência de fissuras, caimento e escoamento dos ralos com teste de água, vedação de cantos e metais, limpeza) e os cuidados de uso do fabricante.</p>'
        '<div class="two"><div><h2>Riscos</h2>' + riscos + '</div><div><h2>Pagamento e aquisição</h2><p>50% na assinatura, 40% no fim dos trabalhos no local, 10% na liberação ' + tag('P') + '. O sinal precisa cobrir material, mobilização e ART.</p>'
        '<p>Aquisição: Scanner (código REPARO), catálogo, clientes antigos e arquitetos. A visita de medição gratuita é custo de venda e está nas horas do Aruak.</p></div></div>'
        + regra + '<h2>Margem</h2>' + ind + '<h2>Critério para manter, ajustar ou suspender</h2>' + crit)
    return p1 + p2

def alexandre():
    rows = [
        ['Proposta', 'Enviada em 23/10 ' + tag('A') + '. Aceite, pagamento e entrega não registrados', 'Confirmado por escrito (envio)'],
        ['Valor e escopo da proposta', 'Abrir o arquivo de 23/10 e copiar aqui. Faixa simulada anterior: R$ 18,9 a R$ 20,8 mil ' + tag('E') + '; exemplo deste manual: R$ 19.400 ' + tag('S'), 'Apenas estimado'],
        ['Sistema', 'Microcimento sobre o revestimento existente, conforme o estudo feito ' + tag('A') + '. Ficha técnica do fabricante para área molhada', 'Impede prometer até ter a ficha'],
        ['Aplicador', 'Não localizado', 'Impede prometer'],
        ['Medidas do ambiente', '[piso m² · paredes m² · box] ' + tag('S') + ' 4 m² de piso e 20 m² de parede', 'Medir na visita'],
        ['Peças soltas (% da área de referência)', '[resultado da percussão]', 'Impede preço até medir'],
        ['Umidade da base e do box', '[leituras]', 'Impede preço até medir'],
        ['Vazamento, infiltração ou mofo', '[sim ou não, com foto]', 'Se sim, Visita Diagnóstica antes'],
        ['Único banheiro da casa?', '[perguntar]', 'Define o plano de uso'],
        ['Condomínio e horários', '[regulamento, síndico, elevador]', 'Impede data de início'],
        ['Metais e acessórios no escopo', '[lista com o cliente]', 'Apenas estimado'],
        ['Três datas', 'Nenhuma confirmada', 'Impede prometer'],
        ['Decisor e forma de pagamento', '[quem decide e como prefere pagar]', 'Perguntar antes da apresentação'],
    ]
    fic = table(['Item', 'Registro do caso Alexandre', 'Status'], rows, 'sm', widths=['24%', '52%', '24%'])
    leitura = box('Leitura do caso hoje', '<p>Há proposta enviada, mas sem aplicador, sem ficha técnica do sistema, sem medição de peças soltas e umidade e sem datas. <b>Não dá para garantir preço nem data de uso.</b> Próxima ação: perguntar ao Alexandre o que aconteceu com a proposta; se houver interesse, agendar a visita de medição e cotar sistema e aplicador antes de reapresentar.</p>', 'warn')
    msgA = msg('''Alexandre, boa tarde. Te mandei a proposta do banheiro no dia 23 e queria saber como ficou do seu lado.

Antes de você decidir, quero voltar aí para medir o revestimento e a umidade com calma. Isso me deixa fechar o preço e as datas de início, de fim e de volta ao uso com segurança.

Consigo [dia] às [hora] ou [dia] às [hora]. Algum dos dois funciona para você?''')
    return page('Frente 3 · enquadramento', 'Ficha de enquadramento · banheiro do Alexandre', 'Primeiro caso do Reparo Rápido. Cada item fica em uma de três colunas: confirmado por escrito, apenas estimado ou impede prometer preço ou prazo.',
        fic + leitura + '<h3>Mensagem para retomar o caso (Aruak)</h3>' + msgA +
        '<p class="small">Antes de enviar: conferir no arquivo da proposta o que foi dito sobre valor e prazo. Se a proposta citou “quatro dias”, corrigir na reapresentação para as três datas medidas.</p>')

def custos():
    rows = []
    for d, v, f in RR_ITENS:
        rows.append([d, f, brl(v, True)])
    comp = table(['Item de custo ' + tag('S'), 'Fonte da cotação', 'Valor'], rows, 'sm num l2', widths=['50%', '30%', '20%'],
                 foot=['Total dos custos', 'Teto: ' + brl(RR_TETO), brl(RR.ccustos, True)])
    res = table(['Resultado do exemplo', 'Valor'], [
        ['Preço', brl(RR.receita)], ['(−) Tributos 8%', brl(-RR.trib)], ['(−) Custos', brl(-RR.ccustos, True)],
        {'cls': 'tot', 'cells': ['= Disponível (' + pct(RR.disp / RR.receita) + ' do preço)', brl(RR.disp, True)]},
        ['÷ 10,5 h do Aruak', brl(RR.ph, True)], ['Saldo parcial (Aruak a R$ 100/h)', brl(RR.saldo, True)],
        ['Contingência não usada volta ao saldo na liberação', brl(RR_CONT, True)],
    ], 'num', widths=['70%', '30%'])
    cot = table(['Cotação', 'Especificação mínima', 'Quem cota', 'Propostas', 'Até', 'Status no caso'], [
        ['Sistema de microcimento (material)', 'Ficha técnica para área molhada sobre cerâmica: primer, malha, base, acabamento, selador; garantia do fabricante', 'Suprimentos <span class="tg">[a designar]</span>', '2', '06/11', 'Não cotado'],
        ['Aplicador', 'Experiência no sistema (3 obras com fotos e 1 referência), agenda, preço por m², garantia da aplicação, compromisso com a ficha técnica', 'Aruak e suprimentos', '2', '13/11', '<b>Não localizado</b>'],
        ['Preparação da base e reassentamento', 'Preço por m² para reassentar peças soltas; regularização', 'Suprimentos', '2', '13/11', 'Não cotado'],
        ['Ralos, cantos e impermeabilização', 'Conforme o fabricante do sistema', 'Suprimentos', '1 a 2', '13/11', 'Não cotado'],
        ['Metais e acessórios', 'Modelos definidos com o cliente', 'Gabriela', '2 lojas', '13/11', 'Lista a definir'],
        ['Proteção, limpeza e descarte', 'Lona, papelão, fita, sacos ou caçamba pequena', 'Gabriela', '1', '13/11', 'Estimado'],
        ['Frete', 'Entrega do material com data', 'Gabriela', '2', '13/11', 'Estimado'],
    ], 'sm', widths=['18%', '34%', '14%', '8%', '8%', '18%'])
    return page('Frente 3 · custos e cotações', 'Composição de custos e lista de cotações', 'Exemplo simulado com o preço de R$ 19.400, para treinar a conta. Cada linha é substituída pela cotação real antes da proposta.',
        comp + '<div class="two"><div>' + res + '</div><div>' + box('Como usar a composição', '<p>Somar as cotações reais. Se o total passar do teto, ajustar escopo (por exemplo, metais comprados direto pelo cliente) ou subir o preço: <b>preço = custos ÷ 0,67</b>. Nunca cortar a contingência para caber.</p>') + '</div></div>'
        '<h2>Lista de cotações</h2>' + cot)

def oculta_datas():
    casos = table(['Achado durante a execução', 'O que fazer', 'Efeito'], [
        ['Peças soltas acima de 10% até 30% da área', 'Orçar o reassentamento adicional por m²', 'Aditivo e, em geral, mais um dia'],
        ['Peças soltas acima de 30%', 'Parar e reavaliar como reforma', 'Gestão de Obra ou novo escopo'],
        ['Umidade acima do limite do fabricante', 'Parar; secagem ou Visita Diagnóstica', 'Nova data de início da aplicação'],
        ['Vazamento em tubulação embutida', 'Parar; reparo hidráulico com proposta própria', 'Nova data de uso'],
        ['Reboco oco ou base desagregada', 'Regularização adicional', 'Aditivo e prazo'],
        ['Ralo ou sifão quebrado', 'Troca por preço unitário', 'Aditivo pequeno'],
    ], 'sm', widths=['34%', '38%', '28%'])
    reg = table(['Registro de condição oculta nº __', ''], [
        ['Data, hora e quem encontrou', ''], ['O que foi encontrado e onde (fotos com escala)', ''], ['Por que não era visível na medição', ''],
        ['Impacto no preço (alternativas com valor)', ''], ['Impacto na data de fim e na data de uso', ''],
        ['Decisão do cliente: autorizo a alternativa __ / não autorizo', ''], ['Assinatura ou “autorizo” por WhatsApp, com data', ''],
    ], 'sm form', widths=['55%', '45%'])
    datas = table(['Data prometida', 'Só prometer quando', 'Exemplo ' + tag('S')], [
        ['Início (mobilização)', 'Contrato e 50% recebidos; material entregue ou com data escrita do fornecedor; aplicador com data escrita; condomínio de acordo; plano de uso combinado; enquadramento sem impeditivo', 'Dia 5 depois da assinatura'],
        ['Fim dos trabalhos no local', 'Cronograma diário do aplicador pela ficha técnica (camadas e intervalos), com um dia de folga para a base. Nenhum “até 4 dias” antes de dois casos medidos', 'Dia 12'],
        ['Liberação para uso', 'Fim dos trabalhos + cura indicada pelo fabricante para área molhada + verificação com teste de água + termo assinado', 'Dia 19'],
    ], 'sm', widths=['18%', '62%', '20%'])
    fl = table(['Dia', 'Lançamento', 'Valor', 'Acumulado'], [[str(d), dsc, brl(v, True), brl(a, True)] for d, dsc, v, a in RR_FLUXO], 'sm num l2', widths=['8%', '56%', '18%', '18%'])
    corpo = ('<h2>Condições ocultas</h2><p>Parar a parte afetada, fotografar com escala, registrar o impacto, orçar a alternativa e colher autorização escrita antes de executar. A contingência cobre variações dentro do escopo (perdas, base um pouco pior dentro dos 10%); o que está fora do escopo vira aditivo autorizado.</p>'
             '<div class="two"><div>' + casos + '</div><div>' + reg + '</div></div>'
             '<h2>Critérios para prometer início, fim e liberação</h2>' + datas +
             '<h2>Caixa do contrato ' + tag('S') + '</h2>' + fl +
             f'<p class="small">O menor acumulado é {brl(min(a for _, _, _, a in RR_FLUXO), True)}, no dia 8: o contrato nunca fica negativo se a compra acontecer depois do sinal. No fim, {brl(RR_FINAL, True)} = disponível de {brl(RR.disp, True)} + contingência de {brl(RR_CONT, True)}, que fica reservada até 30 dias depois da liberação.</p>')
    return page('Frente 3 · oculto, datas e caixa', 'Condições ocultas, datas e caixa', 'Três datas separadas e nenhuma execução adicional sem autorização escrita.', corpo)

def build():
    return comercial() + ficha() + alexandre() + custos() + oculta_datas()
