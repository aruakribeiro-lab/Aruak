# -*- coding: utf-8 -*-
from common import *

def comercial():
    blocos = [
        ('O problema', '<p>O projeto está pronto ou quase, mas os orçamentos dos executores não se comparam ou vêm acima do que você pode investir. A decisão trava, ou a obra começa sem saber quanto vai custar.</p>'),
        ('Com o seu arquiteto', '<p>O projeto é do arquiteto. Nenhuma alteração sem a anuência dele, e as incompatibilidades vão por escrito a ele. Não trabalhamos com reserva técnica.</p>'),
        ('Estudo de Viabilidade', '<p>Para quando há decisões em aberto e um teto de investimento. Você recebe 2 ou 3 cenários de acabamento ou de etapas, a faixa de investimento de cada um, os itens que mais pesam, premissas, riscos e a nossa recomendação. Prazo: 7 a 15 dias úteis.</p>'),
        ('Orçamento Executivo com Plano de Obra', '<p>Para quando o projeto e as especificações permitem levantar quantidades. Você recebe quantitativos por etapa, preços com fornecedor identificado, exclusões, cronograma, curva de desembolso, compras críticas e o plano da obra. Prazo: 15 dias úteis em reforma, depois dos documentos completos.</p>'),
        ('O que não está incluído', ul(['Projeto e compatibilização de projetos complementares.', 'Aprovação na prefeitura.', 'Mobiliário solto, que pode vir separado se você pedir.', 'Mudança de projeto depois de iniciado o orçamento, cobrada por hora técnica.'])),
        ('O estudo é seu', '<p>Você pode executar com quem quiser. Se quiser executar com a gente, a proposta de gestão já vem junto, para você decidir com todos os números na mesa.</p>'),
    ]
    preco = ('<table><tr><td>Estudo de Viabilidade (reforma de até cerca de 100 m² ou 3 ambientes)</td><td class="v">R$ 2.500</td></tr>'
             '<tr><td>Orçamento Executivo com Plano de Obra (reforma delimitada)</td><td class="v">R$ 5.000</td></tr>'
             '<tr><td>Áreas maiores e construção de casa</td><td class="v">sob cotação</td></tr></table>'
             '<p>50% na contratação e 50% na apresentação. Uma rodada de ajustes incluída. Preços cotados válidos por 30 dias.</p>')
    prox = '<p>Reunião de 30 a 45 minutos com você e o seu arquiteto. Traga o projeto e a faixa de investimento. Você sai sabendo qual dos dois estudos faz sentido e quanto custa.</p>'
    return client_page('Frente 5 · página comercial', 'Pré-obra: quanto custa o seu projeto',
        'Antes de começar, saiba com preço real de mercado quanto o projeto custa, o que pesa mais, em que ordem executar e o que comprar primeiro.',
        blocos, preco, prox, 'Feito em parceria com o arquiteto autor do projeto.')

