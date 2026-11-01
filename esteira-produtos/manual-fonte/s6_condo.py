# -*- coding: utf-8 -*-
from common import *

SQ = '<span class="sq"></span>'

def comercial():
    blocos = [
        ('O ponto de partida', '<p>Um prédio de 1992 já passou da vida útil de projeto de vários sistemas, e o Trípoli trocou o gás de cozinha pelo elétrico. A responsabilidade pela conservação é da síndica (Código Civil, art. 1.348). O Dossiê do Prédio já mostrou o retrato inicial.</p>'),
        ('Implantação, uma vez', '<p>Transforma o levantamento inicial em base de gestão: cadastro de sistemas e fornecedores, documentos recebidos e faltantes, calendário de vencimentos com datas reais, plano anual de manutenção (ABNT NBR 5674), prioridades com responsável e prazo e o plano de 90 dias apresentado à síndica, com ART.</p>'),
        ('Acompanhamento mensal', ul(['<b>Essencial:</b> 1 visita programada por mês, relatório mensal, calendário atualizado, 1 demanda de cotação com até 3 propostas comparadas e até 4 consultas por WhatsApp em horário comercial.',
            '<b>Completo:</b> 2 visitas por mês, com verificação do que foi encaminhado, 2 demandas de cotação e até 8 consultas.'])),
        ('O que não está incluído', ul(['Execução de obras: durante o piloto, não executamos obras no condomínio assessorado.', 'Fiscalização de obra ou serviço de terceiros.',
            'Laudos com ART própria (inspeção predial, elétrica, SPDA, incêndio, fachada), com proposta específica.', 'Emergência fora do horário comercial.',
            'A ronda visual não abre painel energizado e não substitui laudo.'])),
        ('Quem decide', '<p>Contratar, fiscalizar e aceitar fornecedores continua com o condomínio. Nós observamos, orientamos, registramos e alertamos por escrito. O relatório é do condomínio.</p>'),
        ('Contrato', '<p>12 meses, sem fidelidade e sem multa: qualquer parte encerra com aviso de 30 dias. Reajuste anual pelo IPCA. Fotos só para os usos autorizados.</p>'),
    ]
    preco = ('<table><tr><td>Implantação (50% na assinatura, 50% na entrega do plano de 90 dias)</td><td class="v">R$ 2.600</td></tr>'
             '<tr><td>Essencial</td><td class="v">R$ 1.600/mês</td></tr><tr><td>Completo</td><td class="v">R$ 2.200/mês</td></tr></table>'
             '<p>Condição de piloto: [preencher com o que foi combinado com a síndica antes desta proposta]. Valores cheios escritos.</p>')
    prox = ('<p>Escolher entre começar pela implantação e decidir o plano mensal na entrega do plano de 90 dias, ou contratar a implantação com o plano mensal desde já.</p>'
            '<p>Apresentação à síndica em [data]; assembleia em [data], se necessária.</p>')
    return client_page('Frente 6 · página comercial · proposta para o Edifício Trípoli', 'Engenheiro do Condomínio',
        'A síndica deixa de achar que o prédio está em dia e passa a mostrar o que está em dia: calendário do que vence, prioridades com responsável e prazo e relatório curto para a assembleia, assinado por engenheiro.',
        blocos, preco, prox)

