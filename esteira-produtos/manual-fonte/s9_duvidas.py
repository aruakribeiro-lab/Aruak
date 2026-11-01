# -*- coding: utf-8 -*-
from common import *

V = '<b>Vender</b>'; X = '<b>Executar</b>'; A = 'Só ampliar'; N = 'Não impede'

DUVIDAS = [
    ('Quantas horas o Aruak e o Yan têm de fato, e qual é a atribuição profissional do Yan?',
     'Aruak com até 120 h por mês nas seis frentes; Yan com cerca de 40 h livres, sem assinar documento técnico.',
     'Capacidade do mês, quem conduz o campo da gestão, a delegação no condomínio e todos os cenários.', 'Aruak e Yan, em 03/11', X + ' gestão e delegação no condomínio; ' + A),
    ('Quem assume cotações, suprimentos, controle de custos e o apoio técnico de orçamento depois da saída do Korran? A Edna participa?',
     'Técnico ou orçamentista a R$ 60/h, pago por entrega.',
     'Sem apoio, o orçamento cai de ' + brl(ORC.ph) + '/h para ' + brl(ORC_SEM.ph) + '/h e o Reparo fica sem preço.', 'Aruak, em 03/11', V + ' e ' + X + ' Reparo e orçamento executivo'),
    ('Qual modelo de honorário usar na primeira gestão?',
     'Honorário mensal por equipe (R$ 12.350 no exemplo) e prorrogação a 60% por alteração do cliente ou causa externa.',
     'Proposta, contrato e o resultado quando a obra atrasa.', 'Aruak decide; Vicente redige', V + ' gestão'),
    ('O que a Carmem respondeu em 16/10 e qual condição de piloto foi prometida? Qual a arrecadação real, o número de unidades e o mandato?',
     'Valores cheios (R$ 2.600, R$ 1.600, R$ 2.200); sem desconto, salvo se prometido (30% nas 3 primeiras mensalidades custam R$ 1.440).',
     'Formato (implantação avulsa ou assinatura), preço e a viabilidade do piloto.', 'Aruak', V + ' o Trípoli'),
    ('O que aconteceu com a proposta do Alexandre, com que valor e escopo, e quem aplica o sistema?',
     'R$ 19.400 como exemplo simulado; microcimento sem aplicador verificado.', 'Preço, datas e enquadramento do primeiro Reparo.', 'Aruak e suprimentos', V + ' e ' + X + ' o primeiro Reparo'),
    ('A alíquota de 8% vale para todos os serviços e empresas? Na gestão, a nota é só sobre o honorário?',
     '8% sobre a receita própria.', 'Cada ponto percentual muda R$ 12 na visita, R$ 30 no laudo, R$ 494 na gestão de 4 meses e todos os preços mínimos.', 'Contador (via Gabriela ou Ivan)', N + '; muda preço mínimo'),
    ('Do que são compostos os R$ 30 mil de lucro bruto de hoje e qual é a estrutura não alocada?',
     'Estrutura de R$ 15 mil por mês no patamar 1 ' + tag('E') + '.', 'Caixa livre, capacidade de pagar a dívida e o momento de contratar.', 'Gabriela e Flávia no Mais Controle; Vicente, se aceitar', A),
    ('Como está a dívida de R$ 650 mil: credores, juros, vencimentos e garantias?',
     'Controle separado; prazos ilustrativos sem juros.', 'Caixa livre real e o ritmo de crescimento possível.', 'Aruak e Vicente', A),
    ('Ivan e Vicente aceitam os papéis propostos? Como fica o acordo dos 35%?',
     'Ivan na abertura de oportunidades; Vicente em controladoria e contratos; nada aceito.', 'Quem faz canal e controladoria e quanto tempo do Aruak é liberado.', 'Aruak, Ivan e Vicente, com revisão jurídica independente', A),
    ('Quanto a Medeiros pagou de honorários, quanto durou, quantas horas o Aruak dedicou e quem segurava o campo?',
     'Caso não reconstruído; hipótese de 20 h do Aruak, 32 h de coordenação e 6 h administrativas por mês.', 'Carga e valor do honorário mensal; prazo-padrão da gestão.', 'Aruak', N + '; calibra a primeira proposta'),
    ('A regra da gratuidade depois do Scanner está confirmada?',
     'Investigar a causa = visita paga; solução definida = medição gratuita de até 1 h.', 'Conversão do Scanner e receita da visita.', 'Aruak', N + ' (vale até decisão contrária)'),
    ('Quem cobre a Gabriela e em que horário vale a promessa de 1 hora útil?',
     'Segunda a sexta, 8h às 17h30; cobertura sugerida: Flávia, só com as mensagens prontas.', 'O texto da promessa no formulário.', 'Aruak e Gabriela', A + ' (divulgação do Scanner)'),
    ('O CREA-GO aceita ART de rotina para vistoria e laudo? A visita diagnóstica precisa de ART? Cabe uma ART anual no condomínio?',
     'ART individual de R$ 108,39 por serviço; anual de R$ 285,59 no condomínio.', 'Vistoria pequena de R$ 159 para R$ 187 por hora; custo da visita.', 'Gabriela no CREA-GO', N),
    ('Como ficam arrependimento e cancelamento na contratação pelo WhatsApp com pagamento antecipado?',
     'Reagendamento uma vez com 24 h; cláusula a redigir (CDC, art. 49).', 'Condição de pagamento antes do agendamento.', 'Vicente', N + '; escrever antes de ampliar o Scanner'),
    ('O laudo de R$ 3.000 inclui leitura de documentos e estudo de hipóteses dentro das 8,25 h?',
     'Não inclui; com mais 2 h, o laudo cai para ' + brl(L3000_10.ph) + '/h.', 'Preço mínimo de ' + brl(L3000.pmin, True) + ' para ' + brl(L3000_10.pmin, True) + '.', 'Aruak, com o último laudo', N),
    ('As mais de 100 vistorias são de Goiânia ou da região? Quantas foram de recebimento e quantas de compra? Qual o prazo do relatório?',
     '“Mais de 100 vistorias entregues”, sem cidade; relatório em 2 dias úteis ' + tag('P') + '; pagamento na confirmação do agendamento ' + tag('P') + '.', 'Texto do catálogo e da página comercial.', 'Aruak', N),
    ('A Completa até 100 m² fica só para revisitas agrupadas? Qual o preço da revisita avulsa?',
     'Completa pequena só agrupada; revisita avulsa de R$ 450, R$ 520 e R$ 610 ' + tag('P') + '.', 'Tabela de vistorias e condições.', 'Aruak', N),
    ('O Reparo Rápido aceita “demolir e refazer”?', 'Fora do preço fechado; cotar depois de avaliação.', 'Escopo do catálogo.', 'Aruak', A),
    ('O filtro de entrada da gestão muda para obra a partir de R$ 150 mil ou honorário mínimo?', 'Obra a partir de cerca de R$ 150 mil ou honorário mínimo de ' + brl(G_PISO) + ' por mês ' + tag('P') + '.', 'Quais obras entram em gestão e quais vão para acompanhamento.', 'Aruak', N),
    ('Onde estão o contrato, o comprovante e as horas do EVF do Cleber?', 'R$ 2.000 com entrada, como registro histórico.', 'Preço de referência da viabilidade.', 'Aruak e Gabriela', N),
    ('Qual é o canal da Defesa Civil em Goiânia?', 'Só o 193 publicado.', 'Texto da saída vermelha.', 'Gabriela, com a Prefeitura', N),
    ('Como a Tip Toy registra a compensação, qual regra vale para obras futuras (0%, 10% e 8%, ou 15%) e como regularizar a ART desde outubro?',
     'Cerca de ' + brl(TIPTOY_TRIB) + ' de tributo a 8% por mês, sem entrada de caixa.', 'Custo real da escola e regra de obras futuras.', 'Contador, Vicente e Aruak', N),
    ('Quanto cobrar de deslocamento fora de Goiânia, quantas assembleias o condomínio inclui e qual o valor da visita extra?',
     'R$ 50 por ida em Goiânia; 1 assembleia por semestre; visita extra com preço autorizado antes.', 'Preço de visitas e vistorias fora da cidade; limites do condomínio.', 'Aruak', N),
    ('O Estudo de Viabilidade de R$ 2.500 vale até 100 m² ou 3 ambientes?', 'Sim ' + tag('P') + '; acima disso, cotação.', 'Preço da viabilidade em obras maiores.', 'Aruak', N),
]

