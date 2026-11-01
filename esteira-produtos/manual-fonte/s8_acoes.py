# -*- coding: utf-8 -*-
from common import *

R = '<span class="pill p-t">Reformas</span>'
C = '<span class="pill p-c">Condomínio</span>'
B = '<span class="pill p-i">Base</span>'

def quadro(rows):
    return table(['Frente', 'Ação', 'Responsável', 'Prazo', 'Evidência de conclusão'], rows, 'sm', widths=['11%', '43%', '16%', '9%', '21%'])

def h24():
    rows = [
        [B, 'Ler “Como usar”, o mapa e as seis páginas comerciais; marcar o que estiver errado ou fora do que foi combinado', 'Aruak', '02/11', 'PDF marcado'],
        [C, 'Recuperar da reunião de 16/10 com a Carmem: o que ela precisa decidir, quantas visitas isso exige, quem aprova, o que disse sobre valor e o que foi dito sobre desconto. Preencher a tabela de promessas e os campos da página comercial do Trípoli', 'Aruak', '02/11', 'Placar: ficha c_carmem_tripoli completa'],
        [R, 'Abrir a proposta do Alexandre de 23/10 e preencher a ficha de enquadramento nas três colunas', 'Aruak', '02/11', 'Ficha na pasta do cliente; Placar com “proposta enviada” e pendências'],
        [R, 'Abrir o último laudo pago e reconstruir as horas por etapa', 'Aruak', '02/11', 'Linha no Mais Controle com horas [M] ou reconstruídas'],
        [R, 'Separar contrato da Resolve, extratos e cronograma da Família Medeiros', 'Aruak', '02/11', 'Pasta com os 4 dados ou “não localizado”'],
        [B, 'Escrever quantas horas por semana tem para vender e para entregar, respeitando Saúde, Família e Trabalho', 'Aruak', '02/11', 'Capacidade registrada no Painel de Obras'],
        [B, 'Agendar para terça às 8h a mensagem com a pauta da reunião de papéis', 'Aruak', '02/11', 'Mensagem agendada'],
    ]
    return quadro(rows)

def d7():
    rows = [
        [B, 'Reunião de papéis: cotações e suprimentos, controle de custos, coordenação de campo, apoio técnico de orçamento, cobertura da Gabriela, horas e atribuição do Yan. Ivan e Vicente participam como pretendentes', 'Aruak, Gabriela, Yan, Flávia', '03/11', 'Ata com nomes, horas e alçadas (Painel de Obras)'],
        [B, 'Montar o Scanner no Google Formulários, com o aviso do 193 antes da primeira pergunta', 'Gabriela', '03/11', 'Link funcionando'],
        [B, 'Testar os 11 caminhos no celular; Aruak revisa as rotas técnicas', 'Gabriela e Aruak', '04/11', 'Planilha de teste completa'],
        [R, 'Mensagem ao Alexandre (pronta na frente 3) e visita de medição, se houver interesse', 'Aruak', '04/11', 'Placar: status e data'],
        [C, 'Marcar a apresentação da proposta com a Carmem', 'Aruak', '04/11', 'Data no Placar'],
        [B, 'Perguntar ao CREA-GO sobre ART de rotina para vistoria e laudo, ART da visita e ART anual do condomínio', 'Gabriela', '05/11', 'Resposta escrita'],
        [B, 'Enviar ao contador a pergunta fiscal: 8% por serviço, nota da gestão só sobre o honorário, Tip Toy', 'Gabriela (Ivan, se aceitar)', '05/11', 'Resposta escrita'],
        [R, 'Escolher os 2 escritórios e enviar a mensagem pronta da frente 5', 'Aruak (Ivan, se aceitar)', '06/11', 'Placar: 2 oportunidades “Pré-obra”'],
        [B, 'Abrir outubro de 2026 por produto: receita, custos diretos e lucro bruto, para conferir os R$ 30 mil', 'Gabriela e Flávia', '06/11', 'Planilha de outubro no Mais Controle'],
        [B, 'Primeira reunião semanal de 30 min com Placar, Painel de Obras e Mais Controle', 'Aruak', '06/11', 'Decisões registradas'],
        [B, 'Publicar o Scanner e atualizar o catálogo: 6 coleções com estágio; sem Silver, sem “em Goiânia”, sem selos e sem fotos de banco de imagem', 'Gabriela', '09/11', 'Link no catálogo; primeiro formulário real'],
    ]
    return quadro(rows)

