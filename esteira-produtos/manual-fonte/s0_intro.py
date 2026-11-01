# -*- coding: utf-8 -*-
from common import *

def capa():
    return f'''<section class="cover">
<div class="band"><div class="brand">ENTRE COLUNAS · ENGENHARIA DE PREVISIBILIDADE</div>
<h1>Manual operacional das seis frentes</h1>
<p class="lead">Como qualificar e apresentar cada oferta, como executar e comprovar a entrega, e como acompanhar o dinheiro recebido, comprometido e o que sobra depois de remunerar o trabalho.</p>
<p class="lead" style="margin-top:6mm;font-size:9.5pt">Versão 1.0 · 01/11/2026 · Goiânia · circulação interna</p></div>
<div class="meta">
<table class="t sm" style="margin-bottom:4mm"><thead><tr><th style="width:6%">#</th><th style="width:30%">Frente</th><th>O que o cliente compra</th></tr></thead><tbody>
<tr><td>1</td><td>Scanner da Obra</td><td>Triagem gratuita que mostra o próximo passo e encaminha ao WhatsApp</td></tr>
<tr><td>2</td><td>Visita Diagnóstica, Laudo e Vistoria</td><td>Evidência técnica para decidir, documento para terceiros, recebimento ou compra de imóvel</td></tr>
<tr><td>3</td><td>Reparo Rápido</td><td>Banheiro renovado com preço fechado e três datas</td></tr>
<tr><td>4</td><td>Gestão de Obra</td><td>Coordenação por administração, com o dinheiro da obra na mão do cliente</td></tr>
<tr><td>5</td><td>Pré-obra com Arquitetos</td><td>Viabilidade ou orçamento executivo antes de começar</td></tr>
<tr><td>6</td><td>Engenheiro do Condomínio</td><td>Implantação e acompanhamento mensal, piloto no Edifício Trípoli</td></tr>
</tbody></table>
<div class="who">
<div><b>Quem vende</b>Qualifica com as perguntas de cada frente, apresenta a página comercial e registra tudo no Placar. Toda conversa termina com sim, não ou data.</div>
<div><b>Quem executa</b>Segue a sequência da ficha interna, usa os modelos, comprova a entrega com evidência escrita e registra horas no Painel de Obras.</div>
<div><b>Quem controla o dinheiro</b>Lança recebido, comprometido e pago por contrato no Mais Controle e acompanha os três indicadores de cada ficha.</div>
</div>
<p class="small">Base: consolidado revisado de 01/11/2026 (seis frentes), correções posteriores das contas, fichas do projeto (Engenheiro do Condomínio v2, Tip Toy v2, Gestão de Obra no método Bora, avatares e filtros, Scanner v2), material da Certificação Método BORA, roteiro e dossiê do Edifício Trípoli e as decisões do Aruak até 01/11/2026. As páginas marcadas como página comercial podem ser apresentadas ao cliente; o restante é de uso interno. Números marcados como estimados ou simulados precisam ser substituídos pelos medidos.</p>
<p class="small">{RT} · {CONTATO}</p>
</div></section>'''

