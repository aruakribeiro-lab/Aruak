# -*- coding: utf-8 -*-
from common import *

CODES = [
 ('VERMELHO', 'Atenção: seu caso pede cuidado imediato.',
  'Os sinais que você marcou podem indicar risco. Saia do local e mantenha as pessoas longe. Se for elétrico e der para fazer com segurança, desligue o disjuntor daquele circuito. Se houver estalos, trinca aumentando ou queda de material, ligue agora para os Bombeiros: 193. Depois, se quiser, fale com a gente pelo WhatsApp: no horário comercial, casos assim têm prioridade.'),
 ('DIAGNOSTICO', 'Seu caso pede descobrir a causa antes de gastar com conserto.',
  'Se pintar, trocar revestimento ou impermeabilizar sem achar a origem, o problema tende a voltar. O próximo passo indicado é a Visita Diagnóstica: um engenheiro vai ao imóvel, mede, fotografa e entrega por escrito o que foi observado, a causa provável quando houver evidência e o que fazer agora. Antes de agendar, você recebe o valor e as condições por escrito.'),
 ('LAUDO', 'Como você vai precisar mostrar isso a alguém, o caminho indicado é um laudo técnico com ART.',
  'O laudo registra a pergunta, o método, as evidências, a conclusão possível e os seus limites, assinado por engenheiro. Antes da proposta, uma conversa curta define o que o laudo precisa responder e para quem.'),
 ('REPARO', 'Seu banheiro ou cozinha pode ser um caso de renovação sem quebradeira.',
  'Para dizer se cabe, com preço fechado e as datas de início, de fim dos trabalhos e de volta ao uso, precisamos ver e medir o ambiente. Se aparecer vazamento ou infiltração, primeiro descobrimos a causa.'),
 ('VISTORIA', 'O que não estiver registrado no recebimento fica mais difícil de cobrar depois.',
  'Fazemos a vistoria de recebimento com checklist e entregamos o relatório fotográfico com ART, pronto para enviar à construtora. São mais de 100 vistorias entregues.'),
 ('COMPRA', 'Antes de assinar, vale ver o que não aparece na visita do corretor.',
  'Vistoriamos o imóvel usado e entregamos por escrito o que precisa de reparo, para você negociar com informação.'),
 ('PREOBRA', 'Antes de começar, descubra se o projeto cabe na sua verba.',
  'Fazemos o estudo de viabilidade ou o orçamento executivo com preços reais de mercado e o plano da obra, junto com o seu arquiteto.'),
 ('GESTAO', 'Para retomar ou começar com segurança, primeiro é preciso saber o que foi feito, o que falta e quanto custa terminar.',
  'Depois, coordenamos a obra com compras aprovadas por você, pagamento só do que foi medido e relatório semanal. O dinheiro da obra fica com você.'),
 ('SINDICO', 'O síndico responde pela conservação do prédio.',
  'Comece pelo Dossiê do Prédio, gratuito: levantamos o que a lei e as normas pedem do seu prédio e o que precisa ser confirmado nos documentos.'),
]

