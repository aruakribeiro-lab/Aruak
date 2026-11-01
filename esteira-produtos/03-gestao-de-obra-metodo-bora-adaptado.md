# Produto · Gestão de Obra no modelo Bora na Obra, adaptado à Entre Colunas

Análise e modelagem · v2 (com módulos 7 e 8) · Entre Colunas · 01/11/2026 · documento interno
Fonte: material da Certificação Método BORA (CMB, fev/2022) no Drive do Aruak, cruzado com a esteira v4, o arquivo 01 (contexto real) e o arquivo 09 (decisões ativas).

---

## 0. O que foi lido e o que faltou

| Material | Situação |
|---|---|
| Apostila completa (versão comprimida, 647 páginas) | **Lida a parte de negócio e gestão:** módulos 0, 1, 2, 4, **7 (Metodologia de Execução BNO, completo)** e **8 (negócio, completo)**. Módulo 3 (projeto) passado por cima. **Módulos 5 e 6 não lidos em detalhe:** são técnicos (fundação, estrutura, instalações, acabamentos) e não mudam o modelo de negócio; ficam como referência para os checklists de fiscalização |
| Modelos do módulo 7 | Lidos: relatório financeiro mensal (com a tabela real de taxas), controle de medição, relatório semanal, checklist de fiscalização, checklist da obra memorável, arquivos do Sistema Gestão BNO (RDO, recibo, proposta) |
| Contratos | Lidos: execução de obra, acompanhamento de obra, consultoria. Não lidos: projeto de arquitetura, prestação de serviço, termo de recebimento |
| Padrões (Asana) | Lidos: reforma de apartamento (obra), EVF/OE. Pós-obra veio vazio |
| Proposta de EVF (apresentação) e checklists de proposta, levantamento e obra memorável | Lidos |
| Planilhas grandes (MODELO_EVF, orçamento executivo, cronograma) | Não abertas nesta rodada; ficam para quando modelarmos o EVF |
| Pasta de marketing (.rar) e pastas de lives (Domus, Lote ao Lucro, Maratona financiamento) | Não lidas (.rar não abre pelo Drive; as lives ficam para a frente de obra com financiamento) |
| Pastas "Livros" e "Reflexão Aruak" | Pessoais, fora do tema; não usadas |
| Pasta de contexto (arquivos 00 a 09) | Lidos o 01 e o 09 |

---

## 1. Como o Bora na Obra trabalha (o método em uma página)

### A esteira deles
Cliente entra por um produto menor e sobe: **projeto → EVF → orçamento executivo → gestão da obra**. "Vários clientes chegaram querendo só a obra. Vendemos o projeto, depois o EVF, depois o orçamento executivo e por fim a gestão." Produtos de presença no canteiro: **visita avulsa ou pacote**, **acompanhamento** (visitas, sem RT) e **gestão/execução** (com RT).

### A obra é administrada, não empreitada
- **Tudo é comprado e contratado em nome do cliente.** A construtora não compra material nem paga mão de obra com o dinheiro dela.
- Para cada compra ou contratação, a equipe apresenta **pelo menos 2 orçamentos numa Ordem de Compra (OC)** e **o cliente escolhe e autoriza**.
- Compras urgentes: **cartão pré-pago do cliente, teto de R$ 500**, sem autorização prévia.
- Pagamentos de mão de obra por **medição semanal**: a equipe mede o que foi executado e informa ao cliente quanto pagar a quem.

### Como eles cobram (o centro do modelo)
1. **Custo mensal fixo, pago antecipado** no início de cada mês. Cobre a **equipe dimensionada** para a obra (arquiteto ou engenheiro + estagiário, visitas diárias de até 2 h), uniforme, impressão, RT e brinde. **O primeiro mês antecipado paga o planejamento**: "você recebe para depois começar a planejar". No exemplo real: R$ 4.310 por mês numa obra de 4 meses.
2. **Taxa variável por etapa sobre cada compra e contratação**, cobrada **integralmente no mês em que a OC é aprovada**, mesmo que o cliente parcele com o fornecedor. É aqui que está o lucro: "você está vendendo gestão da obra, que vai sair entre 12% e 15% de lucro. Essa informação só é importante para você."
3. **O valor da gestão entra dentro do custo da obra**, nunca apresentado separado ("quando mostrávamos separado, o cliente dizia que não precisava da gestão").

**Tabela de taxas que eles usam (relatório financeiro real):**

