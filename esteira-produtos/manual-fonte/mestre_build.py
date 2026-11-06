# -*- coding: utf-8 -*-
"""Documento mestre: tudo o que foi estruturado até 05/11/2026, no posicionamento novo."""
from common import *
import esteira_build as eb
import plano_build as pb
import importlib, s0_intro
MANUAL = [importlib.import_module(m) for m in ['s1_scanner', 's2_diag', 's3_reparo', 's4_gestao', 's5_preobra', 's6_condo', 's7_empresa', 's8_acoes', 's9_duvidas']]

SEC = 'Documento mestre'


def capa():
    return f'''<section class="cover" style="height:auto">
<div class="band"><div class="brand">ENTRE COLUNAS · ENGENHARIA DE PREVISIBILIDADE</div>
<h1>Documento mestre da Entre Colunas</h1>
<p class="lead">Tudo o que foi estruturado até agora em um só lugar: o posicionamento de gestora e fiscal do cliente, a esteira do item 1 ao 6 com preços e mensagens, o Scanner e o Raio-X da Obra, o Plano para Terminar a Obra, a gestão em vez de administração e a abordagem aos arquitetos.</p>
<p class="lead" style="margin-top:6mm;font-size:9.5pt">Versão 1.2 · 06/11/2026 · Goiânia · circulação interna</p></div>
<div class="meta">
{table(['Parte', 'Conteúdo'], [
        ['1 · Onde estamos', 'O que já está pronto, o que está em teste e o que falta decidir'],
        ['2 · Regras gerais', 'Posicionamento, responsabilidade, transição das obras atuais e comissões'],
        ['3 · A esteira, item a item', 'Porta de entrada, diagnóstico, laudos e documentos, obras, parcerias e recorrência, com tabela rápida'],
        ['4 · Gestão em vez de administração', 'Por que o modelo é viável, as quatro condições e como oferecer'],
        ['5 · Parcerias na prática', 'Roteiro da conversa com arquitetos, o que a Mariana contou e o Registro de Alteração de Obra'],
        ['6 · Scanner da Obra e Raio-X', 'As portas, os quatro indicadores e a classificação'],
        ['7 · Plano para Terminar a Obra', 'O produto novo completo: oferta, ficha, margem, triagem, mensagens, campo e riscos'],
        ['8 · Fichas operacionais detalhadas', 'O que é único no manual de 01/11: fichas internas, modelos, casos reais, contas, estrutura da empresa, quadro até 18/12 e dúvidas'],
        ['9 · Decisões e lançamento', 'O que falta decidir e em que ordem lançar'],
    ], 'sm', widths=['28%', '72%'])}
<p class="small">Une este documento ao Manual operacional das seis frentes (01/11), do qual a parte 8 traz só o que não se repete. Onde os dois divergirem, valem as partes 1 a 7. Marcas: {tag('D')} decisão do Aruak · {tag('P')} proposta, vale até confirmar · {tag('E')} estimado, a medir.</p>
<p class="small">{RT} · {CONTATO}</p>
</div></section>'''