def comercial():
    blocos = [
        ('O problema', '<p>Trinca, infiltração, vazamento, banheiro velho, obra parada ou imóvel novo para receber, e você não sabe por onde começar, quem chamar nem quanto vale gastar agora.</p>'),
        ('Como funciona', ol(['Você responde perguntas simples pelo celular, em cerca de três minutos.', 'A tela mostra o caminho indicado para o seu caso e um código.', 'Se quiser, você chama a gente no WhatsApp com esse código e combinamos o próximo passo.'])),
        ('O que você recebe', ul(['Orientação inicial para o tipo de situação que você marcou, com o que fazer e o que evitar agora.', 'Atendimento da nossa equipe pelo WhatsApp em horário comercial, de segunda a sexta, das 8h às 17h30.', 'Se o próximo passo tiver custo, o valor e as condições chegam por escrito antes de qualquer agendamento.'])),
        ('O que o Scanner não é', ul(['Não é avaliação técnica e não substitui a vistoria de um engenheiro.', 'Não damos diagnóstico por foto.', '<b>Risco imediato</b> (estalos, trinca aumentando, teto cedendo, cheiro de queimado, água perto de tomada ou quadro, reboco caindo): saia do local, isole a área e ligue <b>193</b>.'])),
        ('Seus dados', '<p>Usamos suas respostas só para falar com você sobre este caso. A autorização de contato fica no próprio formulário.</p>'),
        ('Para quem é', '<p>Moradores, quem vai comprar ou receber um imóvel, quem vai reformar ou construir e síndicos de prédios em Goiânia.</p>'),
    ]
    preco = '<table><tr><td>Scanner da Obra</td><td class="v">Grátis</td></tr><tr><td>Compromisso</td><td class="v">Nenhum</td></tr></table><p>Visita, vistoria, laudo ou estudo, quando indicados, têm valor informado por escrito antes do agendamento.</p>'
    prox = '<p>Acesse o Scanner pelo link <b>[link do formulário]</b>, pelo QR code ou pela bio do Instagram.</p><p>Prefere conversar? Chame no WhatsApp (62) 98170-8669 e escreva “Scanner”.</p>'
    return client_page('Frente 1 · página comercial', 'Scanner da Obra',
        'Responda algumas perguntas sobre o seu imóvel e veja, na hora, qual é o próximo passo adequado ao seu caso.',
        blocos, preco, prox, 'Orientação inicial automática, com base nas respostas do cliente. Não é avaliação técnica nem substitui a vistoria.')