def ficha():
    prom = table(['O que já foi dito à Carmem', 'Fonte', 'Como o manual preserva', 'Situação'], [
        ['Dossiê do Prédio por fonte pública, gratuito', 'Dossiê de 16/10', 'Base da implantação', 'Entregue'],
        ['Vistoria gratuita de 2 h e dossiê completo em 5 dias úteis', 'Roteiro de 16/10', 'Cumprir antes da proposta; o que for reaproveitado entra uma vez como custo de aquisição', '<span class="tg">[confirmar]</span>'],
        ['Alerta de Vencimentos gratuito, até 15 obrigações', 'Roteiro', 'Oferecido se ela não contratar', 'Disponível'],
        ['“Proposta clara, sem fidelidade”', 'Dossiê', '12 meses, sem multa, aviso de 30 dias', 'Preservado'],
        ['“Não executamos obras dentro da assessoria mensal. O relatório é do condomínio, não de quem quer vender serviço.”', 'Dossiê', 'Sem venda de execução ao condomínio durante o piloto', 'Preservado'],
        ['O valor vem como “fração pequena da arrecadação”', 'Roteiro', 'Mostrar o percentual com a arrecadação real', '<span class="tg">[arrecadação]</span>'],
        ['Piloto “com desconto e valor cheio escrito, nunca gratuito”; o arquivo 09 fala em 30% nas 3 primeiras mensalidades', 'Roteiro (Q6) e arquivo 09', 'Valores cheios na proposta; condição de piloto igual ao que foi dito', '<span class="tg">[pendente]</span>'],
        ['Fotos só com autorização', 'Roteiro', 'Cláusula de dados e uso de imagem separada', 'Preservado'],
    ], 'sm', widths=['36%', '14%', '34%', '16%'])
    regra = box('Decisão para o Trípoli: assinatura ou implantação primeiro', '<p>Pergunta-chave à Carmem: <b>“Depois que resolvermos a primeira lista de problemas, que decisão você ainda vai precisar tomar todo mês com a ajuda de um engenheiro?”</b> Se ela tiver decisões mensais recorrentes, aprovar a frequência e indicar quem autoriza a despesa: apresentar a assinatura. Se a necessidade for organizar documentos e priorizar intervenções: oferecer a implantação avulsa e combinar a revisão na entrega do plano. Antes de qualquer valor, recuperar o que foi prometido sobre desconto. Se nada foi prometido, não dar desconto; se foram 30% nas 3 primeiras mensalidades, honrar (custo de R$ 1.440 no Essencial).</p>')
    comp = table(['', 'Implantação', 'Essencial', 'Completo'], [
        ['Presença', '2 idas de levantamento complementar e reunião de entrega', '1 visita programada por mês', '2 visitas por mês'],
        ['Entrega', 'Inventário, documentos, calendário, plano anual, plano de 90 dias, ART', 'Relatório mensal, calendário, pendências com responsável', 'Idem, com o que evoluiu entre as visitas'],
        ['Cotações', '—', '1 demanda por mês, até 3 propostas', '2 demandas por mês'],
        ['Consultas por WhatsApp', '—', 'Até 4 por mês, resposta em 1 dia útil', 'Até 8 por mês'],
        ['Preço', 'R$ 2.600, 50% e 50%', 'R$ 1.600 por mês', 'R$ 2.200 por mês'],
    ], 'sm', widths=['16%', '30%', '27%', '27%'])
    horas = table(['Horas por mês ' + tag('E'), 'Aruak', 'Yan', 'Adm', 'Idas'], [
        ['Essencial, Aruak sozinho no campo', '6,5 h', '—', '3 h', '1'], ['Essencial em supervisão (meses 1 a 3)', '5 h', '6,25 h', '3 h', '1'],
        ['Essencial, Yan no campo após a passagem', '2 h', '6,25 h', '3 h', '1'], ['Completo, Aruak sozinho no campo', '10 h', '—', '3 h', '2'],
        ['Completo em supervisão', '8 h', '11 h', '3 h', '2'], ['Completo, Yan no campo', '3 h', '11 h', '3 h', '2'],
        ['Implantação (uma vez), com o Yan', '8 h', '8 h', '2 h', '2'], ['Implantação, Aruak sozinho', '14 h', '—', '2 h', '2'],
    ], 'sm', widths=['46%', '13%', '13%', '13%', '15%'])
    resp = '<p class="small"><b>Responsáveis:</b> relacionamento e proposta, Aruak · campo nos meses 1 a 3, Aruak e Yan juntos · depois da passagem, Yan · relatório, Yan rascunha e Aruak revisa e assina · calendário e Alerta de Vencimentos, Gabriela · cobrança, NF e ART anual, Gabriela · Mais Controle, Flávia. A v5 estimava 8 h do Yan no Completo; este manual usa 11 h, coerente com as 6,25 h de uma visita do Essencial.</p>'
    p1 = page('Frente 6 · ficha interna', 'Engenheiro do Condomínio · ficha interna', 'O Trípoli testa se a síndica precisa de acompanhamento contínuo depois de receber o primeiro plano.',
        '<h2>O que foi prometido à Carmem</h2>' + prom + regra + '<h2>Implantação, Essencial e Completo</h2>' + comp + '<h2>Horas por pessoa</h2>' + horas + resp)
    seq = ol(['Recuperar as 4 informações da reunião de 16/10 (o que ela precisa decidir, quantas visitas isso exige, quem aprova, o que disse sobre valor) e o desconto prometido.',
              'Apresentar em pessoa um plano principal, com um preço e um escopo.', 'Assinatura e 50% da implantação; registro da ART anual depois da entrada.',
              'Implantação em 4 semanas: pasta de documentos, levantamento complementar, cadastro, calendário, plano anual e plano de 90 dias.',
              'Reunião de entrega do plano: 50% restantes e, na assinatura, primeira mensalidade.', 'Rotina mensal: visita, relatório, cotações, alertas.',
              'Dia 90: reunião de avaliação com a síndica.', 'Passagem do campo ao Yan pela regra de delegação.'])
    riscos = table(['Risco', 'Tratamento'], [
        ['Troca de síndico (contrato sem fidelidade)', 'Avatar com mandato de 12 meses ou mais; relatório útil para o conselho'],
        ['Arrecadação baixa para a mensalidade', 'Confirmar a arrecadação real (o dossiê estima de R$ 15 mil a R$ 35 mil)'],
        ['Escopo crescendo pelo WhatsApp', 'Limites escritos; o que passar vira visita extra autorizada'],
        ['Aruak preso no campo depois do 3º mês', 'Regra de delegação; se não acontecer até o 6º mês, rever preço ou escopo'],
        ['Pedido de obra ou de fiscalização gratuita', 'Fora do escopo; sem venda de execução no piloto'],
        ['Cancelamento no 3º mês', 'ART anual já paga pesa ' + brl(ART2 / 3, True) + ' por mês atendido'],
    ], 'sm', widths=['40%', '60%'])
    ind = ind_table([
        ('Essencial, Aruak sozinho', ESS_AR, '0'), ('Essencial em supervisão', ESS_SUP, '0'), ('Essencial, Yan no campo', ESS_DEL, '0'),
        ('Completo, Aruak sozinho', COMP_AR, '0'), ('Completo em supervisão', COMP_SUP, '0'), ('Completo, Yan no campo', COMP_DEL, '0'),
        ('Implantação avulsa, com o Yan', IMPL_AV, '0'), ('Implantação avulsa, Aruak sozinho', IMPL_AV_SO, '0'),
    ])
    nota = (f'<p class="small">Essencial a R$ 1.600: depois de 8% e de {brl(ARTM, True)} de ART alocada, e remunerando 5 h do Aruak na meta, cabem {brl(ESS_448, True)} para todos os outros custos; com 6,25 h do Yan e uma ida, restam {brl(ESS_23, True)} para o administrativo. '
            f'Completo com o Aruak no campo: {brl(COMP_AR.ph, True)}/h; o preço para a meta seria {brl(COMP_AR.pmin, True)}. Implantação avulsa com ART individual de R$ 108,39; na assinatura, a ART anual cobre implantação e mensalidades.</p>')
    crit = table(['Por condomínio, depois de 90 dias', 'Decisão'], [
        ['A síndica usou o relatório para pelo menos 1 decisão, mensalidade em dia, Aruak até 5 h por mês na supervisão', '<b>Manter</b> e aplicar a regra de delegação'],
        ['Aruak ainda no campo no 6º mês', '<b>Ajustar:</b> Essencial com o Aruak sozinho precisa de ' + brl(ESS_AR.pmin, True) + '; rever preço no reajuste ou reduzir escopo'],
        ['A síndica não lê nem usa o relatório, 2 mensalidades atrasadas, ou pedidos recorrentes fora do escopo', '<b>Suspender</b> com aviso de 30 dias e entregar os registros'],
    ], 'sm', widths=['62%', '38%'])
    p2 = page('Frente 6 · ficha interna', 'Engenheiro do Condomínio · operação e dinheiro', 'Sequência, aceite, riscos, caixa, margem e regra de decisão.',
        '<h2>Sequência de execução</h2>' + seq + '<p><b>Aceite:</b> implantação aceita com o termo de recebimento do plano de 90 dias; mensal, com o relatório enviado até o 5º dia útil do mês seguinte e os alertas registrados; dia 90, com a ata curta da avaliação.</p>'
        '<div class="two"><div><h2>Riscos</h2>' + riscos + '</div><div><h2>Pagamento, aquisição e caixa</h2><p>Implantação 50% e 50%; mensalidade antecipada até o dia 10 ' + tag('P') + '; ART anual de ' + brl(ART2, True) + ' registrada depois da entrada. O contrato não fica negativo.</p>'
        '<p>Aquisição: indicação (Letícia), síndicos indicados por síndicos, Dossiê do Prédio gratuito e Scanner (código SÍNDICO). O tempo da vistoria gratuita reaproveitado entra uma única vez como aquisição.</p></div></div>'
        '<h2>Margem</h2>' + ind + nota + '<h2>Critério para manter, ajustar ou suspender</h2>' + crit)
    return p1 + p2