def ficha():
    of = table(['', 'Estudo de Viabilidade (EVF)', 'Orçamento Executivo com Plano de Obra'], [
        ['Quando cabe', 'Estudo preliminar aprovado; decisões em aberto; teto de investimento conhecido', 'Projeto executivo, ou desenhos e especificações suficientes para levantar quantidades'],
        ['Pergunta respondida', '“Que versão do projeto cabe na minha verba?”', '“O que vou executar, quanto custa por etapa e o que compro primeiro?”'],
        ['Entrega', 'Cenários com faixa de investimento, itens que mais pesam, premissas, riscos, recomendação e condições da gestão', 'Quantitativos por etapa, preços e fontes, exclusões, cronograma, desembolso, compras críticas, plano de obra e reunião'],
        ['Preço de teste e prazo', 'R$ 2.500 · 7 a 15 dias úteis', 'R$ 5.000 · 15 dias úteis (reforma)'],
        ['Pular para', 'Sem projeto: indicar arquiteto parceiro. Escopo pequeno e definido: Reparo Rápido', 'Projeto que ainda não sustenta quantitativos: viabilidade primeiro'],
    ], 'sm', widths=['16%', '42%', '42%'])
    resp = table(['Papel', 'Pessoa'], [
        ['Abertura com escritórios', 'Aruak; Ivan, se aceitar ' + tag('P')], ['Reunião, levantamento, revisão e apresentação', 'Aruak'],
        ['Quantitativos e cotações', 'Apoio técnico <span class="tg">[pendente de decisão]</span>: orçamentista ou técnico a R$ 60/h, pago na entrega'],
        ['Proposta, cobrança, termo e NF', 'Gabriela'], ['Registro', 'Placar (venda), Painel de Obras (horas), Mais Controle (recebimentos)'],
    ], 'sm', widths=['42%', '58%'])
    horas = table(['Orçamento executivo, com apoio ' + tag('E'), 'Aruak', 'Equipe'], [
        ['Conversa com o arquiteto e qualificação', '1 h', '—'], ['Proposta e fechamento', '1 h', '0,5 h adm'], ['Levantamento no imóvel, com trajeto', '2 h', '—'],
        ['Quantitativos e lista de serviços', '—', '10 h técnico'], ['Cotações (2 fontes nos itens da curva A)', '—', '10 h técnico'],
        ['Revisão técnica, cronograma e plano', '3,5 h', '—'], ['Apresentação e uma rodada de ajuste', '2,5 h', '1,5 h adm'],
        {'cls': 'tot', 'cells': ['Total', '10 h', '20 h técnico + 2 h adm']},
        ['Sem apoio técnico, o Aruak faz tudo', '30 h', '2 h adm'],
        ['Estudo de Viabilidade: com apoio / sem apoio', '6 h / 12 h', '8 h técnico + 1 h adm / 1 h adm'],
    ], 'sm', widths=['56%', '16%', '28%'])
    seq = ol(['O arquiteto apresenta um projeto real travado.', 'Reunião com o proprietário e o arquiteto (roteiro na página seguinte).',
              'Escolha da oferta pelo critério de entrada; proposta de uma página no mesmo dia; 50% na contratação.',
              'Documentos mínimos recebidos (lista na página seguinte). Faltando, registrar premissas ou propor viabilidade.',
              'Levantamento no imóvel; quantitativos; cotações com fornecedor identificado.', 'Revisão técnica do Aruak; cronograma, desembolso e compras críticas.',
              'Apresentação com o arquiteto; uma rodada de ajuste; termo de recebimento; 50% restantes.', 'Retorno em 60 dias: gestão contratada? nova indicação do escritório?'])
    riscos = table(['Risco', 'Tratamento'], [
        ['Projeto incompleto (mais 30% de horas)', 'Premissas escritas; documento faltante muda prazo; hora técnica para mudanças'],
        ['Sem apoio técnico', 'Orçamento cai para ' + brl(ORC_SEM.ph) + '/h: não vender o orçamento sem apoio confirmado'],
        ['Cliente usa o estudo para leiloar executores', 'O estudo é dele e foi pago; a gestão é vendida pelo valor do método'],
        ['Arquiteto pede comissão', 'Eliminatório: sem reserva técnica'],
        ['Preços vencem', 'Validade de 30 dias; atualização cobrada'],
        ['Conflito de autoria', 'Diagnóstico e Soluções por escrito ao arquiteto, nunca direto ao cliente'],
    ], 'sm', widths=['40%', '60%'])
    p1 = page('Frente 5 · ficha interna', 'Pré-obra com Arquitetos · ficha interna', 'O cliente compra planejamento utilizável antes da execução. O arquiteto mantém a autoria e participa da apresentação.',
        '<h2>Duas ofertas separadas</h2>' + of + '<div class="two"><div><h2>Responsáveis</h2>' + resp + '<h2>Riscos</h2>' + riscos + '</div><div><h2>Horas por pessoa</h2>' + horas + '</div></div>'
        '<h2>Sequência de execução e aceite</h2>' + seq + '<p><b>Aceite:</b> apresentação feita com o arquiteto e termo de recebimento assinado. Item que estava no projeto e faltou na planilha é corrigido sem custo.</p>')
    ind = ind_table([
        ('Orçamento R$ 5.000, com apoio técnico', ORC, '0'), ('Orçamento R$ 5.000, Aruak absorve as 20 h técnicas', ORC_SEM, '0'),
        ('Orçamento, projeto incompleto (+30% de horas), com apoio', ORC_ADV, '0'), ('Idem, sem apoio', ORC_ADV_SEM, '0'),
        ('Viabilidade R$ 2.500, com apoio', EVF, '0 (EVF do Cleber: registro histórico)'), ('Viabilidade R$ 2.500, sem apoio', EVF_SEM, '0'),
    ])
    contas = (f'<p class="small">Orçamento: 8% de tributos; R$ 200 de outros diretos (ART de R$ 108,39, uma ida de R$ 50 e R$ 41,61 de impressão e entrega); técnico a R$ 60/h; administrativo a R$ 35/h. '
              f'Com apoio: {brl(ORC.receita)} − {brl(ORC.trib)} − {brl(ORC.ccustos)} = {brl(ORC.disp)} disponíveis; ÷ 10 h = {brl(ORC.ph)}/h; menos 10 h a R$ 100 = saldo de {brl(ORC.saldo)}. '
              f'Sem apoio, o Aruak passa a 30 h pessoais e o saldo cai para {brl(ORC_SEM.saldo)}. Viabilidade: ART e uma ida, 1 h administrativa.</p>')
    crit = table(['Critério até 18/12', 'Como medir', 'Decisão'], [
        ['Venda', 'Estudo pago vindo de um dos dois escritórios', '1 ou mais: seguir. Nenhum: revisar mensagem e oferta antes da rede de janeiro'],
        ['Entrega rentável', 'Disponível por hora medido de R$ 200 ou mais, entrega no prazo, termo assinado', 'Abaixo da meta: apoio técnico, escopo ou preço'],
        ['Segunda indicação', 'O mesmo escritório traz outro cliente em até 60 dias', 'Sim: abrir a rede de 100 a 150 arquitetos em janeiro'],
    ], 'sm', widths=['18%', '44%', '38%'])
    prec = box('Precedentes', '<p><b>Cleber:</b> o Aruak informou a contratação do EVF; o briefing de 29/10 registra R$ 2 mil e entrada recebida, ainda a conciliar com contrato e comprovante ' + tag('A') + '. A faixa de R$ 2 mil a R$ 2,5 mil integra o histórico do EVF; o canal de arquitetos ainda precisa de evidência própria. '
               '<b>BORA:</b> EVFs vendidos entre R$ 3.400 e R$ 5.300 em Brasília, 2022 ' + tag('R') + '.</p>')
    gest = box('Venda da gestão dentro do estudo ' + tag('P'), '<p>O estudo apresenta as condições de uma eventual gestão (honorário mensal, duração, frequência de campo). A venda da gestão só conta no Placar quando houver contrato próprio. O valor do estudo não é abatido da gestão: o ganho do cliente é começar com o planejamento pronto.</p>')
    p2 = page('Frente 5 · ficha interna', 'Pré-obra · dinheiro e critérios', 'Com apoio técnico, o orçamento paga a meta com folga. Sem apoio, não paga.',
        '<h2>Margem: com apoio técnico e com o Aruak absorvendo o trabalho</h2>' + ind + contas +
        '<div class="two"><div><h2>Pagamento e caixa</h2><p>50% na contratação e 50% na apresentação. Antes da segunda parcela saem só a ART e a ida (' + brl(ART1 + IDA, True) + '); o técnico é pago na entrega. O contrato nunca fica negativo.</p>'
        '<h2>Aquisição</h2><p>Arquitetos sem reserva técnica, Scanner (código PRÉ-OBRA) e clientes antigos. O custo de venda está nas horas do Aruak (conversa com o arquiteto e reunião).</p></div><div>' + prec + gest + '</div></div>'
        '<h2>Critério para manter, ajustar ou suspender</h2>' + crit)
    return p1 + p2