def ficha():
    resp = table(['Papel', 'Pessoa', 'Observação'], [
        ['Dono do formulário e da planilha', 'Gabriela ' + tag('P'), 'Monta, testa uma vez por mês e mede'],
        ['Revisão técnica das rotas e textos', 'Aruak', 'Antes de publicar e a cada mudança'],
        ['Atendimento dos códigos', 'Gabriela ' + tag('P'), 'Segunda a sexta, 8h às 17h30; resposta em até 1 hora útil'],
        ['Cobertura nas ausências da Gabriela', '<span class="tg">[pendente de decisão]</span>', 'Sugestão: Flávia, só com as mensagens deste manual e sem opinião técnica'],
        ['Casos vermelhos, laudo e processo', 'Aruak', 'Retorno ao cliente depois da orientação de segurança'],
        ['Registro e medição', 'Gabriela', 'Placar no mesmo dia; números na reunião de sexta'],
    ], widths=['32%', '22%', '46%'])
    horas = table(['Tarefa', 'Gabriela', 'Aruak', 'Origem'], [
        ['Triagem por contato (perguntas, condição, agendamento, Placar)', '15 min', '0', tag('E')],
        ['Código vermelho (orientação e retorno)', '10 min', 'até 15 min', tag('E')],
        ['Laudo ou processo (dimensionar finalidade e escopo)', '10 min', 'até 15 min', tag('E')],
        ['Montagem inicial do formulário', '2 h', '1 h de revisão', tag('E')],
        ['Teste mensal dos nove caminhos', '30 min', '0', tag('P')],
    ], widths=['56%', '14%', '16%', '14%'])
    seq = ol([
        'Cliente responde o formulário e vê a saída com o código e o botão do WhatsApp.',
        'Gabriela responde em até 1 hora útil com a mensagem padrão e as perguntas do código.',
        'Qualifica: decisor identificado, fotos ou dados recebidos, nenhum eliminatório, condição do próximo passo aceita.',
        'Informa a condição por escrito e oferece dois horários (ou passa ao Aruak nos códigos de laudo, pré-obra, gestão e síndico).',
        'Registra no Placar no mesmo dia: código, origem, horários, qualificação, condição, próximo passo e resultado.',
        'Sem resposta: uma mensagem no dia útil seguinte; depois, uma ligação; depois, encerra como “sem retorno” com data de recontato em 60 dias.',
    ])
    riscos = table(['Risco', 'Como tratar'], [
        ['Cliente em risco espera resposta', 'Aviso do 193 antes da primeira pergunta e na saída vermelha; contato só depois da orientação'],
        ['Orientação técnica por WhatsApp sem vistoria', 'Gabriela não opina; Aruak só orienta segurança e encaminha'],
        ['Todo diagnóstico vira “só um orçamento”', 'Regra objetiva da gratuidade (página do roteiro)'],
        ['Promessa de 1 hora útil sem cobertura', 'Definir cobertura antes de divulgar; resposta automática fora do horário'],
        ['Dados pessoais', 'Consentimento obrigatório; planilha com acesso só de Gabriela e Aruak'],
        ['Link quebrado ou rota errada', 'Teste mensal dos nove caminhos no celular'],
    ], widths=['38%', '62%'])
    dinheiro = table(['Item', 'Valor', 'Conta'], [
        ['Custo por contato', brl(SC_CONTATO, True), '15 min × R$ 35/h'],
        ['Custo por venda, 1 em cada 5 contatos', brl(SC_VENDA20, True), '5 contatos × R$ 8,75'],
        ['Custo por venda, se o contato vencedor já está no administrativo do produto', brl(SC_VENDA_INC, True), '4 contatos perdidos × R$ 8,75'],
        ['Exceções do Aruak', 'R$ 100/h', 'Somar ao custo do mês'],
        ['Desembolso do formulário', 'R$ 0', 'Google Formulários gratuito'],
    ], 'num', widths=['56%', '16%', '28%'])
    crit = table(['Depois de 30 formulários concluídos', 'Decisão'], [
        ['Vendas pagas de 20% ou mais dos formulários', '<b>Manter</b> e divulgar mais: bio, status, clientes antigos, QR nas obras'],
        ['De 10% a menos de 20%', '<b>Ajustar</b> perguntas e textos da etapa em que mais se perde gente'],
        ['Menos de 10%', '<b>Restringir</b> a indicados e clientes antigos; revisar canal e público'],
        ['Custo por cliente pago acima de R$ 60, ou Aruak mais de 1 h por semana em exceções', '<b>Ajustar</b> rotas e mensagens antes de divulgar'],
    ], widths=['52%', '48%'])
    corpo = ('<div class="two"><div><h2>Responsáveis</h2>' + resp + '</div><div><h2>Horas por pessoa</h2>' + horas + '</div></div>'
             '<h2>Sequência de execução</h2>' + seq +
             '<h2>Aceite: como provar que o Scanner funcionou</h2><p>Cada código recebido aparece no Placar no mesmo dia útil, com hora de chegada, hora da primeira resposta, qualificação, condição informada, próximo passo com data e resultado: pago, em decisão ou perdido com motivo.</p>'
             '<div class="two"><div><h2>Riscos</h2>' + riscos + '</div><div><h2>Margem e caixa</h2>' + dinheiro + '</div></div>'
             '<h2>Pagamento e aquisição</h2><p>Grátis para o cliente. Divulgação sem mídia paga até o resultado dos 30 formulários: bio do Instagram, status, catálogo do WhatsApp, clientes antigos, cartão e QR code nas obras. O Scanner não é produto de margem: o custo por venda entra como aquisição no produto vendido. Os R$ 157 de versões anteriores eram de outro processo, com o Aruak analisando fotos.</p>'
             '<h2>Critério para manter, ajustar ou suspender</h2>' + crit +
             '<p class="small">Seis vendas em 30 formulários autorizam continuar o teste. Investir em divulgação depende do custo e do saldo dessas vendas. Clientes ainda em decisão ficam separados na conta.</p>')
    return page('Frente 1 · ficha interna', 'Scanner da Obra · ficha interna', 'Triagem gratuita que encaminha o cliente ao próximo atendimento e mede quanto custa gerar uma venda.', corpo)