| Etapa | Taxa | Lógica |
|---|---|---|
| Demolições e retiradas; alvenarias e vedações | 25% | Etapa barata e trabalhosa |
| Mobilização; locação de equipamentos; estrutura; forro de gesso | 20% | |
| Instalações | 25% na apostila (20% no relatório real) | Etapa de risco e retrabalho |
| Forros especiais; pinturas | 15% | |
| Pisos e revestimentos; serviços não listados | 10% | |
| Louças e metais | 7% | |
| Iluminação; marcenaria; marmoraria | 5% | Itens caros, pouco esforço de gestão |
| Equipamentos e maquinários | 3% | |

Argumento de venda: "a taxa diminui conforme o item fica mais caro e exige menos de nós; em determinado momento da obra a gente se paga" (a pesquisa de preço em marcenaria ou marmoraria economiza mais que a taxa).

**Resultado no exemplo deles:** custo direto R$ 395 mil, taxas R$ 38,8 mil (**9,8%**), fixo R$ 17,2 mil (4 meses). **Total da gestão: R$ 56 mil, ou 14,2% sobre o custo.**

### O que o módulo 7 acrescenta (Metodologia de Execução BNO)

**Modalidades de obra e quando usar cada uma**
- **Empreita (preço fechado):** "se você quiser se posicionar como maestro, não faça obra por empreita". O preço vem de suposição, e o construtor vive no modo "estou rico, estou pobre". **Regra deles:** empreita só se a obra durar **menos de uma semana** e tiver **até 3 itens controláveis**. **Nunca com demolição**, porque a surpresa vira aditivo ou prejuízo.
- **Administração convencional (15% a 20% fixo sobre tudo):** é flexível, mas tem um risco: no acabamento, que é a etapa mais cara, o cliente já conhece o mestre e **dispensa o administrador para não pagar a porcentagem**. A tabela decrescente do Bora existe para tirar esse incentivo.
- **Parâmetros de mercado segundo eles:** administração convencional 15%; empreita com BDI de 25% a 35%; no método deles, "é justo ganhar entre **10% e 15% do valor total da obra**". Obra pequena e barata precisa de percentual maior.

**Como montam o fixo mensal**
- Somam as horas de **deslocamento, fiscalização, telefonemas de cotação, documentos do administrativo e conversa com o operacional**, por dia, semana e mês, e multiplicam pela hora (sem lucro).
- Acrescentam custos indiretos (uniforme, placas, RT, brinde) **rateados pelo prazo do cronograma**.
- **O fixo vale só para os meses do cronograma.** Se a obra passar do prazo, não cobram mais meses. Se o cliente acrescenta escopo, apresentam um novo cronograma.
- **O lucro e o risco ficam na taxa variável.** O reembolso também paga taxa.

**Controle pelo pagamento**
- "Só o que está realizado está pago. Não existe pagamento adiantado." O empreiteiro que fez 30% da parede recebe 30%; se fez mal, não recebe. **Quem libera o pagamento é o gestor**, depois da medição e do checklist de aceite.
- Contratam **pequenos empreiteiros que lideram a própria equipe** (núcleos). O gestor fala com o líder de cada frente e **não ocupa o lugar do mestre**: "se o gestor se ocupa da posição do mestre, deixa de fazer o administrativo e o estratégico".
- Fornecedor responde pelo que forneceu; a documentação mostra quem acionar no pós-obra.

**A obra que vende a próxima**
- Limpeza diária, armário para mochilas, placas (vizinhos, EPI, horários, "marque a gente nos stories"), presente e carta para cada vizinho, capacete com o nome do cliente, **quadro de gestão à vista** (Kanban por cores de equipe) e cronograma na parede, projeto atualizado na parede, mapa de fotos com os mesmos ângulos do projeto para o antes e depois.
- **Combinam o depoimento no início:** "meu objetivo é chegar no final e ter um depoimento seu dizendo que valeu a pena".

**A entrega**
- **Manual do proprietário (NBR 14037)** montado durante a obra: cada item instalado já entra no manual com fornecedor e manutenção.
- Vistoria com o cliente e **Termo de Recebimento com ressalvas**, que viram a lista do pós-obra.
- **Caixa reservado para o pós-obra** e presente (overdelivery) já incluído no preço.

**Módulo 8 (negócio)**
Planejamento por **OKR anual dividido em trimestres**; "a família é um prato de cristal"; "contrate porque cresceu, não para crescer"; sair da esfera do técnico para a do dono.

