# -*- coding: utf-8 -*-
"""Esteira formulada, itens 1 a 6 (documento interno, mesmo estilo do manual)."""
from common import *
from esteira_calc import *

V = '<span class="pill p-v">Vendido</span>'
T_ = '<span class="pill p-t">Em teste</span>'
N_ = '<span class="pill p-t">Novo</span>'
S_ = '<span class="pill p-c">Sob consulta</span>'
O_ = '<span class="pill p-i">Por oportunidade</span>'
PB = '<span class="pill p-v">Publicado</span>'


def ficha(nome, est, linhas, oferta=None, nota=None):
    t = table(['', ''], [[f'<b>{a}</b>', b] for a, b in linhas], 'sm ficha', widths=['19%', '81%'])
    h = f'<h2>{nome} {est}</h2>' + t
    if nota:
        h += nota
    if oferta:
        h += '<h3>Mensagem de oferta</h3>' + msg(oferta)
    return f'<div class="nb">{h}</div>'


def capa():
    return f'''<section class="cover" style="height:auto">
<div class="band"><div class="brand">ENTRE COLUNAS · ENGENHARIA DE PREVISIBILIDADE</div>
<h1>A esteira formulada, do item 1 ao 6</h1>
<p class="lead">Cada produto da esteira com público, promessa, entrega, preço, prazo, jornada, perguntas de qualificação e mensagem pronta. Documento de trabalho para a equipe, no novo posicionamento: a Entre Colunas é gestora e fiscal do cliente, não executora.</p>
<p class="lead" style="margin-top:6mm;font-size:9.5pt">Versão 1.0 · 03/11/2026 · Goiânia · circulação interna</p></div>
<div class="meta">
{table(['Item', 'O que é', 'Produtos'], [
        ['1 · Porta de entrada', 'Grátis. Qualifica e leva ao WhatsApp', 'Scanner da Obra, Dossiê do Prédio, Assistente da Obra, atendimento qualificado'],
        ['2 · Diagnóstico', 'Pago, valor menor. Ajuda a decidir', 'Visita Diagnóstica, Conferência da Medição'],
        ['3 · Laudos e documentos', 'Documento para terceiros. Custo é hora técnica', 'Laudo técnico, Vistoria de recebimento, Vistoria antes da compra, Segurança do trabalho, Regularização, Perícia e assistência técnica, EIV e EIT'],
        ['4 · Obras', 'O problema resolvido no imóvel', 'Estudo de Viabilidade Financeira, Orçamento Executivo, Plano para Terminar, Reparo Rápido, Gestão e fiscalização'],
        ['5 · Parcerias', 'Quem indica e recebe comissão', 'Arquitetos, Corretores'],
        ['6 · Recorrência', 'Mensalidade fixa, usando ou não', 'Engenheiro do Condomínio, da Escola e da Empresa'],
    ], 'sm', widths=['20%', '30%', '50%'])}
<p class="small">Marcas: {tag('P')} proposta deste documento, vale até o Aruak confirmar ou mudar · {tag('D')} decisão do Aruak · {tag('E')} estimado, a medir. Premissas do manual: tributos de 8%, meta de R$ 200 disponíveis por hora do Aruak, técnico a R$ 60/h, administrativo a R$ 35/h, R$ 50 por ida, ART de R$ 108,39 até R$ 15 mil.</p>
<p class="small">{RT} · {CONTATO}</p>
</div></section>'''


def regras():
    imp = table(['Produto', 'Comissão', 'Ganho por hora sem comissão', 'Com comissão'], [
        ['Laudo R$ 3.000', '15%', brl(L3000.ph, True), brl(com(L3000, .15).ph, True)],
        ['Vistoria 100 a 250 m² R$ 1.150', '10% · 15%', brl(VI['meio'][0].ph, True), brl(com(VI['meio'][0], .10).ph, True) + ' · ' + brl(com(VI['meio'][0], .15).ph, True)],
        ['Regularização R$ 5.000', '10%', brl(REG.ph, True), brl(com(REG, .10).ph, True)],
        ['Orçamento Executivo R$ 5.000', '10%', brl(ORC.ph, True), brl(com(ORC, .10).ph, True)],
        ['Gestão, mês de R$ 12.350', '4%', brl(G_MES_A.ph, True), brl(com(G_MES_A, .04).ph, True)],
        ['Fiscalização R$ 3.500/mês', '4%', brl(FISC.ph, True), brl(com(FISC, .04).ph, True)],
    ], 'sm num', widths=['40%', '16%', '22%', '22%'])

    pos = table(['Antes', 'Agora ' + tag('D')], [
        ['Construtora Entre Colunas', 'Entre Colunas Engenharia de Previsibilidade'],
        ['Administração de obra: a empresa executa e responde por tudo', 'Gestão e fiscalização: a empresa fica do lado do cliente e confere'],
        ['Concorre com engenheiros e empreiteiros', 'Não concorre: o executor mantém a obra e a responsabilidade pela execução'],
        ['Taxa de administração de 10%, que vira prejuízo no primeiro erro', 'Honorário mensal fixo pela frequência de campo'],
    ], 'sm', widths=['50%', '50%'])
    resp = box('Responsabilidade: a frase certa ' + tag('P'), '<p>“Não somos responsáveis pela execução; respondemos pela fiscalização.” Quem executa responde pela execução, com a ART de execução dele. A Entre Colunas registra ART da fiscalização ou do gerenciamento e responde pelo serviço que presta: conferir, medir, registrar e alertar. Evitar dizer ao cliente que “nada recai sobre a empresa”. O contrato com essa divisão passa pela revisão do Vicente.</p>')
    trans = box('Transição das obras atuais ' + tag('P'), '<p>As obras em andamento no modelo antigo (Victor, João e Alex) terminam como estão, já com empreita fechada e contrato para todos os prestadores. Todo contrato novo sai no modelo de gestor. Assim a equipe não recebe dois discursos ao mesmo tempo.</p>', 'warn')
    com_ = table(['Venda indicada por parceiro', 'Comissão', 'Base de cálculo ' + tag('P')], [
        ['Obra fechada (Gestão e fiscalização, Plano para Terminar)', '4% ' + tag('D'), 'Valor que a Entre Colunas recebe no contrato (honorários), não o valor total da obra'],
        ['Laudos', '10% a 15% ' + tag('D'), 'Valor do laudo'],
        ['Vistorias de recebimento e de compra', '10% a 15% ' + tag('D') + ', recomendado 10%', 'Valor da vistoria. A 15%, a vistoria média cai para ' + brl(com(VI['meio'][0], .15).ph, True) + '/h'],
        ['Estudos (Viabilidade, Orçamento), Regularização, Segurança do trabalho', '10% ' + tag('P'), 'Valor do serviço'],
    ], 'sm', widths=['42%', '22%', '36%'])
    pag = '<p class="small">A comissão pode virar <b>desconto para o cliente</b> ou <b>pagamento ao profissional</b>, conforme o acordo entre os técnicos envolvidos ' + tag('D') + '. Paga depois que o cliente pagar, sobre o valor efetivamente recebido, com recibo ou nota do parceiro. Registro no Placar: parceiro, venda, valor, comissão, data de pagamento ' + tag('P') + '.</p>'
    return page('Regras gerais', 'Posicionamento, responsabilidade e comissões',
        'O que vale para todos os itens da esteira.',
        '<div class="two"><div><h2>O novo posicionamento</h2>' + pos + resp + '</div><div>' + trans +
        '<h2>Comissões de parceiros</h2>' + com_ + pag + '</div></div><h2>Quanto a comissão custa</h2>' + imp + '<p class="small">Meta: R$ 200 disponíveis por hora do Aruak. Comissão calculada sobre o preço de tabela. A vistoria até 100 m² já fica abaixo da meta sem comissão (' + brl(VI['ate100'][0].ph, True) + '/h): vender agrupada por prédio.</p>')