def formulario():
    s1 = table(['Opção (múltipla escolha, obrigatória)', 'Vai para'], [
        ['Trinca ou rachadura', 'Seção 2'], ['Infiltração, mofo ou umidade', 'Seção 2'], ['Vazamento', 'Seção 2'],
        ['Piso ou revestimento soltando', 'Seção 2'], ['Problema na parte elétrica', 'Seção 2'],
        ['Quero renovar banheiro ou cozinha', 'Seção 4'], ['Vou receber um imóvel novo', 'Resultado VISTORIA'],
        ['Vou comprar um imóvel usado', 'Resultado COMPRA'], ['Quero reformar ou construir e tenho projeto ou arquiteto', 'Resultado PRÉ-OBRA'],
        ['Minha obra está parada ou tenho problema com empreiteiro', 'Resultado GESTÃO'], ['Sou síndico ou cuido de um prédio', 'Resultado SÍNDICO'],
    ], 'sm', widths=['68%', '32%'])
    s2 = table(['Você percebe algum destes sinais agora?', 'Vai para'], [
        ['Trinca aumentando, ou trinca em viga, pilar ou laje', 'Resultado VERMELHO'],
        ['Teto, laje ou piso cedendo', 'Resultado VERMELHO'],
        ['Cheiro de queimado, fio esquentando ou disjuntor desarmando quando molha', 'Resultado VERMELHO'],
        ['Pedaço de reboco, revestimento ou fachada caindo', 'Resultado VERMELHO'],
        ['Água escorrendo perto de tomada ou quadro de luz', 'Resultado VERMELHO'],
        ['Não sei dizer', 'Seção 3'], ['Nenhum destes', 'Seção 3'],
    ], 'sm', widths=['68%', '32%'])
    s3 = table(['Pergunta', 'Opções', 'Vai para'], [
        ['Há quanto tempo isso acontece?', 'Menos de 1 mês · 1 a 6 meses · Mais de 6 meses · Não sei', 'continua'],
        ['Já tentaram consertar e o problema voltou?', 'Sim · Não · Nunca tentamos', 'continua'],
        ['Você vai precisar mostrar isso a alguém, como construtora, vizinho, condomínio, seguradora, advogado ou Justiça?', 'Sim', 'Resultado LAUDO'],
        ['', 'Não · Não sei', 'Resultado DIAGNÓSTICO'],
    ], 'sm', widths=['46%', '34%', '20%'])
    s4 = table(['Nesse ambiente existe vazamento, infiltração, mancha de umidade ou mofo?', 'Vai para'], [
        ['Sim', 'Resultado DIAGNÓSTICO'], ['Não', 'Resultado REPARO'], ['Não sei', 'Resultado REPARO (a Gabriela confirma pelas fotos)'],
    ], 'sm', widths=['60%', '40%'])
    dados = table(['Seção final · Seus dados (todas as saídas chegam aqui)', 'Tipo'], [
        ['Nome', 'Resposta curta, obrigatória'], ['WhatsApp com DDD', 'Resposta curta, obrigatória, validação de número'],
        ['Bairro e cidade', 'Resposta curta, obrigatória'],
        ['Como conheceu o Scanner', 'Instagram · Status do WhatsApp · Catálogo · Indicação · Já sou cliente · Outro'],
        ['Autorizo a Entre Colunas a falar comigo pelo WhatsApp sobre este caso e a guardar estas respostas para esse atendimento.', 'Caixa de seleção, obrigatória'],
    ], 'sm', widths=['70%', '30%'])
    topo = box('Descrição do formulário (aparece antes da primeira pergunta)',
        '<p><b>Se existe risco agora</b> (estalos, trinca aumentando, teto ou laje cedendo, cheiro de queimado, fio esquentando, água perto de tomada ou quadro de luz, reboco ou fachada caindo): <b>saia do local, mantenha as pessoas longe e ligue 193 (Bombeiros).</b> Não espere este formulário.</p>'
        '<p>Responda em cerca de 3 minutos e veja qual é o próximo passo adequado ao seu imóvel. Grátis e sem compromisso. É uma orientação inicial automática, com base nas suas respostas, e não substitui a vistoria de um engenheiro.</p>', 'red')
    cfg = ul(['Título: <b>Scanner da Obra · Entre Colunas</b>. Barra de progresso ligada. Não coletar e-mail nem exigir login.',
              'Cada bloco abaixo é uma seção. Nas perguntas com desvio, usar “Ir para a seção com base na resposta”.',
              'Seção 1 começa com <b>Tipo de imóvel</b> (Casa · Apartamento · Comercial · Área comum de condomínio), sem desvio, e depois <b>O que você precisa?</b>, com desvio.',
              'Cada resultado é uma seção própria com o texto, o link do WhatsApp e uma pergunta obrigatória de opção única, <b>“Seu código”</b>, com o código daquela saída. É ela que grava a rota na planilha.',
              'Depois de qualquer resultado, ir para a seção final <b>Seus dados</b> e então Enviar. Os dados de contato vêm por último, depois da orientação.',
              'Mensagem de confirmação: “Recebemos suas respostas. Se ainda não chamou no WhatsApp, use o botão da tela anterior ou escreva para (62) 98170-8669 com o seu código.”'])
    corpo = (cfg + topo + '<div class="two"><div><h3>Seção 1 · O que você precisa?</h3>' + s1 + '<h3>Seção 4 · Banheiro ou cozinha</h3>' + s4 +
             '</div><div><h3>Seção 2 · Sinais de atenção</h3>' + s2 + '<h3>Seção 3 · Sobre o problema</h3>' + s3 + '</div></div>' + dados)
    return page('Frente 1 · formulário', 'O formulário, pronto para montar', 'Copiar no Google Formulários na ordem abaixo. O aviso de emergência vem antes de qualquer pergunta e os dados de contato vêm por último.', corpo)