def plano90():
    imp = ol(['Semana 1: lista de documentos enviada à síndica; registro da ART; agenda das visitas.', 'Semana 2: levantamento complementar nas áreas comuns acessíveis; cadastro de sistemas e fornecedores.',
              'Semana 3: calendário de vencimentos com datas reais; plano anual de manutenção (ABNT NBR 5674).', 'Semana 4: prioridades e plano de 90 dias; reunião de entrega com a síndica.'])
    rows = [
        ['Dias 1 a 30', 'Completar a pasta: CERCON e projeto de incêndio, contratos de elevador, bombas e extintores, laudos, ARTs, notas de manutenção', 'Síndica, com a lista da Entre Colunas', 'Lista de recebidos e faltantes'],
        ['Dias 1 a 30', 'Elétrica depois da saída do gás: localizar projeto e ART do reforço. Sem documento, recomendar diagnóstico por profissional habilitado, com proposta específica', 'Entre Colunas recomenda; síndica decide', 'Item no relatório e na pauta'],
        ['Dias 1 a 30', 'CERCON: validade, classificação e situação da digitalização dos projetos exigida pelo CBMGO (NT 01/2025, prazo de 01/01/2027, conforme o dossiê ' + tag('R') + ')', 'Entre Colunas verifica; síndica providencia', 'Data no calendário'],
        ['Dias 31 a 60', 'Escolher as 3 prioridades com faixa de custo e quem aprova a despesa', 'Aruak e síndica', 'Prioridades assinadas'],
        ['Dias 31 a 60', 'Primeira demanda de cotação, por exemplo limpeza dos reservatórios com certificado ou laudo do SPDA, conforme o que estiver vencido', 'Entre Colunas cota; condomínio contrata', 'Comparativo com até 3 propostas'],
        ['Dias 31 a 60', 'Pauta técnica para a assembleia, se a despesa depender dela', 'Aruak e síndica', 'Pauta enviada'],
        ['Dias 61 a 90', 'Verificar o que foi encaminhado: extintores, iluminação de emergência, relatório anual do elevador', 'Yan na visita do mês', 'Checklist com fotos'],
        ['Dias 61 a 90', 'Inspeção predial (ABNT NBR 16747): recomendar data, sem obrigação municipal em Goiânia', 'Entre Colunas recomenda', 'Item no plano anual'],
        ['Dia 90', 'Reunião de avaliação: o que mudou, quais decisões foram tomadas, continuar, ajustar ou encerrar', 'Aruak e síndica', 'Ata curta'],
    ]
    t = table(['Quando', 'Ação', 'Quem faz', 'Evidência'], rows, 'sm', widths=['12%', '50%', '20%', '18%'])
    av = box('Na implantação avulsa', '<p>A síndica recebe o plano e executa com o condomínio. A Entre Colunas combina, na entrega, uma reunião de revisão no dia 90 (incluída) e oferece o Essencial a partir dali. Na assinatura, as ações da Entre Colunas acontecem dentro das visitas mensais.</p>')
    return page('Frente 6 · plano de 90 dias', 'Implantação e plano de 90 dias', 'Modelo preenchido com os temas do Dossiê do Trípoli ' + tag('S') + '. As datas e as prioridades reais saem dos documentos que a síndica apresentar.',
        '<h2>Implantação em 4 semanas</h2>' + imp + '<h2>Plano de 90 dias</h2>' + t + av)