def item1():
    codes = table(['Código', 'De onde vem', 'Produto a oferecer', 'Primeira resposta'], [
        ['SCN-VERMELHO', 'Perigo marcado na porta do problema', 'Segurança primeiro; depois Visita Diagnóstica com prioridade', 'Em até 15 min no horário comercial'],
        ['SCN-DIAGNOSTICO', 'Problema sem causa clara', 'Visita Diagnóstica', 'Mesmo dia útil'],
        ['SCN-LAUDO', 'Documentar para terceiros, disputa, defeito em imóvel novo', 'Conversa de 15 min e Laudo', 'Mesmo dia útil'],
        ['SCN-REPARO', 'Reparo definido, banheiro ou cozinha', 'Visita de medição do Reparo Rápido', 'Mesmo dia útil'],
        ['SCN-VISTORIA', 'Imóvel novo para receber', 'Vistoria de recebimento', 'Em até 2 h úteis (data de chaves)'],
        ['SCN-COMPRA', 'Imóvel usado para comprar', 'Vistoria antes da compra e, se preciso, Regularização', 'Em até 2 h úteis'],
        ['SCN-PREOBRA', 'Vou começar uma obra', 'Arquiteto parceiro, Viabilidade ou Orçamento Executivo', 'Mesmo dia útil'],
        ['SCN-OBRA', 'Raio-X da obra em andamento', 'Conferência da Medição, Plano para Terminar ou Gestão e fiscalização', 'Mesmo dia útil; em até 2 h se houver pagamento em até 5 dias'],
        ['SCN-SINDICO', 'Cuido de um prédio', 'Dossiê do Prédio e Engenheiro do Condomínio', 'Mesmo dia útil'],
    ], 'sm', widths=['15%', '29%', '34%', '22%'])
    fluxo = ol(['O cliente faz o Scanner e chega ao WhatsApp com o código e as respostas.',
                'A atendente responde no prazo da tabela, com a mensagem do código, e faz no máximo duas perguntas que faltam.',
                'Dúvida técnica do cliente: a atendente envia o link do <b>Assistente da Obra</b> (link externo).',
                'Dúvida sobre proposta, valor ou condição: a atendente consulta a <b>Tabela rápida</b> deste documento (link interno) e responde na hora.',
                'Toda conversa termina com sim, não ou data. Registro no Placar: código, produto oferecido, próximo passo e data.'])
    scanner = ficha('Scanner da Obra', PB, [
        ['Para quem', 'Qualquer pessoa com um problema no imóvel, uma obra em andamento, uma obra para começar, um imóvel para receber ou comprar, ou um prédio para cuidar.'],
        ['Promessa', '“Em poucos minutos, entenda o que fazer e qual é o próximo passo, sem compromisso.”'],
        ['Como funciona', 'Perguntas guiadas, uma por vez. O resultado mostra a orientação, a jornada do cliente e abre o WhatsApp com a mensagem pronta e o código.'],
        ['Portas', 'Apareceu um problema (8 perguntas) · Raio-X da obra em andamento (5 telas) · Vou começar uma obra · Vou receber ou comprar um imóvel · Cuido de um prédio.'],
        ['Onde divulgar', 'Status e catálogo do WhatsApp, Instagram, assinatura das mensagens da equipe, cartão na obra, envio pelos parceiros.'],
        ['Pendente', 'Liberar o link no menu Compartilhar da página; trocar o número quando o WhatsApp novo existir.'],
        ['Indicadores', 'Scanners por semana, por código; contatos que viram conversa; vendas por código; custo por cliente pago.'],
    ])
    dossie = ficha('Dossiê do Prédio', T_, [
        ['Para quem', 'Síndico ou administrador que chega pelo Scanner (SCN-SINDICO) ou por indicação.'],
        ['Promessa', '“O que a lei e as normas pedem do seu prédio e o que precisa ser confirmado nos documentos.”'],
        ['Entrega', 'Lista de obrigações do prédio, vencimentos conhecidos e pontos a confirmar, em uma conversa com o engenheiro.'],
        ['Preço', 'Grátis. É a porta do Engenheiro do Condomínio (item 6).'],
    ])
    assist = ficha('Assistente da Obra (link externo)', N_, [
        ['O que é', 'Chat de IA com as instruções da Entre Colunas, para o cliente tirar dúvidas técnicas gerais a qualquer hora, sem gastar o tempo da equipe.'],
        ['Regras', 'Não dá diagnóstico, não promete prazo nem preço fora da tabela, manda ligar 193 em caso de perigo e termina montando o resumo para o WhatsApp.'],
        ['Pendente', 'Criar o GPT com o arquivo de instruções já pronto (pasta do Scanner) e enviar o link para colocar no Scanner.'],
    ])
    return (page('Item 1 · Porta de entrada', 'Item 1 · Porta de entrada (grátis)',
        'Qualifica sem consumir o engenheiro e leva o cliente ao WhatsApp sabendo o que quer.',
        '<div class="two-flow"><div>' + scanner + dossie + '</div><div>' + assist +
        '<h2>Fluxo do atendimento no WhatsApp</h2>' + fluxo +
        box('Número novo ' + tag('D'), '<p>WhatsApp Business com verificação da Meta, para volume alto de contatos sem risco de bloqueio. A atendente faz atendimento ativo: responde na hora, cobra retorno e não deixa conversa sem próximo passo.</p>') +
        '</div></div>')
        + mensagens1(codes))