def saidas():
    rows = []
    for code, tit, txt in CODES:
        rows.append([f'<b>SCN-{code}</b>', f'<b>{tit}</b> {txt}<br><span class="mono">{WA}{code}</span>'])
    t = table(['Código', 'Texto exibido na tela e link do botão do WhatsApp'], rows, 'sm', widths=['15%', '85%'])
    rod = box('Rodapé em todas as saídas', '<p>Orientação inicial automática, com base nas suas respostas. Não é avaliação técnica e não substitui a vistoria. Para registrar seu caso, clique em Próxima e envie seus dados.</p>')
    nota = ('<p class="small">O 199 da Defesa Civil só entra no texto depois de confirmado o canal de Goiânia. O texto da vistoria não usa “em Goiânia” até a contagem das 100 vistorias ser separada por cidade. '
            'A mensagem que chega ao WhatsApp é: “Fiz o Scanner. Código: SCN-...”.</p>')
    return page('Frente 1 · nove saídas', 'As nove saídas e o encaminhamento ao WhatsApp', 'Cada saída mostra um texto curto, o código e o botão que abre o WhatsApp com a mensagem pronta.', t + rod + nota)

def roteiro():
    perg = table(['Código', 'Perguntas da Gabriela', 'Condição informada por escrito', 'Segue para'], [
        ['VERMELHO', 'Nenhuma. Ligar na hora (protocolo ao lado)', 'Orientação de segurança; retorno do Aruak', 'Aruak'],
        ['DIAGNÓSTICO', 'Me conta com as suas palavras o que está acontecendo · 3 fotos: de longe, de perto e da parede ou teto ao lado · Quem decide junto com você? · Existe discussão com vizinho, construtora ou seguro?', 'Visita Diagnóstica de R$ 1.200, paga antes do agendamento, nota em até 2 dias úteis', 'Agenda da Gabriela'],
        ['LAUDO', 'As mesmas, mais: para quem o documento vai e até quando? Já existe processo?', 'Conversa de 15 min com o Aruak; laudo a partir de R$ 3.000, 50% na contratação', 'Aruak'],
        ['REPARO', '3 fotos (geral, piso e parede do box) · É o único banheiro da casa? · Tem mancha, cheiro de mofo ou rejunte escuro perto do ralo? · Existe data que precisa ser respeitada? · Quem decide?', 'Visita de medição gratuita de até 1 h, só com solução definida. Mancha ou mofo: Visita Diagnóstica', 'Agenda do Aruak'],
        ['VISTORIA e COMPRA', 'Metragem privativa · Data das chaves ou da assinatura · Endereço ou empreendimento · Recebimento de novo ou compra de usado?', 'Valor da tabela pela metragem; pagamento na confirmação do agendamento ' + tag('P'), 'Agenda da Gabriela'],
        ['PRÉ-OBRA e GESTÃO', 'Tem projeto? Quem é o arquiteto? · Para quando? · Já tem uma faixa de investimento? · Dinheiro próprio ou financiamento? · Quem decide?', 'Conversa de 30 min com o Aruak', 'Aruak'],
        ['SÍNDICO', 'Nome e endereço do condomínio · Unidades e idade do prédio · Último susto · Quem aprova: síndico, conselho ou assembleia?', 'Dossiê do Prédio gratuito; conversa com o Aruak', 'Aruak'],
    ], 'sm', widths=['12%', '44%', '30%', '14%'])
    regra = box('Regra da gratuidade ' + tag('P'),
        '<p>Se o cliente pede que a empresa <b>investigue a causa ou indique uma intervenção</b>, o próximo passo é a Visita Diagnóstica paga. Se a <b>solução já está definida</b> e a empresa só precisa verificar se consegue orçar um reparo, cabe a visita de medição gratuita, de até 1 hora, com o custo registrado no Placar.</p>')
    nunca = box('A Gabriela nunca', ul(['dá opinião técnica, diz “não é nada” ou “pode usar”;', 'passa faixa de preço de reforma ou prazo de obra;', 'promete horário fora da agenda confirmada;', 'pede dados além dos necessários para o caso.']), 'warn')
    elim = '<p class="small"><b>Não passa no filtro:</b> quer laudo com a conclusão pronta, quer conclusão por foto, quer preço fechado em obra com demolição, quer que a empresa compre com o dinheiro dela, quer “só a ART”, ou já brigou com dois ou mais profissionais na mesma obra.</p>'
    m1 = msg('''Oi, [nome], boa tarde. Aqui é a Gabriela, da Entre Colunas. Recebi o seu código do Scanner, obrigada por responder.

Para deixar tudo certo com o engenheiro, posso te fazer três perguntas rápidas por aqui?''')
    m2 = msg('''[Nome], pelo que você me mandou, antes de qualquer conserto vale descobrir de onde isso vem. Se pintar ou trocar sem achar a causa, a chance de voltar é grande.

O Aruak faz uma visita de até uma hora e meia, mede a umidade, fotografa e te manda por escrito, em até dois dias úteis, o que foi observado, a causa provável quando houver evidência e o que fazer agora. O material é seu, mesmo se você contratar outra pessoa para o conserto.

A visita custa R$ 1.200, paga antes do agendamento. Fica melhor para você [dia] de manhã ou [dia] à tarde?''')
    m3 = msg('''[Nome], vi as fotos do banheiro. Pelo que aparece, pode ser um caso de renovação sem quebradeira, mas o preço e as datas só saem depois de medir.

O Aruak passa aí para medir e testar o revestimento, em até uma hora, sem custo. Depois ele te apresenta a proposta com o valor fechado e as datas de início, de fim dos trabalhos e de volta ao uso.

Consigo [dia] às [hora] ou [dia] às [hora]. Qual fica melhor?''')
    m4 = msg('''[Nome], bom dia. Ficou alguma coisa da visita que eu possa adiantar por aqui?

Se preferir, seguro o horário de [dia] para você até amanhã às 12h. Depois disso libero para outro cliente.''')
    corpo = (perg + '<div class="two"><div>' + regra + '</div><div>' + nunca + '</div></div>' + elim +
             '<div class="two"><div><h3>Primeira resposta (até 1 hora útil)</h3>' + m1 + '<h3>Retomada sem resposta (dia útil seguinte)</h3>' + m4 + '</div>'
             '<div><h3>Oferta da visita (DIAGNÓSTICO)</h3>' + m2 + '</div></div>'
             '<div class="two"><div><h3>Visita de medição (REPARO)</h3>' + m3 + '</div><div>'
             '<p class="small" style="margin-top:6mm">Mensagens no padrão do Aruak: sem travessão, parágrafos curtos, um próximo passo no fim. O que estiver entre colchetes é preenchido antes de enviar. A Gabriela assina como ela mesma; as mensagens do Aruak saem do celular dele.</p></div></div>')
    return page('Frente 1 · roteiro', 'Roteiro da Gabriela', 'Responder em até 1 hora útil, fazer só as perguntas do código, informar a condição por escrito e terminar com dois horários ou com a passagem ao Aruak.', corpo)