def como_usar():
    leitores = table(['Quem', 'O que ler primeiro', 'O que preencher', 'Onde registrar'], [
        ['Quem vende (hoje: Aruak; Gabriela na triagem)', 'Página comercial de cada frente, perguntas de qualificação, critérios de recusa e mensagens prontas', 'Nota de qualificação, condição informada ao cliente, data do próximo passo, motivo de perda', '<b>Placar</b>: oportunidade, origem, decisor, ação datada, preço, sinal ou motivo de recusa'],
        ['Quem executa (hoje: Aruak; Yan quando a atribuição e as horas forem confirmadas)', 'Sequência de execução, checklist, modelos e critério de aceite de cada ficha', 'Checklist de campo, devolutiva, medições, relatórios e termo de aceite', '<b>Painel de Obras</b>: escopo aceito, agenda, horas por pessoa, marcos, pendências'],
        ['Quem controla o dinheiro (hoje: Gabriela e Flávia; controladoria proposta a Vicente)', 'Bloco “dinheiro” de cada ficha, quadro de caixa e estrutura da empresa', 'Recebido, a receber, comprometido, pago, custo para terminar e horas', '<b>Mais Controle</b>: um registro por contrato, sem misturar dinheiro de um contrato com outro'],
    ], widths=['22%', '28%', '26%', '24%'])
    leg = table(['Marca', 'Significa'], [
        [tag('D'), 'Decisão do Aruak. Só muda com nova decisão dele.'],
        [tag('A'), 'Informado pelo Aruak, ainda sem documento conferido.'],
        [tag('M'), 'Medido em contrato real (horas, valores ou prazos registrados).'],
        [tag('E'), 'Estimado. Precisa ser medido nas próximas entregas.'],
        [tag('P'), 'Proposto neste manual. Vale como regra de trabalho até o Aruak confirmar ou mudar.'],
        [tag('R'), 'Referência externa (CREA-GO, método BORA, normas).'],
        [tag('S'), 'Exemplo simulado, para treinar o uso do modelo. Não é caso real.'],
        ['<span class="tg">[pendente de decisão]</span>', 'Escolha em aberto. A ficha mostra a regra provisória.'],
    ], widths=['26%', '74%'])
    est = table(['Estágio', 'Uso no manual'], [
        ['<span class="pill p-v">Vendido</span>', 'Já houve venda paga daquele formato (laudo, vistoria).'],
        ['<span class="pill p-t">Em teste</span>', 'Preço ou formato em teste até 18/12/2026, com regra de decisão escrita.'],
        ['<span class="pill p-c">Sob consulta</span>', 'Publicado no catálogo sem preço; a proposta sai depois da visita ou do planejamento.'],
        ['<span class="pill p-i">Ideia</span>', 'Fica para a lista de janeiro de 2027.'],
    ], widths=['26%', '74%'])
    regras = ul([
        '<b>Duas prioridades até 18/12/2026:</b> reformas e serviços ligados a elas, e o piloto do Engenheiro do Condomínio no Trípoli. Ideia nova vai para a lista de janeiro. ' + tag('D'),
        '<b>Preço global fechado, na execução de obra, só no Reparo Rápido enquadrado</b> (banheiro; cozinha depois do primeiro banheiro). Visita, vistoria, laudo e pré-obra têm honorário fechado por escopo. Condomínio tem implantação e mensalidade. O restante da execução é Gestão de Obra por administração. ' + tag('D'),
        '<b>O dinheiro de um contrato não paga outro.</b> Na gestão, o dinheiro da obra não passa pelo caixa da Entre Colunas. ' + tag('D'),
        '<b>Promessa só sai medida, precificada, contratada e com responsável.</b> Nenhum prazo de execução é anunciado antes de ser medido em caso real. ' + tag('D'),
        '<b>Contratos mensais sem fidelidade</b>, com aviso de 30 dias. ' + tag('D'),
        '<b>Nenhum software pago antes de janeiro de 2027.</b> Fontes de verdade: Placar, Painel de Obras e Mais Controle, sem duplicar. ' + tag('D'),
        '<b>O Aruak sai do papel de mestre de obras.</b> Mais horários oferecidos na agenda, não mais horas do Aruak; visitas em janelas fixas. Ordem de prioridade: Saúde, Família, Trabalho. ' + tag('D'),
    ])
    return page('Guia de uso', 'Como usar este manual', 'Cada frente tem uma página comercial e uma ficha interna com exemplo preenchido. Comece pela sua função.',
        leitores + '<div class="two"><div><h2>Legenda das marcas</h2>' + leg + '</div><div><h2>Estágio de cada oferta</h2>' + est +
        box('Regra de ouro do vendedor', '<p>Toda conversa comercial termina com sim, não ou data. Proposta se apresenta, não se envia. Obstáculo (decisor, prazo, verba) se pergunta antes do preço.</p>') +
        '</div></div><h2>Regras que valem para todas as frentes</h2><div class="small" style="color:#1f2a30">' + regras + '</div>')