def onde_estamos():
    pronto = table(['Entrega', 'Situação', 'Onde está'], [
        ['Scanner da Obra v5, com Raio-X, obra nova, vistorias e jornada do cliente', 'Publicado; link ainda privado', 'claude.ai/artifact/1h5ZWoMDvYETjoDnwatA4h'],
        ['Selo novo Entre Colunas Engenharia de Previsibilidade', 'Pronto, dourado e preto, sem fundo', 'esteira-produtos/marca'],
        ['Esteira formulada do item 1 ao 6', 'Pronta para a equipe', 'Parte 3 deste documento'],
        ['Plano para Terminar a Obra e Conferência da Medição', 'Estruturados, sem venda', 'Parte 7'],
        ['Apresentação da esteira para a equipe (8 páginas)', 'Pronta', 'Esteira_de_Produtos_Entre_Colunas.pdf'],
        ['Instruções do Assistente da Obra (GPT)', 'Prontas; falta criar o GPT', 'esteira-produtos/scanner'],
        ['Primeira conversa com arquiteto (Mariana Hammer)', 'Feita; dor registrada', 'Parte 5'],
        ['Registro de Alteração de Obra', 'Modelo pronto para enviar à Mariana', 'Parte 5'],
    ], 'sm', widths=['46%', '27%', '27%'])
    falta = ol(['Liberar o link do Scanner no menu Compartilhar e divulgar.',
                'Decidir a base dos 4% (honorários ou valor da obra) e a comissão nas vistorias (10% recomendado).',
                'Confirmar os preços propostos dos produtos novos.',
                'CREA-GO: ART da fiscalização e registro da especialização em segurança do trabalho.',
                'Contrato de fiscalização com a divisão de responsabilidade, revisado pelo Vicente.',
                'Apoio técnico de orçamento e médico do trabalho parceiro.',
                'Número novo do WhatsApp com verificação da Meta.',
                'Segunda conversa com a Mariana, levando o Registro de Alteração de Obra.'])
    return page(SEC, 'Parte 1 · Onde estamos', 'O que já existe, onde encontrar e o que falta para a esteira rodar.',
        '<h2>O que está pronto</h2>' + pronto + '<div class="two"><div><h2>O que falta</h2>' + falta + '</div><div>' +
        box('A ideia central', '<p>A Entre Colunas deixa de ser construtora e passa a ser a engenharia do lado do cliente: confere, mede, registra e avisa antes de cada decisão de dinheiro. A esteira leva o cliente do Scanner grátis ao diagnóstico pago, aos laudos, às obras com fiscalização e à mensalidade, com arquitetos e corretores indicando em todos os degraus.</p>') +
        '</div></div>')


def gestao():
    cond = table(['Condição', 'Por que', 'Como cumprir'], [
        ['1. Alguém responde pela execução', 'Sem ART de execução, quem assina vira, na prática, o responsável pela obra', 'Executor com responsável técnico próprio; em apartamento, definir por escrito quem assina o plano da NBR 16280; equipe informal em obra que exige responsável: responsabilidade técnica à parte, com preço do risco, ou recusar'],
        ['2. A medição trava o pagamento', 'Sem isso, o fiscal vira um relatório que ninguém lê', 'Cláusula no contrato do cliente com o executor: só se paga o que a Entre Colunas mediu e aprovou'],
        ['3. Escopo escrito', 'Com consumidor, o Código de Defesa do Consumidor anula cláusula que tira a responsabilidade; o que protege é o escopo preciso', 'Frequência de visitas, o que é conferido em cada etapa, prazo do relatório e o que fica de fora (elementos ocultos, ensaios, projeto)'],
        ['4. Nunca receber de executor ou fornecedor', 'É o que dá credibilidade ao fiscal', 'Compromisso escrito no contrato com o cliente. Comissão de arquiteto e corretor é diferente: eles indicam e não são fiscalizados'],
    ], 'sm', widths=['22%', '33%', '45%'])
    resist = table(['Resistência', 'Resposta'], [
        ['Cliente acha caro pagar quem não faz a obra', 'A conta do prejuízo: uma parcela adiantada que não vira serviço paga meses de fiscalização. A Conferência da Medição prova o valor antes'],
        ['Empreiteiro que não aceita ser medido', 'Já filtra quem não entregaria. Mesma lógica da empreita fechada com contrato para todos'],
        ['A equipe ainda opera como executora', 'Regra de transição: obras atuais terminam como estão; contratos novos já como fiscal'],
    ], 'sm', widths=['36%', '64%'])
    return page(SEC, 'Parte 4 · Gestão em vez de administração',
        '“Não somos responsáveis pela execução; respondemos pela fiscalização.” A linha é viável, mas só com as quatro condições abaixo.',
        '<div class="two"><div><h2>Por que é viável</h2>' + ul([
            'O Confea trata execução e fiscalização de obra como atividades técnicas diferentes, cada uma com a sua ART.',
            'Quem executa responde pela execução; pelo Código Civil, o empreiteiro responde por cinco anos pela solidez e segurança. O fiscal responde pelo serviço que presta: conferir, medir, registrar e alertar.',
            'Sem dinheiro de obra nem material passando pela empresa, acabam os prejuízos como os 8 rolos de fio do WTC.',
            'O honorário fica previsível e um fiscal atende mais obras por semana que um administrador.',
            'Engenheiros e empreiteiros viram parceiros, não concorrentes.']) +
        '</div><div><h2>Como oferecer</h2><p><b>Frase de venda:</b> “Você não precisa trocar quem vai executar. Precisa de alguém do seu lado que confira cada etapa antes de você pagar.”</p>' +
        ul(['<b>Fiscalização</b> (R$ 3.500/mês ' + tag('P') + '): uma visita por semana, medição antes de cada pagamento, relatório com fotos e pendências.',
            '<b>Gestão e fiscalização</b> (a partir de R$ 7.400/mês): fiscalização mais planejamento, cronograma, cotações em nome do cliente, reunião semanal e fechamento financeiro.',
            '<b>Porta de entrada:</b> Conferência da Medição e Plano para Terminar mostram com evidência o que um fiscal enxerga.',
            '<b>Levar na reunião:</b> relatório semanal e medição de exemplo, a cláusula de pagamento vinculado à medição e uma lista curta de empreiteiros que aceitam ser fiscalizados.']) +
        '</div></div><h2>As quatro condições</h2>' + cond + '<h2>Onde vai ter resistência</h2>' + resist +
        '<p class="small"><b>Teste ' + tag('P') + ':</b> nos dois próximos contratos novos, com as quatro condições desde o primeiro dia. Medir horas por mês, quantos pagamentos a medição barrou ou corrigiu, e se o cliente renova ou indica.</p>')