def build():
    rows = [[str(i + 1), q, p, m, w, b] for i, (q, p, m, w, b) in enumerate(DUVIDAS)]
    t = table(['#', 'Dúvida', 'Premissa adotada neste manual', 'O que pode mudar', 'Quem pode confirmar', 'Impede vender, executar ou só ampliar?'], rows, 'sm',
              widths=['3%', '27%', '25%', '19%', '13%', '13%'])
    intro = '<p>Em ordem de impacto. Enquanto a dúvida não for respondida, vale a premissa da terceira coluna. As oito primeiras mudam o que se vende ou quem executa nas próximas semanas; as demais ajustam preço, texto ou limite.</p>'
    fim = ('<p class="small">Referências usadas: consolidado revisado de 01/11/2026; revisão das contas; fichas do projeto (Engenheiro do Condomínio v2, Tip Toy v2, Gestão de Obra no método Bora, avatares, Scanner v2); '
           'material da Certificação Método BORA (apostila, modelos de EVF, contrato, ordem de compra, medição, relatório semanal e financeiro, cronograma da Família Medeiros); roteiro e dossiê do Edifício Trípoli; '
           'valores de ART da Tabela A do CREA-GO para 2026; Google Formulários (seções com desvio por resposta).</p>')
    return page('Fechamento', 'Dúvidas que surgiram durante a estruturação', 'Para cada dúvida: a premissa adotada, o que ela pode mudar, quem pode confirmar e se impede vender, executar ou apenas ampliar a operação.',
        intro + t + fim)