def checklist():
    fixa = table(['', 'Parte fixa (toda visita, cerca de 1 h)', 'O que olhar', 'Registro'], [
        [SQ, 'Ocorrências', 'O que aconteceu desde a última visita, com zelador e síndica', 'Lista'],
        [SQ, 'Extintores', 'Lacre, manômetro, data da recarga, acesso livre, sinalização', 'Foto e data'],
        [SQ, 'Iluminação de emergência', 'Botão de teste; blocos apagados', 'Quantos falharam'],
        [SQ, 'Rotas de fuga', 'Escada e corredores livres; porta corta-fogo fechando sozinha', 'Foto se houver problema'],
        [SQ, 'Quadro geral, por fora', 'Sem abrir o painel: cheiro de queimado, ruído, tampa quente, identificação, relato de desarme', 'Ok ou alerta'],
        [SQ, 'Casa de bombas', 'Funcionamento e alternância, vazamento, ruído', 'Ok ou falha'],
        [SQ, 'Reservatórios', 'Nível, tampa, data da última limpeza, só com acesso seguro', 'Data'],
        [SQ, 'Elevador', 'Data da última visita da conservadora, chamados do mês, nivelamento', 'Data e chamados'],
        [SQ, 'Garagem e subsolo', 'Umidade, infiltração, fissura nova, ralos, armadura aparente', 'Foto comparativa'],
        [SQ, 'Hidrômetro', 'Leitura do mês; salto indica vazamento', 'Leitura'],
        [SQ, 'Portão, cerca e interfone', 'Funcionamento, sensor, sinalização', 'Ok ou falha'],
        [SQ, 'Documentos', 'O que vence nos próximos 60 dias', 'Alerta à síndica'],
    ], 'sm check', widths=['5%', '24%', '53%', '18%'])
    tema = table(['Mês', 'Tema do mês (cerca de 1 h)', 'Mês', 'Tema do mês'], [
        ['1', 'Elétrica documental: projeto, ART do reforço pós-gás, relatos', '7', 'Estrutura aparente na garagem e no térreo'],
        ['2', 'Cobertura e impermeabilização, onde o acesso for seguro', '8', 'Elevador documental e casa de máquinas'],
        ['3', 'SPDA visual e data do último laudo', '9', 'Pré-chuva: calhas, ralos, descidas'],
        ['4', 'Fachada e peitoris, do térreo e das janelas', '10', 'Lazer e acessibilidade'],
        ['5', 'Hidráulica: prumadas visíveis, registros, tetos', '11', 'Perímetro: cerca, câmeras, iluminação'],
        ['6', 'Incêndio: hidrantes, mangueiras, sinalização, CERCON', '12', 'Revisão anual e relatório para a assembleia'],
    ], 'sm', widths=['6%', '44%', '6%', '44%'])
    seg = box('Segurança e ocorrência crítica', '<p>Quem vai a campo não abre painel energizado nem atesta capacidade elétrica (NR-10). Cobertura com risco de queda acima de 2 m só com autorização, aptidão, capacitação (NR-35), análise de risco e meios de proteção; sem isso, registrar a limitação. Risco relevante na visita: aviso imediato à síndica, com horário, destinatário, orientação e encaminhamento registrados, consolidados no relatório. Na estação de chuva, infiltração entra na parte fixa.</p>', 'warn')
    return page('Frente 6 · checklist', 'Checklist da visita', 'Ronda visual das áreas comuns acessíveis: parte fixa em toda visita e um tema por mês em rodízio. Não sustenta conclusão sobre capacidade elétrica, elevador ou sistema de incêndio.',
        fixa + '<h2>Tema do mês</h2>' + tema + seg)