def premissas():
    prem = table(['Premissa', 'Valor', 'Origem e tratamento'], [
        ['Tributos sobre a receita', '8%', tag('A') + ' Informado pelo Aruak. O contador confirma empresa, serviço e alíquota efetiva. Versões anteriores usavam 13% e ficam identificadas com a data.'],
        ['Remuneração interna da hora do Aruak', brl(AR) + '/h', tag('D') + ' Usada só para calcular o saldo parcial. Não é pró-labore.'],
        ['Meta de disponível por hora do Aruak', brl(META) + '/h', tag('P') + ' Antes de remunerar o Aruak. Abaixo dela, a oferta precisa de ajuste de escopo, preço ou equipe.'],
        ['Hora técnica (Yan, coordenador, orçamentista, júnior)', brl(TEC) + '/h', tag('E') + ' Versões antigas usavam R$ 80/h.'],
        ['Hora administrativa', brl(ADM) + '/h', tag('E')],
        ['Deslocamento', brl(IDA) + ' por ida', tag('E') + ' Registrar também as horas de trajeto.'],
        ['ART, Tabela A do CREA-GO 2026', f'{brl(ART1, True)} até R$ 15 mil · {brl(ART2, True)} acima', tag('R') + ' Aplicar a modalidade correspondente à atividade e ao contrato.'],
        ['ART anual do condomínio', f'{brl(ART2, True)} · {brl(ARTM, True)} por mês em 12 meses', tag('R') + ' Sai do caixa no registro. Se o contrato terminar no 3º mês, pesa ' + brl(ART2/3, True) + ' por mês atendido.'],
        ['ART de rotina (Tabela B)', f'{brl(ARTROT1, True)} até R$ 1.000 · {brl(ARTROT2, True)} até R$ 2.000', tag('pendente de decisão') + ' Só se o CREA-GO aceitar vistoria e laudo nessa modalidade.'],
    ], widths=['28%', '24%', '48%'])
    ex = V1200
    conta = table(['Linha da conta (visita de R$ 1.200 por indicação)', 'Valor'], [
        ['Receita', brl(ex.receita)],
        ['(−) Tributos 8%', brl(-ex.trib)],
        ['(−) Administrativo 0,5 h, uma ida e ART', brl(-ex.ccustos)],
        ['(−) Aquisição atribuível', brl(0)],
        {'cls': 'tot', 'cells': ['= Disponível antes de remunerar o Aruak', brl(ex.disp)]},
        ['÷ 4,5 h do Aruak = disponível por hora', brl(ex.ph)],
        ['(−) 4,5 h × R$ 100', brl(-450)],
        {'cls': 'tot', 'cells': ['= Saldo parcial do produto', brl(ex.saldo)]},
    ], 'num', widths=['74%', '26%'])
    tres = ('<div class="step"><b class="nn">1</b><div><b>Disponível por hora do Aruak.</b> Receita menos tributos, equipe, terceiros, despesas diretas e aquisição atribuível, dividido pelas horas do Aruak, antes de remunerá-lo. No Scanner, sem horas dele, usar custo por atendimento e por cliente pago.</div></div>'
            '<div class="step"><b class="nn">2</b><div><b>Saldo parcial do produto.</b> O disponível total menos as horas do Aruak a R$ 100. Não inclui estrutura não alocada, ociosidade, garantia e retrabalho: esses entram uma única vez no fechamento do mês.</div></div>'
            '<div class="step"><b class="nn">3</b><div><b>Caixa livre do contrato.</b> Recebimentos efetivos menos pagamentos e menos o que ainda precisa ficar reservado para terminar a entrega. O maior saldo acumulado negativo define o giro necessário. A dívida antiga tem controle separado.</div></div>')
    reg = box('Registro antes de comprometer a equipe (um por contrato, no Mais Controle)',
              '<p>Cliente e produto · entrega e exclusões · preço e datas de recebimento · horas previstas por pessoa · executor e revisor · gasto que acontece antes da próxima entrada de dinheiro · prazo · critério de aceite. Ao lado de cada indicador, anotar <b>quantos contratos já foram medidos</b>. Hoje, nenhum produto deste manual tem horas medidas em contrato: todos os números de horas são informados ou estimados.</p>')
    return page('Economia', 'Premissas e as três contas de cada ficha', 'Usar as mesmas definições permite comparar produtos e preservar o dinheiro necessário para a entrega.',
        prem + '<div class="two"><div><h2>As três contas</h2>' + tres + '</div><div><h2>Exemplo de leitura</h2>' + conta + '</div></div>' + reg)