### As três esferas da gestão (é assim que vendem e entregam)
- **Planejamento (estratégico):** estudo e compatibilização dos projetos, visita técnica, análise crítica (prazos longos de marcenaria, vidro e marmoraria; regras do condomínio; mão de obra disponível), orçamento executivo, cronograma real e cronograma do cliente, logística do canteiro. Reforma: 7 a 15 dias; casa do zero: 30 a 45 dias. Fecha com **reunião de apresentação do planejamento e Termo de Recebimento do Planejamento** (vídeo Loom antes).
- **Gerenciamento (administrativo):** OCs com comparativos, contratos com prestadores, relatório semanal (medição + fotos + contas pagas), **relatório financeiro mensal** (fixo + taxas), **previsto (EVF) × realizado**, aditivos numerados.
- **Fiscalização (operacional):** visitas diárias de até 2 h, diário de obra (RDO), recebimento e conferência de material, medição para liberar pagamento, checklist por etapa.

### O que eles garantem (quebra de objeção)
- **Se o prazo estourar por culpa da gestão, o fixo mensal não é cobrado** no período excedente. "Fica claro que você não vai enrolar a obra para ganhar mais."
- Garantia de 5 anos da execução.
- **Sem reserva técnica** (#borasemrt): bonificação de fornecedor é repassada ao cliente.

### Venda
- Primeira reunião presencial, nunca proposta por WhatsApp; perguntas de rapport; **"qual a sua experiência com obras?"** como pergunta estratégica.
- Proposta em apresentação: capa personalizada, como é hoje, problemas comuns em obra, portfólio, depoimentos, serviços, as três esferas, sistema, **pacotes** (Acompanhamento, Planejamento, Gestão completa), taxa variável, garantia, CTA.
- Preço: do maior para o menor; mostrar parcelas. Sair da reunião com **data de retorno** (5 a 7 dias).
- "Desconto é o preço que você paga por não saber vender o seu valor." Desconto só com contrapartida (à vista).

### Gestão da empresa
Preço pela hora (custos fixos + variáveis + investimentos ÷ horas produtivas; lucro 20% a 25% em serviço; mais em consultoria e laudo). Processos como checklist ("fazendo pela última vez", gravado em vídeo). Gestão à vista. Reuniões semanais curtas e trimestrais de planejamento. Caixa de 3 a 6 meses. Salários até 25% do faturamento.

---

## 2. O que encaixa na Entre Colunas (e por quê)

| Dor real da Entre Colunas (arquivos 01 e 09) | O que o método Bora resolve |
|---|---|
| "Recebeu ~90% do faturamento tendo executado ~70% das obras. Adiantamento não é lucro, é dívida em forma de obra." | **O cliente paga fornecedores e mão de obra direto.** A Entre Colunas só recebe o fixo antecipado e as taxas. Não existe mais dinheiro do cliente no caixa da empresa para ser usado em outra obra (regra 5) |
| Margem real de 8% a 15% contra meta de 30% | O lucro não depende de acertar o orçamento de empreitada: a taxa incide sobre o que é comprado. Estouro de material deixa de ser prejuízo da empresa |
| Conversão de proposta abaixo de 10% e orçamentos grandes parados | Esteira com porta paga (EVF/orçamento executivo) e pacotes; o cliente compra o planejamento antes de decidir a obra inteira |
| "Obra vendida do zero perde dinheiro pela venda" (esteira v4) | O orçamento executivo deixa de ser feito de graça: vira produto (Bora: R$ 3.400 a R$ 5.300 em 2022) |
| Gestão e administração de obra marcada como "motor de lucro; testar numa obra real" (esteira v4) | É exatamente este produto. O método dá o processo, os documentos e a forma de cobrar |
| Canal de arquitetos com "sem RT escondida" (Código de Ética do CAU) | É a bandeira deles (#borasemrt) e o modelo de proposta com o logo do escritório parceiro |
| Modelo de empreitada parcial já em uso (15% na assinatura, 80% direto a fornecedores, 5% na entrega) | A Entre Colunas já está a meio caminho; falta formalizar OC, taxa por etapa e relatório financeiro |

---

## 3. O produto adaptado: Gestão de Obra Entre Colunas

### Pacotes (mesma lógica do Bora)

| Pacote | O que é | Como cobra | RT |
|---|---|---|---|
| **Acompanhamento** | Visitas técnicas programadas (até 2 h), relatório com fotos, orientação aos prestadores | Por pacote de visitas por mês | Não |
| **Planejamento** | Estudo de projetos, orçamento executivo, cronograma, OCs dos itens críticos; o cliente executa com quem quiser | Valor fechado (produto de porta, como o EVF) | Não |
| **Gestão completa** (recomendado) | Planejamento + gerenciamento + fiscalização, com RT e ART de execução | **Fixo mensal antecipado + taxa por etapa** | Sim |

### Como calcular o fixo mensal (com os parâmetros da nossa calculadora)
Fixo = (horas da equipe no mês × R$ 80 + custos externos do mês) ÷ (1 − 13%)

Exemplo: obra de **R$ 300 mil de custo, 4 meses** (a mesma linha da planilha de horas: 38 h da empresa e R$ 800 de externos por mês):
- (38 h × R$ 80 + R$ 800) ÷ 0,87 = **R$ 4.414 por mês** (o Bora cobrava R$ 4.310 no exemplo deles)
- 4 meses = R$ 17.655

### Taxa por etapa (lucro e hora do Aruak)
Aplicando a tabela do Bora a uma obra com o mesmo perfil do exemplo deles, a taxa média fica perto de **9,8% do custo**:
- 9,8% × R$ 300 mil = **R$ 29.400**, que depois de 13% de imposto vira R$ 25.578
- Horas do Aruak: 20 h/mês × 4 = 80 h, mais a venda (8 h ÷ 30% de conversão ≈ 27 h) = 107 h
- **R$ 25.578 ÷ 107 h ≈ R$ 239 por hora do Aruak**, já com a equipe paga pelo fixo

**Total pago pelo cliente pela gestão: R$ 47 mil, ou 15,7% do custo.** É praticamente o catálogo atual (15%), mas com três diferenças: o fixo antecipado paga a equipe antes do trabalho, a taxa é cobrada no mês da compra e o dinheiro da obra nunca passa pelo caixa da empresa.

> Estimativa a validar: a taxa média de 9,8% depende do perfil da obra. Uma reforma com muita demolição e alvenaria puxa a média para cima; uma com muita marcenaria e marmoraria, para baixo. A planilha da primeira obra vai mostrar a taxa real.

### Comparação com o que existe hoje
| Modelo | Quanto a Entre Colunas recebe numa obra de R$ 300 mil de custo | Quem carrega o risco de material e prazo |
|---|---|---|
| Empreitada (custo × 1,43) | R$ 129 mil de margem bruta no papel, mas margem real histórica de 8% a 15% | **A Entre Colunas** |
| Administração 15% (catálogo) | R$ 45 mil | Dividido; hoje sem regra escrita |
| **Gestão modelo Bora** | R$ 47 mil (R$ 17,7 mil fixo + R$ 29,4 mil taxas) | **O cliente paga direto; a empresa responde pela gestão** |

---

## 4. Ajustes obrigatórios para a nossa realidade

0. **Choque com a frente atual de reformas com preço fechado.** A regra do Bora (empreita só abaixo de uma semana, até 3 itens e sem demolição) bate com a nossa frente de "reformas com preço e data fechados" até 18/12. **Recomendação:** manter preço fechado (× 1,43) só para serviços pequenos e empacotados, como o banheiro sem quebrar (3 a 4 dias) e a pintura; **reforma com demolição ou com mais de uma semana passa para Gestão de Obra**. A decisão é sua, porque mexe na frente atual.
0. **O Aruak fora do papel de mestre.** Hoje 60% das horas do Aruak são de canteiro (arquivo 01). No modelo do Bora, quem faz a presença diária é o gestor de campo (o Yan ou um estagiário treinado), com empreiteiros-núcleo, e o Aruak fica no estratégico. Isso é o que permite chegar à meta de 6 h por semana no canteiro.
1. **Conselho e lei:** os modelos são de arquiteto (CAU, RRT, Lei 12.378). Trocar por **CREA-GO, ART e Lei 5.194/66**.
2. **Uso de imagem:** o contrato do Bora dá à empresa o direito de usar imagens "sem aprovação do contratante". Isso contraria o que já decidimos (autorização específica e separada) e a LGPD. **Retirar.**
3. **Cláusula que tira a contratada de qualquer processo** (11.9 do contrato de execução): juridicamente frágil. **Vicente revisa.**
4. **Multa de 10% na rescisão** (contrato de execução): para obra pode ficar, mas sem conflitar com a regra de "sem fidelidade" que vale para os mensais (condomínio e escola).
5. **Alçadas:** o Bora usa teto de R$ 500 no cartão do cliente. A Entre Colunas já tem Korran (compra até R$ 1.000) e Yan (mão de obra até R$ 2.000 com dois referenciais). **Escrever no contrato qual alçada vale na obra do cliente.**
6. **Prazo e garantia:** a regra do módulo 7 é mais forte que a do contrato: o fixo vale só para os meses do cronograma, seja qual for a causa do atraso (salvo escopo novo com cronograma novo). Adotar só depois de a primeira obra mostrar que o planejamento é cumprido. Antes disso é promessa sem medida (regra 6).
7. **Tip Toy:** as condições combinadas (até R$ 100 mil sem taxa; R$ 101 a 250 mil 10%; acima de R$ 251 mil 8%) são um caso especial. Não usar como tabela geral.
8. **Ferramenta:** o Bora vende o Sistema Gestão BNO. **Nenhum software pago antes de janeiro/2027**: usar o Painel de Obras, o Mais Controle e planilhas.
9. **Preços de 2022:** EVF e orçamento executivo a R$ 3 mil a R$ 5 mil eram valores de 2022 em Brasília. Recalcular pela nossa hora.

---

## 5. Kit de documentos a adaptar (já existem nos modelos do Bora)

| Documento | Quando | Modelo de origem |
|---|---|---|
| Contrato de Gestão de Obra (fixo + taxas) | Fechamento | Contrato de execução de obra |
| Contrato de Acompanhamento | Fechamento | Contrato de acompanhamento |
| Ficha de cadastro do cliente nas lojas | Planejamento | Anexo do contrato |
| Termo de Recebimento do Planejamento | Fim do planejamento | Checklist de fiscalização |
| Ordem de Compra (2 a 3 propostas, cliente autoriza) | Toda compra e contratação | Anexo do contrato + OC |
| DS (Diagnóstico e Soluções) para o arquiteto | Quando o projeto tem falha | Anexo do contrato |
| Diário de obra (RDO) | Toda visita | Arquivos Gestão BNO |
| Relatório semanal (medição + fotos + contas a pagar) | Toda semana | Relatório semanal |
| Controle de medição por contrato | Toda semana | Controle de medição |
| Relatório financeiro mensal (fixo + taxas + previsto × realizado) | Todo mês, pago até o 5º dia útil | Relatório financeiro |
| Checklist de canteiro e de fiscalização por etapa | Planejamento e execução | Checklists |
| Termo de Conclusão de Obra e lista de pendências do pós-obra | Entrega | Checklist de fiscalização |

---

## 6. Como testar (respeitando a regra até 18/12)

A esteira v4 já diz: gestão de obra é o motor de lucro e precisa de **uma obra real com papéis e horas medidos**. Isso cabe na frente "obras com margem".

1. Escolher **a próxima obra fechada** (ou uma reforma do canal de arquitetos) e oferecer o pacote Gestão completa.
2. Usar só 5 documentos no primeiro teste: contrato, OC, relatório semanal, relatório financeiro mensal e termo de recebimento do planejamento.
3. Medir: horas do Aruak, do Yan e do administrativo por semana; taxa média real; dias entre a OC e o pagamento da taxa; atraso em relação ao cronograma.
4. **Decisão no fim da obra:** se a hora do Aruak ficar acima de R$ 200 e o caixa não tiver adiantado nada, o modelo vira padrão da Entre Colunas para obra nova.

---

## 7. Pendências e próximos materiais

| O que preciso | Para quê |
|---|---|
| Decisão do Aruak: reforma com demolição ou com mais de uma semana sai do preço fechado e passa para Gestão de Obra? | Define a regra comercial a partir de agora |
| Horas reais do Yan por semana numa obra (deslocamento, fiscalização, cotações, documentos) | Fechar a fórmula do fixo com o método do módulo 7 |
| Planilha MODELO_EVF (já está no Drive) | Modelar o EVF/orçamento executivo como produto de entrada |
| Confirmar com o Ivan: imposto real e se 13% vale para a taxa de administração | Muda a conta da seção 3 |
| Vicente: revisar o contrato de gestão adaptado (seção 4) | Antes da primeira proposta |