def abordagem():
    ganha = ul(['O projeto vira obra construída, que entra no portfólio do escritório.', 'Autoria preservada: incompatibilidades vão por escrito ao arquiteto.',
                'O cliente decide com segurança e não abandona o projeto por causa de orçamento.', 'Sem reserva técnica e sem disputa pelo cliente: a Entre Colunas não faz projeto.'])
    avatar = '<p><b>Avatar:</b> escritório de Goiânia com projetos residenciais de reforma ou construção, que não executa obra ou executa com quem não confia, já teve projeto travado por orçamento e aceita trabalhar sem reserva técnica. <b>Eliminatórios:</b> pede comissão; quer o estudo de graça para fechar o projeto dele; quer que a Entre Colunas altere o projeto.</p>'
    m = msg('''[Nome], boa tarde. Tudo certo por aí?

Estou testando uma coisa com dois escritórios que respeito e pensei em você. Sabe aquele projeto que fica parado porque o cliente recebe orçamentos que não fecham ou que ninguém consegue comparar?

Eu faço o orçamento executivo com preço real de mercado e o plano da obra, junto com você, sem mexer no projeto sem a sua palavra. O cliente paga pelo estudo, você participa da apresentação e não existe reserva técnica no meio.

Você tem algum projeto travado agora em que isso ajudaria? Se tiver, me dá 30 minutos na [dia] ou na [dia] que eu te mostro como seria com um caso real seu.''')
    rot = table(['Tempo', 'Roteiro da reunião com o proprietário e o arquiteto'], [
        ['3 min', '<b>Combinar o fim no começo.</b> “No final, vocês me dizem se faz sentido, se não faz, ou marcamos uma data. Pode ser?”'],
        ['10 a 15 min', '<b>Entender.</b> O que a obra precisa resolver? Até quanto pretendem investir e de onde saiu esse número? Para quando precisam da obra pronta, existe data que não pode passar? Quem decide junto? Qual foi a experiência de vocês com obra até hoje? O que não pode acontecer de jeito nenhum?'],
        ['5 min', '<b>Mostrar</b> a pergunta que o estudo responde e a amostra de entrega. Explicar a diferença entre viabilidade e orçamento executivo.'],
        ['5 min', '<b>Recomendar uma oferta</b>, com o porquê, o preço e o prazo. O defeito antes do “mas”: “Não é gratuito e leva 15 dias úteis, mas vocês começam a obra sabendo o custo de cada etapa.”'],
        ['5 min', '<b>Fechar com passo único.</b> “Faz sentido começarmos? Mando hoje a proposta de uma página e o PIX da entrada.” Sair com sim, não ou data.'],
        ['Depois', 'Resumo escrito no mesmo dia, para o cliente e o arquiteto. Registro no Placar.'],
    ], 'sm', widths=['12%', '88%'])
    docs = table(['Documentos mínimos', 'Estudo de Viabilidade', 'Orçamento Executivo'], [
        ['Arquitetura', 'Estudo preliminar ou anteprojeto: planta baixa e cortes principais', 'Projeto executivo: plantas, cortes, elevações, paginação de pisos, detalhes das áreas molhadas'],
        ['Complementares', 'Não obrigatórios', 'Os disponíveis: elétrico, hidrossanitário e estrutural, quando houver intervenção'],
        ['Especificações', 'Lista de acabamentos pretendidos ou referências', 'Memorial com marcas e modelos; quadros de esquadrias, louças e metais'],
        ['Imóvel', 'Fotos e medidas (reforma); regras do condomínio', 'Acesso para levantamento; regras do condomínio'],
        ['Cliente', 'Teto de investimento e prazo desejado', 'Fornecedores já escolhidos pelo cliente; prazo'],
    ], 'sm', widths=['16%', '40%', '44%'])
    return page('Frente 5 · abordagem', 'Abordagem ao arquiteto, reunião e documentos', 'A conversa começa por um projeto real travado e termina com sim, não ou data.',
        '<div class="two"><div><h2>O que o arquiteto ganha</h2>' + ganha + avatar + '</div><div><h2>Mensagem ao arquiteto (Aruak)</h2>' + m + '</div></div>'
        '<h2>Roteiro da reunião</h2>' + rot + '<h2>Documentos mínimos</h2>' + docs)