def mensagens1(codes):
    M = [
        ('SCN-VERMELHO', '''[Nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu Scanner e vi que você marcou um sinal de perigo.

Antes de qualquer coisa: as pessoas já estão longe do local? Se houver fumaça, estalos ou algo caindo, ligue agora para os Bombeiros, no 193.

Assim que estiver seguro, me manda duas fotos de longe. O Aruak, nosso engenheiro, olha hoje e te diz o próximo passo.'''),
        ('SCN-DIAGNOSTICO', '''[Nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu Scanner sobre [problema] em [onde].

Pelo que você contou, o caminho é descobrir a causa antes de gastar com conserto, senão o problema tende a voltar.

Na Visita Diagnóstica o Aruak vai ao imóvel, mede, fotografa e te entrega por escrito o que foi observado e o que fazer. O investimento é de R$ 1.200.

Tenho [dia] às [hora] ou [dia] às [hora]. Qual fica melhor para você?'''),
        ('SCN-LAUDO', '''[Nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu Scanner e vi que você precisa de um documento para [construtora, condomínio, seguradora].

Antes de passar valor, o Aruak faz uma conversa de 15 minutos com você para definir o que o laudo precisa responder e para quem. Assim a proposta já sai certa.

Pode ser hoje às [hora] ou amanhã às [hora]?'''),
        ('SCN-REPARO', '''[Nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu Scanner sobre o [banheiro, cozinha].

Para fechar preço e as três datas, de início, de fim e de volta ao uso, a gente precisa ver e medir. A visita de medição é sem custo e leva até 1 hora.

Fica bom [dia] às [hora]?'''),
        ('SCN-VISTORIA', '''[Nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu Scanner sobre o imóvel do [empreendimento].

Para um imóvel de [metragem] m², a vistoria de recebimento fica em [valor da faixa], com relatório fotográfico e ART em até 2 dias úteis.

O ideal é fazer antes de você assinar o recebimento das chaves. Qual é a data marcada pela construtora?'''),
        ('SCN-COMPRA', '''[Nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu Scanner sobre a [casa, apartamento] que você está pensando em comprar.

Para [metragem] m², a vistoria antes da compra fica em [valor da faixa]. Você recebe por escrito o que precisa de reparo, para negociar com informação.

Você comentou que [houve reforma do dono anterior]. Vale pedir a matrícula atualizada, que a gente confere junto se a área construída bate.

Quando está prevista a assinatura?'''),
        ('SCN-PREOBRA', '''[Nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu Scanner sobre a [obra].

Pelo que você contou, o próximo passo é [o projeto com um arquiteto / saber se o projeto cabe na verba / o orçamento executivo].

O Aruak conversa com você e com o seu arquiteto por 30 a 45 minutos e já sai dali dizendo qual estudo faz sentido e quanto custa.

Qual dia da semana fica melhor para vocês dois?'''),
        ('SCN-OBRA', '''[Nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu Raio-X da obra, obrigada por mandar os números.

Pelo que você informou, [o ponto de atenção do Raio-X, em uma frase].

O Aruak pode conversar com você por 20 minutos para entender a obra e dizer o que faz sentido fazer antes do próximo pagamento.

Você prefere hoje às [hora] ou amanhã às [hora]?'''),
        ('SCN-SINDICO', '''[Nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu Scanner sobre o [condomínio].

O primeiro passo é o Dossiê do Prédio, que é gratuito: a gente levanta o que a lei e as normas pedem do seu prédio e o que precisa ser confirmado nos documentos.

Para começar, me passa o número de unidades e a idade aproximada do prédio?'''),
    ]
    col = lambda L: ''.join(f'<h3>{c}</h3>' + msg(t) for c, t in L)
    return (page('Item 1 · Porta de entrada', 'Códigos do Scanner e primeira resposta',
        'O que oferecer para cada código, em quanto tempo responder e a mensagem da atendente, no padrão do Aruak: parágrafos curtos com linha em branco entre eles, sem travessão e com o próximo passo no fim.',
        codes + '<div class="two-flow"><div>' + col(M[:2]) + '</div><div>' + col(M[2:4]) + '</div></div>')
        + page('Item 1 · Porta de entrada', 'Primeira resposta por código (continuação)', '',
        '<div class="two-flow"><div>' + col(M[4:7]) + '</div><div>' + col(M[7:]) + '</div></div>'))