def parcerias():
    roteiro = table(['Momento', 'O que dizer'], [
        ['Abertura (30 s)', '“[Nome], bom dia. Aqui é o Aruak, engenheiro, da Entre Colunas. Você tem 5 minutinhos agora? Estou conversando com alguns arquitetos que eu respeito para entender como é o dia a dia de vocês com obra. Não vou te vender nada, quero ouvir você.”'],
        ['Aquecimento (1 min)', '“Vi o projeto [nome]. Gostei muito de [detalhe real]. Como foi esse?”'],
        ['A dor (3 a 6 min)', '“O que mais te incomoda hoje quando um projeto seu vai para a obra?” Se faltar: “Teve algum projeto recente que não terminou do jeito que você desenhou?” Para aprofundar: “Me conta mais.” “O que isso custou para você?” “O que você já tentou?” Para confirmar: “Então o que mais pesa hoje é [palavras dele]. É isso?”'],
        ['Pergunta nova', '“Como vocês lidam hoje com mudanças que o cliente aprova na obra?”'],
        ['Encerramento (30 s)', '“Obrigado. Me ajudou muito entender isso. Posso te mandar uma mensagem quando eu esbarrar com alguma coisa que ajude nesse ponto?”'],
    ], 'sm', widths=['20%', '80%'])
    regras_ = ul(['Não oferecer nada: nem estudo, nem fiscalização, nem comissão.', 'Quando ele parar de falar, contar até três antes da próxima pergunta.', 'Parar no minuto 10.',
                  'Se ele lembrar de um problema de obra feita juntos, não se defender: “É verdade. O que você acha que deveria ter sido diferente?”',
                  'Anotar no Placar a dor nas palavras dele, o que ela custa e um detalhe pessoal. Mensagem de agradecimento na mesma noite.'])
    mariana = box('Mariana Hammer · obra da Shaine em 2024 · conversa em 03/11', '<p><b>A dor, nas palavras dela:</b> o cliente muda alguma coisa durante a obra e depois questiona pontos como o elétrico. As mudanças normalmente são sugeridas pela marcenaria ou pelo profissional da obra.</p>'
        '<p><b>O que está por trás:</b> a mudança é aprovada de boca na obra, ninguém registra e ninguém avisa a arquiteta. Meses depois, ela leva a culpa por uma decisão que não foi dela. Custa reputação, tempo para provar o que estava no projeto e retrabalho caro.</p>'
        '<p><b>Próximo passo:</b> enviar o Registro de Alteração de Obra, gratuito, sem oferecer serviço. Se a dor se repetir em 2 ou 3 escritórios, ela vira a mensagem da parceria: “com alguém do lado do cliente, toda mudança fica registrada e você nunca mais leva a culpa pelo que não decidiu”.</p>')
    reg_msg = msg('''ALTERAÇÃO DE OBRA Nº [01]

Obra: [cliente e endereço] · Data: [dia/mês]

O que muda: [ex.: ponto de tomada da parede da TV sobe de 30 cm para 1,10 m]

Onde: [ambiente e parede] (foto em anexo)

Quem sugeriu: [marceneiro, eletricista, cliente, arquiteta] · Motivo: [...]

O que mais é afetado: [elétrica, marcenaria, hidráulica, revestimento ou nada]

Custo a mais: [R$ ou sem custo] · Prazo a mais: [dias ou nenhum]

Projeto da arquiteta: [mexe ou não mexe]

Aprovação do cliente: responder “APROVO A ALTERAÇÃO Nº [01]” · Ciência da arquiteta: responder “CIENTE”''')
    folha = table(['Nº', 'Data', 'O que muda', 'Onde', 'Quem sugeriu', 'Afeta', 'Custo e prazo', 'Aprovado por', 'Arquiteta ciente'],
                  [['01', '', '', '', '', '', '', '', ''], ['02', '', '', '', '', '', '', '', ''], ['03', '', '', '', '', '', '', '', '']], 'sm form')
    envio = msg('''Mariana, bom dia. Lembra do que você falou sobre o cliente mudar coisas na obra por sugestão do marceneiro e depois cobrar você pelo ponto elétrico?

Montei um registro simples para isso. Cada mudança vira uma mensagem no grupo da obra, com o que mudou, quem sugeriu, quem aprovou e se mexe no seu projeto. O cliente aprova por escrito e você dá ciência antes de executar.

Te mando abaixo. Se fizer sentido, testa na próxima obra e me conta o que mudaria.''')
    return (page(SEC, 'Parte 5 · Parcerias na prática: a primeira conversa',
        'Ligação de 5 a 10 minutos para descobrir a maior dor do arquiteto e criar rapport, sem oferecer nada.',
        '<h2>Roteiro</h2>' + roteiro + '<div class="two"><div><h2>Regras</h2>' + regras_ + '</div><div>' + mariana + '</div></div>')
        + page(SEC, 'Parte 5 · Registro de Alteração de Obra',
        'O presente da segunda conversa: resolve a dor da Mariana e pode ser usado com qualquer equipe.',
        '<div class="two"><div><h2>Texto para o grupo da obra</h2>' + reg_msg + '</div><div><h2>Três regras para combinar no início da obra</h2>' +
        ol(['Nenhuma mudança é executada sem o registro aprovado pelo cliente por escrito. A resposta no WhatsApp vale como aprovação.',
            'Se a mudança mexe no projeto, a arquiteta dá ciência antes de executar.',
            'No fim da obra, a lista de alterações vai junto com o projeto atualizado.']) +
        '<h2>Mensagem para a Mariana</h2>' + envio + '</div></div><h2>Folha para a pasta da obra</h2>' + folha +
        '<p class="small">Na Gestão e fiscalização, o registro de mudanças entra como parte do serviço. No Orçamento Executivo, a regra de mudanças entra no plano da obra.</p>'))