def proposta_amostra():
    prop = table(['Proposta · Orçamento Executivo com Plano de Obra ' + tag('S'), ''], [
        ['Sua preocupação', '“Recebemos três orçamentos que não dá para comparar e o mais barato parece incompleto.”'],
        ['A pergunta que vamos responder', 'Quanto custa executar o projeto do escritório [nome], etapa por etapa, e o que precisa ser comprado primeiro?'],
        ['O que você recebe', 'Quantitativos por etapa, preços com fornecedor identificado e exclusões; cronograma; curva de desembolso; compras críticas; plano de obra; reunião de apresentação com o arquiteto; uma rodada de ajuste'],
        ['O que não está incluído', 'Projeto, compatibilização, aprovação na prefeitura, mobiliário solto; mudanças de projeto depois de iniciado o orçamento (hora técnica)'],
        ['Documentos que precisamos', 'Lista mínima da página anterior, até [data]'],
        ['Prazo', '15 dias úteis depois dos documentos completos; apresentação em [data]'],
        ['Investimento', 'R$ 5.000: 50% na contratação e 50% na apresentação. Preços cotados válidos por 30 dias'],
        ['Se executar com a Entre Colunas', 'Condições da gestão apresentadas junto com o orçamento; nenhuma obrigação de contratar'],
        ['Responsável técnico', RT + ', com ART'],
        ['Próximo passo', 'Aceite por escrito e PIX da entrada; levantamento no imóvel em [data]'],
    ], 'sm', widths=['26%', '74%'])
    cen = table(['Amostra de Estudo de Viabilidade ' + tag('S'), 'Essencial', 'Equilibrado (recomendado)', 'Completo'], [
        ['Faixa de investimento', 'R$ 210 a 235 mil', 'R$ 265 a 290 mil', 'R$ 330 a 360 mil'],
        ['O que muda', 'Mantém esquadrias; acabamento padrão', 'Troca esquadrias; marcenaria nos quartos', 'Inclui área gourmet e automação'],
        ['Prazo estimado de obra', '3 meses', '4 meses', '5 meses'],
        ['Gestão, se executar conosco', 'Honorário mensal por 3 meses', 'Honorário mensal por 4 meses', 'Honorário mensal por 5 meses'],
    ], 'sm', widths=['31%', '23%', '23%', '23%'])
    tot = sum(e[1] for e in __import__('s4_gestao').ETAPAS)
    abc = sorted(__import__('s4_gestao').ETAPAS, key=lambda e: -e[1])[:5]
    acum = 0; rows = []
    for e in abc:
        acum += e[1]; rows.append([e[0], brl(e[1]), pct(e[1] / tot), pct(acum / tot)])
    abct = table(['Amostra de Orçamento Executivo: etapas que mais pesam ' + tag('S'), 'Valor', 'Peso', 'Acumulado'], rows, 'sm num', widths=['52%', '16%', '14%', '18%'])
    des = table(['Desembolso do cliente', 'Mês 1', 'Mês 2', 'Mês 3', 'Mês 4', 'Contingência', 'Total'],
                [['Previsto ' + tag('S'), brl(45000), brl(55000), brl(100000), brl(75000), brl(25000), brl(300000)]], 'sm num')
    crit = '<p class="small"><b>Compras críticas da amostra:</b> esquadrias (45 dias de fabricação), marcenaria (30 a 45 dias), marmoraria (20 dias depois da medição), porcelanato sob encomenda (20 dias). Cada uma vira data-limite de decisão no cronograma.</p>'
    return page('Frente 5 · proposta e amostra', 'Proposta paga e amostra de entrega', 'A proposta tem uma página e começa pela preocupação do cliente. A amostra mostra o que ele leva para casa.',
        prop + cen + abct + des + crit)