def item2():
    vd = ficha('Visita Diagnóstica', T_, [
        ['Para quem', 'Quem tem um problema sem causa clara: infiltração, trinca, umidade, piso soltando, problema que voltou depois do conserto.'],
        ['Promessa', '“Descubra a causa antes de gastar com conserto.”'],
        ['Entrega', 'Visita do engenheiro, medições e fotos, e nota técnica por escrito com o que foi observado, a causa provável quando houver evidência e o que fazer agora.'],
        ['Não inclui', 'Ensaios destrutivos, laudo com ART para terceiros, orçamento de reparo.'],
        ['Preço e prazo', f'R$ 1.200 · nota em até 2 dias úteis · pagamento antes do agendamento · {brl(V1200.ph, True)}/h ' + tag('E')],
        ['Jornada', 'Scanner → Visita Diagnóstica → Laudo (se precisar mostrar a alguém) ou Reparo → conferência depois do reparo.'],
        ['Qualificar', 'O que apareceu e onde? Desde quando? Voltou depois de algum conserto? Vai precisar mostrar a alguém?'],
        ['Próximo degrau', 'Laudo (item 3), Reparo Rápido ou Gestão e fiscalização (item 4).'],
    ])
    cm = ficha('Conferência da Medição', N_, [
        ['Para quem', 'Quem está no meio da obra e tem uma parcela para pagar sem saber se ela corresponde ao que foi feito.'],
        ['Promessa', '“Antes de pagar, saiba se o valor bate com o que foi executado.”'],
        ['Entrega', 'Leitura do contrato, do orçamento e da última medição; conferência na obra, serviço por serviço; nota com o que confere, o que diverge e o que pedir à equipe; devolutiva de 30 minutos.'],
        ['Preço e prazo', f'R$ 1.800 ' + tag('P') + f' · visita em até 3 dias úteis e nota em até 2 · pagamento antes do agendamento · {brl(CM_S.ph, True)}/h ' + tag('E')],
        ['Regra', 'Só vender com a parcela vencendo em 4 dias úteis ou mais. Antes disso: pagar só o que está medido e comprovado, ou combinar nova data.'],
        ['Jornada', 'Raio-X → Conferência da Medição → Plano para Terminar (R$ 3.900 em até 30 dias) → Gestão e fiscalização.'],
        ['Qualificar', 'Qual é o próximo pagamento, de quanto e para quando? O que existe por escrito? Quem conferiu a última medição?'],
    ])
    return page('Item 2 · Diagnóstico', 'Item 2 · Diagnóstico (pago, valor menor)',
        'O cliente paga pouco para decidir com segurança. É o degrau que mais leva aos itens 3 e 4.',
        '<div class="two-flow"><div>' + vd + '</div><div>' + cm + '</div></div>')