def urgencias_teste():
    urg = table(['Quando', 'O que fazer', 'Quem e prazo', 'Registro'], [
        ['Antes de qualquer contato', 'Aviso do 193 no topo do formulário e na saída vermelha', 'Automático', '—'],
        ['Código VERMELHO no horário comercial', 'Ligar. Perguntar se há alguém no local. Orientar: sair, isolar, desligar o circuito se for seguro e ligar 193 se houver estalo, trinca aumentando ou queda. Avisar o Aruak por telefone', 'Gabriela em até 15 min ' + tag('P'), 'Placar, etapa Vermelho: hora de chegada, hora do contato, orientação dada'],
        ['Depois da orientação', 'Aruak retorna, orienta e, se necessário, agenda visita prioritária, paga antes, com o valor da Visita Diagnóstica', 'Aruak em até 2 horas úteis ' + tag('P'), 'Encaminhamento e data'],
        ['Fora do horário', 'Resposta automática do WhatsApp Business: “Recebemos sua mensagem e respondemos no próximo horário útil. Se houver risco agora, saia do local e ligue 193.”', 'Gabriela no primeiro horário útil', 'Hora de chegada'],
        ['Nunca', 'Diagnóstico a distância, liberar uso do ambiente ou ir ao local sem contrato, salvo decisão do Aruak', '—', '—'],
    ], 'sm', widths=['16%', '46%', '18%', '20%'])
    paths = [
        ('VERMELHO', 'Trinca ou rachadura → Trinca aumentando'), ('DIAGNOSTICO', 'Infiltração → Nenhum destes → Não'),
        ('LAUDO', 'Vazamento → Nenhum destes → Sim'), ('REPARO', 'Renovar banheiro ou cozinha → Não'),
        ('VISTORIA', 'Vou receber um imóvel novo'), ('COMPRA', 'Vou comprar um imóvel usado'),
        ('PREOBRA', 'Reformar ou construir com projeto'), ('GESTAO', 'Obra parada ou problema com empreiteiro'), ('SINDICO', 'Sou síndico'),
    ]
    teste = table(['#', 'Caminho a marcar', 'Código esperado', 'Aviso antes', 'Texto certo', 'WhatsApp com código', 'Linha gravada', 'Tempo ≤ 3 min'],
        [[str(i + 1), p, f'SCN-{c}', '<span class="sq"></span>', '<span class="sq"></span>', '<span class="sq"></span>', '<span class="sq"></span>', '<span class="sq"></span>'] for i, (c, p) in enumerate(paths)]
        + [['10', 'Trinca → Não sei dizer → Não', 'SCN-DIAGNOSTICO', '<span class="sq"></span>', '<span class="sq"></span>', '<span class="sq"></span>', '<span class="sq"></span>', '<span class="sq"></span>'],
           ['11', 'Renovar banheiro → Sim', 'SCN-DIAGNOSTICO', '<span class="sq"></span>', '<span class="sq"></span>', '<span class="sq"></span>', '<span class="sq"></span>', '<span class="sq"></span>']],
        'sm check', widths=['4%', '34%', '17%', '9%', '9%', '10%', '9%', '8%'])
    obs = '<p class="small">Fazer em um Android e em um iPhone, com dados móveis. Quem testou, data e falhas encontradas vão na própria planilha. Repetir todo mês e sempre que um texto mudar.</p>'
    # exemplo de medição
    form, wa, qual, cond, pagos, decid = 30, 18, 12, 9, 6, 3
    g_min = wa * 15; a_min = 30
    custo = r2(g_min / 60 * ADM + a_min / 60 * AR)
    cpp = r2(custo / pagos)
    vendas = [('Visita Diagnóstica', 2, V1200), ('Vistoria 101 a 249 m²', 3, VI['meio'][0]), ('Laudo', 1, L3000)]
    rec = sum(e.receita * q for _, q, e in vendas)
    disp = r2(sum((e.disp - cpp) * q for _, q, e in vendas))
    hrs = sum(e.h * q for _, q, e in vendas)
    funil = table(['Etapa', 'Quantidade', 'Taxa'], [
        ['Formulários concluídos', str(form), '100%'], ['Chamaram no WhatsApp', str(wa), pct(wa / form, 0)],
        ['Qualificados', str(qual), pct(qual / form, 0)], ['Receberam condição por escrito', str(cond), pct(cond / form, 0)],
        ['Pagaram', str(pagos), pct(pagos / form, 0)], ['Ainda decidindo (fora da conta)', str(decid), '—'],
    ], 'num', widths=['56%', '20%', '24%'])
    custos = table(['Conta do mês', 'Valor'], [
        [f'Gabriela: {wa} contatos × 15 min = {hh(g_min/60)} × R$ 35', brl(g_min / 60 * ADM, True)],
        ['Aruak: 2 exceções × 15 min = 0,5 h × R$ 100', brl(a_min / 60 * AR, True)],
        {'cls': 'tot', 'cells': ['Custo humano do Scanner', brl(custo, True)]},
        {'cls': 'tot', 'cells': [f'÷ {pagos} clientes pagos = custo por cliente pago', brl(cpp, True)]},
        [f'Receita das {pagos} vendas (2 visitas, 3 vistorias, 1 laudo)', brl(rec)],
        ['Disponível dessas vendas, já com a aquisição real', brl(disp, True)],
        [f'Horas do Aruak nessas vendas: {hh(hrs)} → disponível por hora', brl(r2(disp / hrs), True)],
    ], 'num', widths=['74%', '26%'])
    planilha = '<p class="small"><b>Colunas que a Gabriela acrescenta à planilha do formulário:</b> origem · chamou no WhatsApp · hora da 1ª resposta · qualificado (S/N e motivo) · condição informada · próximo passo e data · pagou · produto · valor · minutos da Gabriela · minutos do Aruak.</p>'
    corpo = ('<h2>Situações urgentes</h2>' + urg + '<h2>Teste no celular antes de divulgar</h2>' + teste + obs +
             '<h2>Medição do custo por cliente pago · exemplo ' + tag('S') + '</h2>' + planilha +
             '<div class="two"><div>' + funil + '<p class="small">Decisão do exemplo: 6 de 30 é 20%, faixa “manter”. O custo por cliente pago ficou abaixo dos R$ 43,75 da premissa.</p></div><div>' + custos + '</div></div>')
    return page('Frente 1 · urgências, teste e medição', 'Urgência, teste no celular e custo por cliente pago', 'Em risco imediato, o cliente não espera foto analisada nem retorno. Antes de divulgar, os nove caminhos são testados no celular.', corpo)

def build():
    return comercial() + ficha() + formulario() + saidas() + roteiro() + urgencias_teste()