def scanner():
    portas = table(['Porta', 'Para quem', 'O que acontece', 'Resultado'], [
        ['Apareceu um problema', 'Morador com patologia', '8 perguntas: perigo, problema, onde, o que mudou, o que piora, tentativas, decisão e fotos', 'SCN-VERMELHO, DIAGNOSTICO, LAUDO ou REPARO'],
        ['Estou construindo ou reformando', 'Obra em andamento', 'Raio-X em 5 telas: ponto da obra, entregas, pago e entregue, dinheiro até a mudança e governança', 'SCN-OBRA com classificação e quatro indicadores'],
        ['Vou começar uma obra', 'Obra nova ou reforma geral', 'Tipo, ponto do projeto, verba, prazo e quem executa; caminho em seis etapas e cinco regras', 'SCN-PREOBRA'],
        ['Vou receber ou comprar um imóvel', 'Imóvel novo, usado ou com defeito', 'O que faz cada vistoria e o passo a passo do caso; alerta de regularização no usado', 'SCN-VISTORIA, COMPRA ou LAUDO'],
        ['Cuido de um prédio', 'Síndico', 'Dossiê do Prédio gratuito', 'SCN-SINDICO'],
    ], 'sm', widths=['20%', '18%', '40%', '22%'])
    ind = table(['Indicador do Raio-X', 'Conta'], [
        ['1 · Pagamento e entrega', 'Pago − executado e aceito − pago com destino identificado fora da medição. Tolerância: maior entre R$ 3.000 e 3% do combinado'],
        ['2 · Fôlego para terminar', 'Disponível + entradas confirmadas − dívidas − custo para terminar (mínimo e máximo)'],
        ['3 · Fôlego nos próximos 30 dias', 'Saldo dia a dia com entradas e os três maiores pagamentos; primeira data negativa'],
        ['4 · Confiabilidade das entregas', 'Três últimas entregas e as causas dos atrasos, separadas entre proprietário, equipe e fatores externos'],
    ], 'sm', widths=['30%', '70%'])
    cls = table(['Classificação', 'Quando'], [
        ['Replanejamento prioritário', 'Falta dinheiro no custo mínimo, caixa negativo em 30 dias, ou obra parada ou em troca de prestadores'],
        ['Dados insuficientes', 'Sem os indicadores 1 e 2; o resultado diz qual informação pedir à equipe'],
        ['Conferir antes da próxima decisão', 'Valor a conciliar, falta só no custo máximo, entregas a conferir, medição sem registro, pagamento pouco claro, faixa larga ou trinca aumentando'],
        ['Acompanhamento regular', 'Nenhum dos casos acima'],
    ], 'sm', widths=['30%', '70%'])
    return page(SEC, 'Parte 6 · Scanner da Obra e Raio-X',
        'A porta de entrada grátis: perguntas guiadas, resultado na hora com a jornada do cliente, e WhatsApp com o código e as respostas, cada parte num parágrafo.',
        '<h2>As portas</h2>' + portas + '<div class="two"><div><h2>Os quatro indicadores</h2>' + ind + '</div><div><h2>Classificação</h2>' + cls + '</div></div>'
        '<p class="small">Cada número traz a origem: com base em documento, estimado pelo proprietário ou a levantar. Nada é dado como conferido pela Entre Colunas. O Scanner não pede CPF, extrato nem dados bancários. O aviso de bombeiros saiu da entrada; a pergunta de perigo continua na porta do problema. Modo de teste: link com #teste no final, 13 casos.</p>')