def item3():
    laudo = ficha('Laudo técnico', V, [
        ['Para quem', 'Quem precisa de um documento para construtora, condomínio, seguradora, vizinho ou processo.'],
        ['Entrega', 'Pergunta a responder, método, evidências, conclusão possível e limites, assinado pelo engenheiro, com ART.'],
        ['Preço', f'A partir de R$ 3.000 · conversa de 15 minutos antes da proposta · {brl(L3000.ph, True)}/h ' + tag('E')],
        ['Qualificar', 'Para quem é o documento? Até quando? Já existe processo ou perito nomeado? (Se sim, é assistência técnica.)'],
    ])
    vist = ficha('Vistoria de recebimento e Vistoria antes da compra', V, [
        ['Recebimento', 'Imóvel novo, antes de assinar o recebimento das chaves. Checklist de pisos, revestimentos, portas, janelas, instalações, caimentos, prumo, nível e medidas. Relatório fotográfico com ART para a construtora corrigir.'],
        ['Antes da compra', 'Imóvel usado, antes de assinar. Infiltrações, trincas, umidade, telhado, instalações e sinais de reforma sem regularização. O que precisa de reparo, por escrito, para negociar.'],
        ['Preço', table(['Área privativa', 'Vistoria', 'Completa (com revisita)'], [['Até 100 m²', 'R$ 840', 'R$ 1.080'], ['100 a 250 m²', 'R$ 1.150', 'R$ 1.500'], ['250 m² ou mais', 'R$ 1.400', 'R$ 1.950']], 'sm num')],
        ['Prazo', 'Relatório em até 2 dias úteis · pagamento na confirmação do agendamento · revisita da Completa em até 60 dias.'],
    ])
    sst = ficha('Segurança do trabalho: PGR, LTCAT e PCMSO', N_, [
        ['Para quem', 'Empresas, escolas e obras que precisam cumprir as normas regulamentadoras. Na obra, a NR-18 exige o PGR do canteiro.'],
        ['PGR (NR-1)', f'Programa de Gerenciamento de Riscos: inventário de riscos e plano de ação. {brl(PGR.receita)} para até 20 funcionários e uma unidade ' + tag('P') + f' · {brl(PGR.ph, True)}/h ' + tag('E')],
        ['LTCAT', f'Laudo das condições ambientais do trabalho, com medições. {brl(LTCAT.receita)} até 20 funcionários ' + tag('P') + f' · {brl(LTCAT.ph, True)}/h. Exige equipamento de medição (alugado ou próprio).'],
        ['Pacote', f'PGR + LTCAT: {brl(SST_PAC.receita)} ' + tag('P') + f' · {brl(SST_PAC.ph, True)}/h'],
        ['PCMSO (NR-7)', 'Feito e assinado por médico do trabalho parceiro, que cobra direto do cliente. A Entre Colunas apresenta o pacote completo.'],
        ['Antes de vender', 'Confirmar o registro da especialização em segurança do trabalho no CREA-GO e o médico parceiro.'],
        ['Próximo degrau', 'Engenheiro da Empresa (item 6), com a revisão do PGR dentro da mensalidade.'],
    ], nota='<p class="small">Preços calculados pelas horas e pela meta; as referências públicas são de licitações. Confirmar com 2 ou 3 cotações em Goiânia.</p>')
    reg = ficha('Regularização de imóveis', N_, [
        ['Para quem', 'Dono ou comprador de imóvel com área construída sem registro na prefeitura ou na matrícula. É o serviço que mais destrava a venda para o corretor.'],
        ['Etapa 1', f'Diagnóstico de regularização: matrícula, cadastro na prefeitura, vistoria e caminho possível. {brl(REG_DIAG.receita)} ' + tag('P') + ', abatido se contratar a etapa 2.'],
        ['Etapa 2', f'Regularização completa até 150 m²: levantamento, as built, projeto para aprovação, ART, protocolo e acompanhamento até o alvará. {brl(REG.receita)} ' + tag('P') + ' · acima de 150 m², sob cotação. Taxas da prefeitura e do cartório por conta do cliente.'],
        ['Base', 'Alvará de Regularização (LC 314/2018) e averbação no cartório são etapas separadas.'],
    ])
    per = ficha('Perícia e assistência técnica', O_, [
        ['Para quem', 'Quem está em processo judicial ou arbitragem envolvendo obra ou imóvel. Perícia judicial é nomeação do juiz; o que se vende é a assistência técnica para uma das partes.'],
        ['Entrega e preço', f'Análise do processo e quesitos · acompanhamento da perícia · parecer técnico. {brl(ASSIST.receita)} em três etapas (R$ 2.000 + R$ 1.500 + R$ 2.500) ' + tag('P') + f' · {brl(ASSIST.ph, True)}/h ' + tag('E')],
    ])
    eiv = ficha('EIV e EIT', O_, [
        ['O que são', 'Estudo de Impacto de Vizinhança e Estudo de Impacto de Trânsito, exigidos pela prefeitura para certos empreendimentos. Em Goiânia, o EIV segue a Lei 11.127/2024 e o Plano Diretor (LC 349/2022).'],
        ['Oferta', f'Análise de enquadramento: {brl(EIV_ENQ.receita)} ' + tag('P') + ', abatida no estudo. O estudo é sob cotação, pelo porte do empreendimento.'],
    ])
    sub = ('O cliente compra um documento para mostrar a alguém. O custo é quase só hora técnica, por isso a margem é a mais alta da esteira, mas não é 100%: um laudo de R$ 3.000 deixa cerca de '
           + brl(r2(L3000.receita - L3000.trib - L3000.ccustos)) + ' antes das horas do engenheiro.')
    return (page('Item 3 · Laudos e documentos', 'Item 3 · Laudos, vistorias e segurança do trabalho', sub,
        '<div class="two-flow"><div>' + laudo + vist + '</div><div>' + sst + '</div></div>')
        + page('Item 3 · Laudos e documentos', 'Item 3 · Regularização, assistência técnica, EIV e EIT',
        'Os braços que dependem de prefeitura, cartório ou processo. Regularização sobe de importância com os corretores.',
        '<div class="two-flow"><div>' + reg + '</div><div>' + per + eiv + '</div></div>'))