def mapa():
    rows = [
        ['1', 'Scanner da Obra', '0 · porta', 'Morador, comprador, síndico', 'Grátis', '<span class="pill p-t">Em teste</span>', 'Gabriela', 'Formulário + Gabriela', '30 formulários com custo por cliente pago'],
        ['2', 'Visita Diagnóstica, Laudo e Vistoria', '1 · diagnóstico', 'Quem tem um problema sem causa clara, precisa de documento ou vai receber ou comprar imóvel', 'Visita R$ 1.200 · laudo a partir de R$ 3.000 · vistoria R$ 840 a R$ 1.950', '<span class="pill p-v">Vendido</span> laudo e vistoria · <span class="pill p-t">Em teste</span> visita', 'Aruak', 'Aruak', '5 visitas qualificadas até 30/11; último laudo reconstruído; 3 vistorias cronometradas'],
        ['3', 'Reparo Rápido', '2 · solução', 'Morador de banheiro ocupado, sem querer quebradeira', 'Preço global fechado após medição', '<span class="pill p-c">Sob consulta</span>', 'Aruak', 'Aplicador + coordenador; Aruak libera', 'Banheiro do Alexandre com cotação, aplicador e três datas'],
        ['4', 'Gestão de Obra', '2 · solução', 'Dono com projeto, verba e decisor, que quer previsibilidade', 'Honorário mensal por equipe (recomendado)', '<span class="pill p-c">Sob consulta</span>', 'Aruak', 'Coordenador de campo + Aruak', 'Medição Medeiros reconstruída; 1 proposta apresentada'],
        ['5', 'Pré-obra com Arquitetos', '1 · diagnóstico', 'Cliente do arquiteto travado no investimento', 'Viabilidade R$ 2.500 · orçamento executivo R$ 5.000', '<span class="pill p-t">Em teste</span>', 'Aruak (Ivan, se aceitar)', 'Aruak + apoio técnico a definir', '2 escritórios, 1 projeto real cada, 1 estudo pago'],
        ['6', 'Engenheiro do Condomínio', '3 · recorrência', 'Síndica do Trípoli', 'Implantação R$ 2.600 · Essencial R$ 1.600/mês · Completo R$ 2.200/mês', '<span class="pill p-t">Em teste</span>', 'Aruak', 'Aruak; Yan após a regra de passagem', 'Proposta apresentada à Carmem e decisão'],
    ]
    t = table(['#', 'Frente', 'Degrau', 'Para quem', 'Preço ou critério', 'Estágio', 'Quem vende', 'Quem executa hoje', 'Prova até 18/12'], rows, 'sm',
              widths=['3%', '13%', '8%', '17%', '17%', '11%', '8%', '11%', '12%'])
    escada = box('Como a escada funciona', '<p>O degrau 0 qualifica sem consumir o Aruak. O degrau 1 cobra o trabalho técnico que ajuda o cliente a decidir. O degrau 2 resolve (Reparo Rápido com preço fechado; Gestão por administração). O degrau 3 mantém o cliente (condomínio e empresa). Cada entrega termina com a oferta do degrau seguinte, sem vender execução ao condomínio assessorado durante o piloto.</p>')
    fora = '<p class="small"><b>Fora das duas prioridades, só por oportunidade:</b> Engenheiro da Empresa (R$ 3.000/mês, ' + brl(EMPRESA.ph) + '/h estimados), Engenheiro da Escola (Tip Toy, R$ 1.800/mês compensados na mensalidade, sem entrada de caixa e com cerca de ' + brl(TIPTOY_TRIB) + ' de tributo a 8%), perícia, regularização e EIV. Não entram nas metas até 18/12.</p>'
    return page('Mapa', 'As seis frentes em uma página', 'Quem compra, o que compra, em que estágio está e qual prova precisa existir até 18/12/2026.', t + escada + fora)