def plano():
    # o Plano entra como parte 7, com a mesma capa de produto como abertura do capítulo
    return pb.comercial() + pb.ficha() + pb.dinheiro() + pb.triagem() + pb.mensagens() + pb.execucao() + pb.riscos_duvidas()


def aviso_manual():
    t = table(['No manual de 01/11', 'O que vale agora', 'Onde ver'], [
        ['Construtora Entre Colunas', 'Entre Colunas Engenharia de Previsibilidade', 'Parte 2'],
        ['Seis frentes', 'Esteira em seis itens: porta, diagnóstico, laudos e documentos, obras, parcerias, recorrência', 'Parte 3'],
        ['Gestão de Obra com compras e engenheiro responsável pelas decisões técnicas', 'Gestão e fiscalização: a Entre Colunas não executa; responde pela fiscalização', 'Partes 3 e 4'],
        ['Scanner no Google Formulários', 'Scanner publicado como página, com Raio-X, obra nova, vistorias e jornada', 'Parte 6'],
        ['Arquiteto que pede comissão é eliminatório; sem reserva técnica', 'Comissão de 4% sobre obra fechada e 10% a 15% em laudos e vistorias, como desconto ou pagamento ao profissional', 'Parte 2'],
        ['Obra em andamento ia direto para a Gestão', 'Conferência da Medição e Plano para Terminar como porta de entrada', 'Partes 3 e 7'],
        ['Perícia, regularização, EIV, escola e empresa fora da esteira', 'Braços dos itens 3 e 6, com preços propostos; PGR, LTCAT e PCMSO incluídos', 'Parte 3'],
        ['Mapa das seis frentes', 'Mapa da esteira em seis itens', 'Parte 3'],
    ], 'sm', widths=['36%', '46%', '18%'])
    return page('Parte 8 · Fichas operacionais', 'Parte 8 · Fichas operacionais detalhadas',
        'Do manual de 01/11 ficou só o que não existe nas partes 1 a 7: fichas internas, modelos, casos reais, contas, estrutura da empresa, quadro até 18/12 e dúvidas. Foi escrito antes do novo posicionamento: onde divergir, vale a tabela abaixo.',
        '<h2>O que mudou desde 01/11</h2>' + t +
        '<h2>O que entrou e o que saiu</h2>' + table(['Entrou nesta parte', 'Saiu, porque está nas partes 1 a 7 ou ficou desatualizado'], [[
            ul(['Premissas e contas', 'Visita, Laudo e Vistoria: ficha, exemplo, agendamento, checklist e modelos', 'Reparo Rápido: ficha, caso Alexandre, condições ocultas, datas e caixa',
                'Gestão: caso Medeiros, ordem de compra, medição, relatório semanal e fechamento financeiro', 'Pré-obra: proposta e amostra de entrega',
                'Condomínio: proposta do Trípoli, ficha, plano de 90 dias, checklist, relatório e limites', 'Estrutura da empresa, quadro até 18/12 e dúvidas']),
            ul(['Scanner no Google Formulários (o Scanner já está publicado)', 'Páginas comerciais antigas de Visita, Laudo, Vistoria, Reparo, Gestão e Pré-obra (as fichas da parte 3 substituem)',
                'Gestão de Obra no modelo de executor', 'Abordagem ao arquiteto sem comissão (substituída pela parte 5)', 'Comparativo das seis frentes e mapa antigo', 'Quadro de ações da semana de 03/11, que já passou', 'Exemplo de canais, composição simulada de custos e comparação de formas de cobrar a gestão'])]],
            'sm', widths=['50%', '50%']) +
        '<p class="small">Todos os números do manual continuam conferidos (32 de 32 valores do consolidado). As frentes seguem a ordem do manual: 1 Scanner, 2 Visita, Laudo e Vistoria, 3 Reparo Rápido, 4 Gestão de Obra, 5 Pré-obra com Arquitetos, 6 Engenheiro do Condomínio.</p>')