def item4():
    evf = ficha('Estudo de Viabilidade Financeira', T_, [
        ['Para quem', 'Quem tem projeto em andamento e um teto de investimento, e precisa saber se o projeto cabe na verba.'],
        ['Entrega', '2 ou 3 cenários de acabamento ou de etapas, faixa de investimento de cada um, itens que mais pesam, riscos e recomendação.'],
        ['Preço e prazo', f'R$ 2.500 · 7 a 15 dias úteis · 50% na contratação e 50% na apresentação · {brl(EVF.ph, True)}/h com apoio técnico'],
    ])
    oe = ficha('Orçamento Executivo com Plano de Obra', T_, [
        ['Para quem', 'Quem tem projeto pronto e quer contratar com preço real, ou recebeu orçamentos que não se comparam.'],
        ['Entrega', 'Quantitativos por etapa, preços com fornecedor, exclusões, cronograma, desembolso mês a mês, compras críticas e plano da obra.'],
        ['Preço e prazo', f'R$ 5.000 · 15 dias úteis em reforma · 50% e 50% · {brl(ORC.ph, True)}/h com apoio técnico. Sem apoio técnico, não vender.'],
    ])
    pt_ = ficha('Plano para Terminar a Obra', N_, [
        ['Para quem', 'Obra em andamento, lenta, parada ou com dinheiro que não fecha.'],
        ['Entrega', 'Registro da situação, conciliação do pago com o executado, saldo de serviços, orçamento para terminar, sequência e cronograma até a mudança, plano de caixa e regra de medição para a equipe atual.'],
        ['Preço e prazo', f'R$ 4.500 com documentos, R$ 5.500 sem, R$ 3.900 depois da Conferência ' + tag('P') + ' · 10 dias úteis · documento próprio com todos os detalhes.'],
    ])
    rr = ficha('Reparo Rápido', S_, [
        ['Para quem', 'Banheiro ou cozinha para renovar, em ambiente único, sem quebradeira desnecessária.'],
        ['Entrega', 'Preço fechado e três datas por escrito: início, fim dos trabalhos e volta ao uso.'],
        ['Regra', 'Se aparecer vazamento, infiltração ou trinca ativa, a causa vem antes (Visita Diagnóstica). Visita de medição sem custo, até 1 hora.'],
    ])
    gf = ficha('Gestão e fiscalização de obra', S_, [
        ['Para quem', 'Dono de obra com projeto, verba e decisão, que quer alguém do seu lado sem trocar a equipe que já tem, quando ela é boa.'],
        ['Promessa', '“Você mantém a sua equipe e o seu dinheiro. A gente fica do seu lado para que cada etapa seja conferida antes de você pagar.”'],
        ['Fiscalização ' + tag('P'), f'1 visita por semana, medição antes de cada pagamento, relatório semanal com fotos, registro de pendências e conferência do material entregue. {brl(FISC.receita)}/mês · {brl(FISC.ph, True)}/h ' + tag('E')],
        ['Gestão e fiscalização', f'Fiscalização mais planejamento, cronograma, cotações com 2 ou 3 propostas em nome do cliente (ele paga direto ao fornecedor), reunião semanal e fechamento financeiro mensal. Honorário mensal fixo, a partir de R$ 7.400 para a equipe padrão; exemplo de {brl(G_MENSAL)}/mês numa obra de R$ 300 mil em 4 meses.'],
        ['Não faz', 'Não executa, não recebe o dinheiro da obra, não compra com dinheiro próprio, não altera o projeto sem o arquiteto.'],
        ['Responsabilidade', 'A execução é do executor, com a ART dele. A Entre Colunas tem ART de fiscalização e responde por conferir, medir, registrar e alertar.'],
        ['Pré-requisito', 'Planejamento antes: Orçamento Executivo, Plano para Terminar ou o primeiro mês cobrindo o planejamento.'],
    ])
    return page('Item 4 · Obras', 'Item 4 · Obras',
        'O cliente compra o problema resolvido no imóvel. Os braços seguem a situação dele: vai começar, já começou, obra pequena ou quer alguém conduzindo.',
        '<div class="two-flow"><div>' + evf + oe + pt_ + rr + '</div><div>' + gf +
        box('Por que o modelo de gestor', '<p>A taxa de 10% de administração não se pagava: qualquer erro saía do lucro, como os 8 rolos de fio sumidos no WTC, e o engenheiro responsável por tudo ganhava menos que o pedreiro. Como fiscal, o honorário paga o trabalho de conferir e o risco da execução fica com quem executa. E o retrabalho, que nasce dos itens que começam sem valor ou definição fechada, é resolvido antes, no Orçamento Executivo ou no Plano para Terminar.</p>') +
        '</div></div>')


def item5():
    arq = ficha('Arquitetos', T_, [
        ['O que ganha', 'O projeto vira obra construída e entra no portfólio. A autoria é preservada. O cliente não abandona o projeto por causa do orçamento. A Entre Colunas não faz projeto, então não disputa o cliente.'],
        ['O que traz', 'Estudo de Viabilidade Financeira, Orçamento Executivo, Gestão e fiscalização, Visita Diagnóstica.'],
        ['Comissão', '4% sobre obra fechada; 10% nos estudos ' + tag('P') + '. Desconto ao cliente ou pagamento ao arquiteto, como combinarem.'],
        ['Avatar', 'Escritório de Goiânia com projetos residenciais de reforma ou construção, que não executa obra ou executa com quem não confia, e já teve projeto travado por orçamento.'],
        ['Eliminatórios', 'Quer o estudo de graça para fechar o projeto dele; quer que a Entre Colunas altere o projeto.'],
        ['Teste', '2 escritórios conhecidos, 1 projeto real de cada, 1 estudo pago até 18/12. Se o mesmo escritório trouxer um segundo cliente em 60 dias, abrir a rede de arquitetos em janeiro.'],
    ], oferta='''[Nome], boa tarde. Tudo certo por aí?

Estou abrindo uma parceria com poucos escritórios e pensei em você. Sabe aquele projeto que trava porque o cliente recebe orçamentos que não fecham ou que ninguém consegue comparar?

Eu faço o estudo de viabilidade ou o orçamento executivo com preço real e, se o cliente quiser, fico do lado dele na obra como fiscal, sem mexer no projeto sem a sua palavra. Cada indicação que vira contrato tem a sua participação, combinada por escrito entre a gente.

Você tem algum projeto travado agora? Se tiver, me dá 30 minutos na [dia] ou na [dia] que eu te mostro com um caso real seu.''')
    cor = ficha('Corretores', N_, [
        ['O que ganha', 'A venda não trava: imóvel regularizado, vistoria antes da compra que dá segurança ao comprador e menos desistência na hora de assinar.'],
        ['O que traz', 'Vistoria antes da compra, Regularização, Laudo, Reparo Rápido antes de anunciar, Vistoria de recebimento para quem comprou na planta.'],
        ['Comissão', '10% a 15% em laudos e vistorias (recomendado 10% nas vistorias) e 10% na regularização ' + tag('P') + '. Desconto ao cliente ou pagamento ao corretor.'],
        ['Avatar ' + tag('P'), 'Corretor autônomo ou imobiliária pequena de Goiânia que vende imóvel usado e lançamento, e já perdeu negócio por área sem registro, defeito descoberto tarde ou comprador inseguro.'],
        ['O que muda para nós', 'Resposta em até 2 horas úteis, proposta no mesmo dia e vistoria em até 3 dias úteis. Corretor não espera.'],
        ['Teste ' + tag('P'), '3 corretores conhecidos, 2 serviços pagos até 18/12. Medir tempo de resposta e conversão.'],
    ], oferta='''[Nome], boa tarde. Tudo bem?

Te escrevo porque sei que negócio de imóvel usado costuma travar em dois pontos: área construída que não está na matrícula e comprador com medo do que não aparece na visita.

A Entre Colunas resolve os dois. A gente faz a vistoria antes da compra, com relatório em até 2 dias úteis, e cuida da regularização quando a área não bate. Cada indicação sua que virar serviço tem comissão, combinada por escrito.

Você tem algum imóvel agora em negociação em que isso ajudaria? Se tiver, me passa o endereço que eu te respondo hoje mesmo.''')
    return page('Item 5 · Parcerias', 'Item 5 · Parcerias',
        'Arquitetos e corretores alimentam os itens 2, 3 e 4. A conversa com eles é outra: o parceiro não compra, ele indica, e cada indicação coloca a reputação dele em jogo.',
        '<div class="two-flow"><div>' + arq + '</div><div>' + cor + '</div></div>')