def teste():
    t = table(['Escritório', 'Arquiteto e contato', 'Projeto travado', 'Proprietário e decisor', 'Oferta', 'Próxima data', 'Status'], [
        ['1 · [nome]', '[nome · telefone]', '[cliente · tipo de obra]', '[nomes]', '[EVF ou orçamento]', '[data]', '[ ]'],
        ['2 · [nome]', '[nome · telefone]', '[cliente · tipo de obra]', '[nomes]', '[EVF ou orçamento]', '[data]', '[ ]'],
    ], 'sm form', widths=['13%', '16%', '17%', '16%', '13%', '12%', '13%'])
    cal = table(['Até', 'Entrega', 'Responsável', 'Evidência'], [
        ['06/11', 'Escolher os 2 escritórios e enviar a mensagem', 'Aruak (Ivan, se aceitar)', 'Placar: 2 oportunidades “Pré-obra” com data'],
        ['13/11', 'Conversa de 30 min com cada arquiteto e 1 projeto real escolhido', 'Aruak', 'Projeto recebido; decisor identificado'],
        ['13/11', 'Apoio técnico definido para quantitativos e cotações', 'Aruak', 'Nome, valor por hora, disponibilidade'],
        ['27/11', 'Reunião com o proprietário de cada projeto', 'Aruak e arquiteto', 'Sim, não ou data no Placar'],
        ['04/12', 'Proposta paga apresentada', 'Aruak e Gabriela', 'Proposta enviada no mesmo dia'],
        ['18/12', 'Pelo menos 1 estudo pago e iniciado', 'Aruak', 'Entrada no Mais Controle'],
        ['Entrega + 60 dias', 'Horas medidas, saldo e segunda indicação', 'Gabriela', 'Painel de Obras e Placar'],
    ], 'sm', widths=['12%', '42%', '20%', '26%'])
    reg = '<p class="small"><b>Registro de cada caso:</b> escritório, arquiteto, projeto, proprietário, decisor, oferta, valor, datas, status, motivo de perda (Placar); horas por pessoa (Painel de Obras); recebimentos e pagamentos ao técnico (Mais Controle).</p>'
    return page('Frente 5 · teste', 'Teste com dois escritórios', 'Pronto para começar: dois escritórios conhecidos, um projeto real de cada e meta proposta de um estudo pago até 18/12. A rede de janeiro só depois do resultado.',
        t + '<h2>Calendário</h2>' + cal + reg)

def build():
    return comercial() + ficha() + abordagem() + proposta_amostra() + teste()