def relatorio_limites():
    rel = table(['Relatório mensal (2 páginas)', 'Exemplo de preenchimento, mês 1 ' + tag('S')], [
        ['1. Semáforo por sistema e o que mudou', 'Incêndio: <span class="pill p-t">amarelo</span> CERCON e projeto a confirmar · Elétrica: <span class="pill p-t">amarelo</span> ART do reforço não localizada · Elevador: <span class="pill p-v">verde</span> conservadora em dia; relatório anual a localizar · Reservatórios: <span class="pill p-t">amarelo</span> limpeza sem certificado · Cobertura: <span class="pill p-i">não vista</span> acesso sem proteção'],
        ['2. O que vence em 60 dias', 'Recarga dos extintores; limpeza dos reservatórios (datas a confirmar nos documentos)'],
        ['3. Três prioridades, com faixa de custo', 'Diagnóstico elétrico pós-gás · situação do CERCON e digitalização · limpeza dos reservatórios com certificado'],
        ['4. Cotações em andamento e quem decide', 'Limpeza dos reservatórios: 2 de 3 propostas recebidas; decide a síndica'],
        ['5. Resolvido e pendente', 'Resolvido: lista de documentos entregue. Pendente: pasta do elevador'],
        ['6. Limitações da visita', 'Cobertura não acessada por falta de proteção (NR-35); quadro geral avaliado só por fora'],
        ['7. Fotos e assinatura', 'Até 6 fotos; ' + RT],
    ], 'sm', widths=['30%', '70%'])
    lim = ul(['Visitas programadas: 1 no Essencial, 2 no Completo. Visita extra só com preço informado e autorizado antes.',
              'Ronda visual das áreas comuns acessíveis; sem abrir painel energizado; cobertura só com condições seguras.',
              'WhatsApp em horário comercial, resposta em 1 dia útil: até 4 consultas por mês no Essencial e 8 no Completo.',
              'Cotações: 1 demanda por mês no Essencial e 2 no Completo, até 3 propostas, comparativo com critério escrito. Fornecedor que não responde em 7 dias fica registrado.',
              'Assembleia: até 1 participação por semestre ' + tag('P') + '.',
              'Fora do escopo: execução, acompanhamento e fiscalização de obra; laudos com ART própria; análise de reformas das unidades (NBR 16280); emergência fora do horário comercial.'])
    dele = ol(['Atribuição do Yan registrada: formação, o que pode fazer em campo e o que fica com o Aruak. A ART e a assinatura continuam do Aruak.',
               'Horas reservadas na agenda do Yan: 6,25 h por mês no Essencial e 11 h no Completo, por condomínio.',
               'NR-35 válida para as visitas com cobertura; nunca abrir painel energizado (NR-10).',
               '<b>Duas entregas seguidas</b> supervisionadas, no prazo, dentro do escopo, sem omissão relevante e com revisão do Aruak dentro do tempo orçado.',
               'A síndica é avisada de quem vai a campo.',
               'Reversão: qualquer omissão crítica devolve a supervisão por mais duas entregas. O mês quatro, sozinho, não habilita ninguém.'])
    return page('Frente 6 · relatório e limites', 'Relatório mensal, limites e delegação ao Yan', 'O relatório cabe em duas páginas e termina sempre com o que cabe à síndica decidir.',
        rel + '<div class="two"><div><h2>Limites de atendimento</h2>' + lim + '</div><div><h2>Regra para delegar o campo ao Yan</h2>' + dele + '</div></div>')