def item6():
    regras6 = box('Regras da mensalidade ' + tag('P'), ul([
        'Funciona como o advogado de partido: o cliente paga todo mês, usando ou não. Visitas e consultas não usadas não acumulam.',
        'Lista fechada do que está incluído: visitas, relatório, calendário de vencimentos, cotações e consultas por WhatsApp em horário comercial.',
        'Obra e reforma nunca estão na mensalidade: são orçadas à parte e entram como Fiscalização ou Gestão (item 4).',
        'Laudos e documentos com ART própria recebem proposta à parte, com 10% de desconto para assinante.',
        'Mensal, sem fidelidade, aviso de 30 dias; reajuste anual pelo IPCA.']))
    cond = ficha('Engenheiro do Condomínio', T_, [
        ['Para quem', 'Síndico profissional ou morador, em prédio com manutenção a cargo do condomínio. Piloto: Edifício Trípoli.'],
        ['Planos', 'Implantação R$ 2.600 · Essencial R$ 1.600/mês (1 visita, relatório, calendário, 1 cotação, 4 consultas) · Completo R$ 2.200/mês (2 visitas, 2 cotações, 8 consultas).'],
        ['Atenção', f'Com o Aruak sozinho no campo, o Essencial fica em {brl(ESS_AR.ph, True)}/h e o Completo em {brl(COMP_AR.ph, True)}/h. A margem vem com a passagem do campo para o Yan.'],
    ])
    esc_ = ficha('Engenheiro da Escola', T_, [
        ['Por que é nicho forte', 'Escola está sempre em reforma, tem janela certa para obra (férias de dezembro e de julho), vencimentos com Bombeiros e Vigilância Sanitária e responsabilidade com crianças.'],
        ['Para quem', 'Escola particular com prédio próprio, ou alugado com a manutenção a cargo dela, em que a direção ou a mantenedora decide e paga.'],
        ['Inclui', '1 visita por mês fora do horário de aula, ronda com checklist e fotos só das instalações, relatório mensal com semáforo, calendário de vencimentos com aviso de 60 dias, 1 cotação, 4 consultas e aviso imediato de ocorrência crítica.'],
        ['Preço', f'R$ 1.800/mês ' + tag('P') + f', pago em dinheiro · {brl(ESCOLA.ph, True)}/h ' + tag('E') + '. A Tip Toy segue como piloto compensado na mensalidade do Theo.'],
        ['Oferta extra', 'Plano de férias: em outubro e em maio, lista das obras da próxima janela com orçamento e fiscalização (item 4).'],
    ], oferta='''[Nome], bom dia. Aqui é o Aruak, engenheiro, da Entre Colunas.

Escola tem duas épocas que não perdoam: as férias, quando toda obra precisa caber em poucas semanas, e os vencimentos de Bombeiros e Vigilância Sanitária, que aparecem sempre na hora errada.

Eu acompanho a manutenção da escola todo mês, com visita fora do horário de aula, relatório curto e o calendário de vencimentos com aviso de 60 dias. Quando chega a janela de férias, a lista de obras já está orçada.

Faz sentido eu passar aí numa [dia] depois das [hora] para conhecer o prédio?''')
    emp = ficha('Engenheiro da Empresa', O_, [
        ['Para quem', 'Empresa com sede ou galpão próprio, que precisa de manutenção predial e de segurança do trabalho em dia.'],
        ['Inclui ' + tag('P'), '1 visita por mês, consultas, calendário de vencimentos, cotações e o acompanhamento do PGR ao longo do ano, com a revisão dentro da mensalidade. O PGR inicial é cobrado à parte.'],
        ['Preço', f'R$ 3.000/mês · {brl(EMPRESA.ph, True)}/h ' + tag('E')],
    ])
    return page('Item 6 · Recorrência', 'Item 6 · Recorrência',
        'O cliente paga todo mês e a Entre Colunas cuida das consultas, dos vencimentos e da manutenção. É o que dá previsibilidade de caixa, e hoje depende de um só piloto.',
        regras6 + '<div class="two-flow"><div>' + cond + emp + '</div><div>' + esc_ + '</div></div>')