def ate1812():
    rows = [
        [C, 'Proposta do Trípoli apresentada em pessoa, com um plano principal', 'Aruak', '13/11', 'Proposta entregue e data de decisão no Placar'],
        [R, 'Medeiros reconstruída e modelo de honorário decidido para o primeiro contrato', 'Aruak', '13/11', 'Registro com os 4 dados e decisão'],
        [R, 'Apoio técnico de orçamento definido: nome, valor por hora, disponibilidade', 'Aruak', '13/11', 'Painel de Obras'],
        [R, 'Conversa com os 2 arquitetos e 1 projeto real de cada', 'Aruak', '13/11', 'Placar'],
        [B, 'Cláusulas de contratação remota (CDC, art. 49)', 'Vicente, se aceitar', '13/11', 'Minuta'],
        [R, 'Alexandre: sistema e aplicador cotados por escrito, ou decisão de não oferecer preço fechado', 'Suprimentos (definir em 03/11)', '20/11', 'Lista de cotações com status'],
        [R, 'Contrato de gestão e contrato do condomínio', 'Vicente, se aceitar', '20/11', 'Minutas'],
        [R, 'Modelos de ordem de compra, medição, relatório semanal e fechamento no Drive', 'Gabriela', '20/11', 'Pasta de modelos'],
        [R, 'Reunião com o proprietário de cada projeto de pré-obra', 'Aruak e arquitetos', '27/11', 'Sim, não ou data no Placar'],
        [R, 'Teste da Visita Diagnóstica: 5 casos qualificados e decisão', 'Aruak e Gabriela', '30/11', 'Tabela dos 5 casos no Placar'],
        [R, 'Três vistorias cronometradas, com revisão e envio', 'Aruak', '30/11', 'Horas [M] no Painel de Obras'],
        [B, 'Outubro e novembro fechados por produto', 'Gabriela e Flávia (Vicente)', '30/11', 'Mais Controle'],
        [C, 'Trípoli: decisão e primeiro recebimento, se contratado', 'Aruak', '04/12', 'Contrato e 50% no Mais Controle'],
        [R, 'Proposta de pré-obra apresentada', 'Aruak', '04/12', 'Placar'],
        [R, 'Primeira proposta de gestão por honorário mensal apresentada', 'Aruak', '11/12', 'Placar'],
        [B, 'Medição do Scanner: funil e custo por cliente pago', 'Gabriela', '18/12', 'Planilha do formulário'],
        [B, 'Mapa da dívida e proposta de plano', 'Vicente, se aceitar; Aruak', '18/12', 'Documento'],
        [B, 'Revisão por produto: manter, ajustar, suspender ou ampliar, com os três indicadores e o número de contratos medidos', 'Aruak e responsáveis aceitos', '18/12', 'Comparativo atualizado e ata'],
        [B, 'Entregas de Ivan e Vicente verificadas no quadro semanal', 'Aruak', '18/12', 'Quadro semanal'],
    ]
    return quadro(rows)

def build():
    p1 = page('Quadro de ações', 'Trabalho desta semana e até 18/12/2026', 'Duas prioridades: reformas e serviços ligados a elas, e o piloto do condomínio. Amanhã é feriado (Finados): nas próximas 24 horas, só tarefas do Aruak, sem acionar equipe nem clientes.',
        '<h2>Próximas 24 horas</h2>' + h24() + '<h2>Próximos 7 dias (3 a 9/11)</h2>' + d7())
    p2 = page('Quadro de ações', 'Até 18/12/2026', 'Cada ação tem responsável, prazo e evidência em um dos três sistemas. Responsáveis marcados com “se aceitar” dependem da reunião de papéis.',
        ate1812() + box('Ritual de acompanhamento', '<p>Toda sexta, 30 minutos, só com o que existir nos sistemas. <b>Placar:</b> oportunidades qualificadas, propostas apresentadas, sinais recebidos e perdas com motivo. <b>Painel de Obras:</b> capacidade disponível, horas gastas por pessoa e entregas travadas. <b>Mais Controle:</b> recebido, comprometido, pago e pico de caixa por contrato. Cada reunião termina com decisão, responsável e prazo.</p>'))
    return p1 + p2