def comparativo():
    def row(lab, e):
        return [lab, brl(e.receita), hh(e.h), brl(e.disp), brl(e.ph), brl(e.saldo)]
    rows = [row('Implantação avulsa, com o Yan', CMP['av_y']), row('Implantação avulsa, Aruak sozinho', CMP['av_s'])]
    for m in (3, 6, 12):
        rows.append(row(f'Implantação + Essencial, cancela no mês {m} · Yan assume no 4º mês', CMP[('ess_y', m)]))
    for m in (3, 6, 12):
        rows.append(row(f'Implantação + Essencial, cancela no mês {m} · Aruak sempre no campo', CMP[('ess_s', m)]))
    for m in (3, 6, 12):
        rows.append(row(f'Implantação + Completo, cancela no mês {m} · Yan assume no 4º mês', CMP[('comp_y', m)]))
    t = table(['Cenário', 'Receita total', 'Horas do Aruak', 'Disponível', 'Por hora do Aruak', 'Saldo parcial'], rows, 'sm num',
              widths=['44%', '11%', '11%', '11%', '12%', '11%'])
    # caixa da assinatura (Essencial, Yan)
    lanc = [('Mês 0 · assinatura', 1300.0, -ART2, 0.0, 0.0), ('Mês 1 · entrega do plano e 1ª mensalidade', 2900.0, 0.0, -(IMPL_CUSTO_Y + YAN_ESS*TEC + 3*ADM + IDA), -r2(1300*T)),
            ('Mês 2', 1600.0, 0.0, -(YAN_ESS*TEC + 3*ADM + IDA), -r2(2900*T)), ('Mês 3', 1600.0, 0.0, -(YAN_ESS*TEC + 3*ADM + IDA), -r2(1600*T))]
    acc = 0.0; cx = []
    for lab, rec, art, eq, tr in lanc:
        acc = r2(acc + rec + art + eq + tr); cx.append([lab, brl(rec), brl(art) if art else '—', brl(eq, True) if eq else '—', brl(tr, True) if tr else '—', brl(acc, True)])
    cxt = table(['Caixa da assinatura Essencial, com o Yan', 'Recebe', 'ART', 'Equipe e idas', 'Tributos', 'Acumulado'], cx, 'sm num', widths=['36%', '12%', '12%', '14%', '12%', '14%'])
    leit = box('Leitura', f'<p>Com o Aruak sempre no campo, a assinatura nunca chega a R$ 200 por hora dele ({brl(CMP[("ess_s", 12)].ph)}/h em 12 meses) e consome {hh(CMP[("ess_s", 12)].h)} da agenda. Com o Yan a partir do 4º mês, passa da meta já no 6º mês ({brl(CMP[("ess_y", 6)].ph)}/h) e usa {hh(CMP[("ess_y", 12)].h)} do Aruak em 12 meses. Cancelar no 3º mês não dá prejuízo, mas fica abaixo da meta, porque a ART anual e a supervisão pesam. A implantação avulsa com o Yan paga a meta ({brl(CMP["av_y"].ph)}/h) e é a porta mais segura quando a síndica ainda não tem decisões mensais.</p>')
    outras = ('<p class="small"><b>Recorrências relacionadas, fora das metas até 18/12:</b> Engenheiro da Empresa, R$ 3.000 por mês com 7 h do Aruak (' + brl(EMPRESA.ph) + '/h estimados), implantação cobrada à parte. '
              'Tip Toy, Engenheiro da Escola: R$ 1.800 por mês compensados na mensalidade do Theo; sem entrada de caixa e com cerca de ' + brl(TIPTOY_TRIB) + ' de tributo a 8%; contrato com sugestões já entregues ao Vicente. A próxima escola paga em dinheiro.</p>')
    return page('Frente 6 · comparação', 'Implantação avulsa ou assinatura', 'Comparação com cancelamento no 3º, 6º e 12º mês. Assinatura com ART anual de R$ 285,59 paga no início; implantação avulsa com ART de R$ 108,39.',
        t + leit + cxt + outras)

def build():
    return comercial() + ficha() + plano90() + checklist() + relatorio_limites() + comparativo()