def tabela_rapida():
    rows = [
        ['2', 'Visita Diagnóstica', 'R$ 1.200', 'Nota em até 2 dias úteis', 'Antes do agendamento', '10% a 15%'],
        ['2', 'Conferência da Medição', 'R$ 1.800 [P]', 'Visita em 3 dias úteis, nota em 2', 'Antes do agendamento', '10% [P]'],
        ['3', 'Laudo técnico', 'A partir de R$ 3.000', 'Na proposta', 'Na proposta', '10% a 15%'],
        ['3', 'Vistoria (até 100 / 100 a 250 / 250+ m²)', 'R$ 840 / 1.150 / 1.400', 'Relatório em 2 dias úteis', 'No agendamento', '10% (recomendado)'],
        ['3', 'Vistoria Completa, com revisita', 'R$ 1.080 / 1.500 / 1.950', 'Revisita em até 60 dias', 'No agendamento', '10% (recomendado)'],
        ['3', 'PGR · LTCAT · pacote', 'R$ 2.200 · 3.800 · 5.400 [P]', 'A definir', 'A definir', '10% [P]'],
        ['3', 'Regularização: diagnóstico · completa até 150 m²', 'R$ 1.200 · 5.000 [P]', 'Depende da prefeitura', 'A definir', '10% [P]'],
        ['3', 'Assistência técnica', 'R$ 6.000 em 3 etapas [P]', 'Prazos do processo', 'Por etapa', '10% [P]'],
        ['3', 'EIV e EIT: análise de enquadramento', 'R$ 800 [P]', 'A definir', 'Antes', '10% [P]'],
        ['4', 'Estudo de Viabilidade Financeira', 'R$ 2.500', '7 a 15 dias úteis', '50% e 50%', '10% [P]'],
        ['4', 'Orçamento Executivo', 'R$ 5.000', '15 dias úteis', '50% e 50%', '10% [P]'],
        ['4', 'Plano para Terminar', 'R$ 4.500 / 5.500 / 3.900 [P]', '10 dias úteis', '50% e 50%', '4%'],
        ['4', 'Reparo Rápido', 'Preço fechado após medição', 'Três datas', 'Na proposta', '4%'],
        ['4', 'Fiscalização · Gestão e fiscalização', 'R$ 3.500/mês [P] · a partir de R$ 7.400/mês', 'Mensal', 'Início do mês', '4%'],
        ['6', 'Condomínio: implantação · Essencial · Completo', 'R$ 2.600 · 1.600 · 2.200/mês', 'Mensal', 'Mensal', 'A definir'],
        ['6', 'Escola · Empresa', 'R$ 1.800/mês [P] · R$ 3.000/mês', 'Mensal', 'Mensal', 'A definir'],
    ]
    t = table(['Item', 'Produto', 'Preço', 'Prazo', 'Pagamento', 'Comissão'], rows, 'sm', widths=['6%', '30%', '22%', '17%', '13%', '12%'])
    return page('Tabela rápida', 'Tabela rápida para a atendente (link interno)',
        'Para responder na hora sobre valor, prazo, pagamento e comissão. Preço marcado [P] ainda depende de confirmação do Aruak.', t +
        '<p class="small">Vistoria antes da compra usa a mesma tabela da vistoria de recebimento. Taxas de prefeitura e cartório são sempre do cliente. Reparo Rápido, Gestão e Condomínio: valor só depois da visita ou da reunião.</p>')


def decisoes():
    d = ol(['<b>Base dos 4%:</b> sobre os honorários da Entre Colunas ou sobre o valor total da obra? Numa obra de R$ 300 mil, é a diferença entre R$ 1.976 e R$ 12.000.',
            '<b>Comissão nas vistorias:</b> 10% (recomendado) ou até 15%? A 15% a vistoria fica abaixo da meta.',
            '<b>Comissão dos estudos, regularização e segurança do trabalho:</b> 10% como proposto?',
            '<b>Preços novos:</b> Conferência R$ 1.800; Plano R$ 4.500 / 5.500 / 3.900; PGR R$ 2.200; LTCAT R$ 3.800; regularização R$ 1.200 + R$ 5.000; assistência técnica R$ 6.000; Fiscalização R$ 3.500/mês; Escola R$ 1.800/mês.',
            '<b>CREA-GO:</b> especialização em segurança do trabalho registrada? Qual ART usar na fiscalização?',
            '<b>Médico do trabalho parceiro</b> para o PCMSO.',
            '<b>Apoio técnico de orçamento:</b> sem ele, Viabilidade, Orçamento e Plano não pagam a meta.',
            '<b>Texto de responsabilidade e contrato de fiscalização:</b> revisão do Vicente.',
            '<b>Selo novo:</b> vetorizar com designer.',
            '<b>Assistente da Obra:</b> criar o GPT e mandar o link.'])
    ordem = table(['Ordem', 'O que lançar', 'Por quê'], [
        ['1', 'Link público do Scanner e atendimento ativo no WhatsApp', 'Já está pronto; é a porta de todos os itens'],
        ['2', 'Vistorias e laudos com 3 corretores', 'Caixa mais rápido, margem alta, venda curta'],
        ['3', 'Conferência da Medição e Plano para Terminar', 'O Raio-X já gera esses contatos'],
        ['4', 'Arquitetos: 2 escritórios', 'Leva ao item 4 e à Gestão'],
        ['5', 'Regularização e segurança do trabalho', 'Depois de confirmar CREA, médico parceiro e preços'],
        ['6', 'Escola e Empresa', 'Janeiro, com a janela de férias e o calendário de vencimentos'],
    ], 'sm', widths=['8%', '46%', '46%'])
    return page('Decisões e lançamento', 'O que falta decidir e em que ordem lançar',
        'Com estas decisões, a esteira fica pronta para a equipe usar.',
        '<div class="two"><div><h2>Decisões do Aruak</h2>' + d + '</div><div><h2>Ordem de lançamento ' + tag('P') + '</h2>' + ordem + '</div></div>')


def main():
    body = capa() + regras() + item1() + item2() + item3() + item4() + item5() + item6() + tabela_rapida() + decisoes()
    extra = 'table.ficha thead{display:none} table.ficha{border-top:2px solid #1b6b57} table.ficha td:first-child{color:#1b6b57} table.ficha td table.t thead{display:table-header-group} table.ficha td table.t{margin:0}'
    html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Esteira formulada, itens 1 a 6</title><style>' + CSS + extra +
            '</style></head><body>' + body + '</body></html>')
    open('esteira.html', 'w').write(html)
    print('ok', len(html))


if __name__ == '__main__':
    main()