def manual():
    m = {x.__name__: x for x in MANUAL}
    s2, s3, s4, s5, s6, s7, s8 = m['s2_diag'], m['s3_reparo'], m['s4_gestao'], m['s5_preobra'], m['s6_condo'], m['s7_empresa'], m['s8_acoes']
    acoes = s8.build()
    acoes = acoes[acoes.index('<section', 10):]  # só o quadro até 18/12; a semana de 03/11 já passou
    return (aviso_manual() + s0_intro.premissas()
            + s2.ficha() + s2.agenda_checklist() + s2.devolutiva()
            + s3.ficha() + s3.alexandre() + s3.oculta_datas()
            + s4.medeiros() + s4.oc_medicao() + s4.relatorio_fechamento()
            + s5.proposta_amostra()
            + s6.comercial() + s6.ficha() + s6.plano90() + s6.checklist() + s6.relatorio_limites()
            + s7.cenario() + s7.patamares() + s7.ivan_vicente()
            + acoes + m['s9_duvidas'].build())


def main():
    body = (capa() + onde_estamos() + eb.regras() + eb.item1() + eb.item2() + eb.item3() + eb.item4() + eb.item5() + eb.item6() + eb.tabela_rapida()
            + gestao() + parcerias() + scanner() + plano() + manual() + eb.decisoes())
    extra = ('table.ficha thead{display:none} table.ficha{border-top:2px solid #1b6b57} table.ficha td:first-child{color:#1b6b57} '
             'table.ficha td table.t thead{display:table-header-group} table.ficha td table.t{margin:0} '
             '.client{font-size:9.3pt}.client h1.ct{font-size:24pt}.cgrid{gap:4mm 6mm}')
    html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Documento mestre da Entre Colunas</title><style>' + CSS + extra +
            '</style></head><body>' + body + '</body></html>')
    open('mestre.html', 'w').write(html)
    print('ok', len(html))


if __name__ == '__main__':
    main()
