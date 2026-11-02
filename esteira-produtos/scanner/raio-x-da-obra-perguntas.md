# Scanner da Obra · perguntas, contas e regras (v3)

v3 · 02/11/2026 · documento interno · página publicada: https://claude.ai/artifact/1h5ZWoMDvYETjoDnwatA4h (modo de teste: final `#teste`)

A v3 incorpora a análise do ChatGPT sobre o “Raio-X da Obra em Andamento” e mantém o que só funciona numa página sem servidor: o resultado sai na hora, na tela, e o lead chega pelo WhatsApp com o resumo pronto.

## A primeira tela

“O que você quer entender sobre o seu imóvel hoje?”, com o aviso de perigo (193) antes de qualquer pergunta e duas portas principais:
- **Apareceu um problema no meu imóvel** (cerca de 3 minutos): cliente da Visita Diagnóstica, do laudo ou do reparo.
- **Estou construindo ou reformando** (Raio-X da Obra em Andamento, de 10 a 15 minutos): cliente da retomada, do plano para terminar e da gestão.

Atalhos mantidos: vou começar uma obra (Pré-obra), vou receber ou comprar um imóvel (Vistoria), cuido de um prédio (Engenheiro do Condomínio).

## Porta 1 · Apareceu um problema (8 telas, uma pergunta por vez)

| Tela | Pergunta | Opções |
|---|---|---|
| 1 | Há alguma situação oferecendo perigo às pessoas agora? | Fumaça, faíscas ou cheiro de queimado · algo caindo · teto, laje, parede ou piso cedendo · outro perigo → **SCN-VERMELHO**. “Nenhum sinal” segue. “Não sei avaliar” segue, e o resultado traz um aviso de segurança. |
| 2 | Que problema apareceu? | Infiltração, mancha ou umidade · fissura ou trinca · piso ou revestimento soltando · elétrico · hidráulico · banheiro ou cozinha para renovar, sem vazamento · outro |
| 3 | Onde ele aparece e quem mais foi afetado? | Um ambiente · vários ambientes · também no vizinho · área comum do prédio · tipo de imóvel |
| 4 | Quando percebeu e o que mudou? | Há quanto tempo · está igual, aumentou, aparece e some, voltou depois de um reparo · detalhe opcional |
| 5 | O que acontece antes de aparecer ou piorar? | Chuva · uso do chuveiro, da pia ou de equipamento · obra no vizinho · nenhuma relação · não sei |
| 6 | Alguém já tentou descobrir a causa ou consertar? | Ninguém · sim, resolveu por um tempo · sim, não resolveu · quem foi (opcional) |
| 7 | Que decisão você precisa tomar? | Entender a providência · contratar um reparo definido · documentar para construtora, condomínio ou seguradora · tratar uma disputa · outra |
| 8 | Tem fotos? | Orientação para mandar pelo WhatsApp (de longe, de perto, ao lado), sem se aproximar do problema |

**Para onde cada caso vai:**
- Documentar ou disputa → **SCN-LAUDO** (o texto avisa que, com perito já nomeado, o serviço é assistência técnica).
- Reparo definido em banheiro ou cozinha → **SCN-REPARO**.
- Reparo definido, mas com trinca, problema que aumentou, voltou depois de um reparo, ou infiltração ou vazamento que não se resolveu → **SCN-DIAGNOSTICO**, com a explicação “por que não o reparo direto”.
- Outro reparo definido → **SCN-REPARO** (visita de medição sem custo, até 1 hora).
- Banheiro ou cozinha para renovar, querendo entender a providência → **SCN-REPARO**.
- Todo o resto → **SCN-DIAGNOSTICO**.

## Porta 2 · Raio-X da Obra em Andamento (introdução e 5 telas)

**Promessa:** “Antes do próximo pagamento, entenda o que já foi entregue, o que está travando a sua obra e se o dinheiro cobre o que falta até a mudança.” A pessoa pode marcar “não sei”; o resultado mostra qual informação pedir à equipe. As respostas ficam só no aparelho e o rascunho permite continuar de onde parou.

| Tela | O que pergunta |
|---|---|
| 1 · Em que ponto a obra está | Tipo de obra (casa nova, reforma de casa, reforma de apartamento, ampliação, conclusão de obra recebida já iniciada) · como está hoje (normal, equipe reduzida, andando e parando, parada, em troca de prestadores) · última etapa concluída e etapa em execução (a lista muda com o tipo) · início, entrega combinada e entrega que a equipe informa hoje · motivo da mudança de data · como contratou · quem compra o material · quem coordena · quem confere antes de pagar · por que procurou agora |
| 2 · O que a equipe combinou e o que aconteceu | As três últimas entregas prometidas (serviço, data, situação) · o que impediu quando atrasou · retrabalho nos últimos 30 dias · equipe parada por frente não pronta · quem decide e até quando · próxima entrega importante e o que já está garantido · sinais na obra (trinca aumentando abre o aviso 193) |
| 3 · Quanto foi pago e quanto foi entregue | O que conferir (obra inteira, empreitada principal ou um prestador) · data de referência · valor combinado e de onde vem · acréscimos e retiradas aprovados · pedidos em discussão · total pago · executado e aceito (medição em reais, marcação das etapas ou só uma impressão) · pago com destino identificado e se já entrou na medição · executado e ainda não pago · próximo pagamento (valor, data e o que dá direito a ele) · quem conferiu a medição e que registro existe |
| 4 · O dinheiro chega até a mudança | O que precisa estar pronto para considerar entregue · o que ficou para depois · o que ainda falta (lista por tipo) · **a pergunta-chave** · custo para terminar (mínimo e máximo) e de onde vem · quanto a obra já deve · dinheiro disponível (ou “prefiro não informar”) · recursos próprios e financiamento com data, e se a liberação depende de etapa · os três maiores pagamentos dos próximos 30 dias · a última surpresa de custo |
| 5 · Quem governa a próxima decisão | Documentos que conseguiria entregar a outra pessoa · quem aprova gasto extra e como registra · decisão dos próximos sete dias e o valor · que ajuda faria mais diferença |

**A pergunta-chave:** “Se amanhã outra equipe pegasse a sua obra exatamente como está, quanto ainda seria preciso gastar para chegar à entrega que você escolheu?”

O Scanner não pede CPF, extrato nem dados bancários.

## Os quatro indicadores

**1 · Pagamento e entrega** (no conjunto escolhido na tela 3)
- Combinado atualizado (B′) = combinado + acréscimos − retiradas.
- A conciliar (C) = pago − executado e aceito − pago com destino identificado que ainda não entrou na medição.
- O executado vem da medição em reais (“com base em documento” quando há planilha, quantidades ou aceite assinado) ou da marcação das etapas (B′ × percentual pelas etapas, “estimado”). A impressão geral fica registrada e **não vira reais**.
- Limite de tolerância: o maior entre R$ 3.000 e 3% de B′. Dentro dele: “Confere”. Acima: “Conciliar”. Abaixo de −limite: executado além do pago, conferir o que é devido.

**2 · Fôlego para terminar** (obra inteira)
- Recursos = disponível + recursos próprios programados + financiamento aprovado. Venda esperada e crédito em negociação ficam de fora.
- Compromissos = dívidas já existentes + custo para terminar (mínimo e máximo). Dívida não informada entra como zero, com aviso.
- Sobra ou falta = recursos − compromissos, nos dois extremos. Falta mesmo no mínimo: “Falta”. Falta só no máximo: “Conferir”. Sobra nos dois: “Fecha”.
- Sem o custo para terminar, o Scanner mostra uma **referência** (pago × B′ ÷ executado − pago), só para a obra inteira com mais de 10% executado, e avisa que não substitui o orçamento.

**3 · Fôlego nos próximos 30 dias**
- Saldo de hoje, entradas com data dentro de 30 dias e os três maiores pagamentos, em ordem de data (no mesmo dia, a saída vem antes da entrada). Pagamento sem data entra como hoje, com aviso de projeção parcial.
- Se o saldo fica negativo, mostra a data e quanto falta: uma obra pode ter dinheiro no total e parar antes da próxima entrada.

**4 · Confiabilidade das entregas**
- Das três últimas entregas: aceitas, com pendência ou parciais, não iniciadas, não conferidas; quantas passaram da data sem aceite.
- As causas são separadas com justiça: dependem do proprietário (decisão, pagamento, projeto, material quando ele compra), da equipe (falta de equipe, serviço anterior, material quando a equipe compra) ou de fora (chuva, acesso).
- “Conferir” quando há entrega vencida sem aceite, causa não esclarecida, retrabalho sem responsável ou problema sem quem decide.

## Classificação

| Nível | Quando |
|---|---|
| **Replanejamento prioritário** | Falta dinheiro mesmo no custo mínimo, ou o caixa fica negativo nos 30 dias, ou a obra está parada ou em troca de prestadores |
| **Dados insuficientes** | Não dá para calcular nem o indicador 1 nem o 2. O resultado diz qual informação falta |
| **Conferir antes da próxima decisão** | Valor a conciliar acima do limite · falta só no custo máximo · entregas a conferir · medição sem registro conferível ou conferida por quem recebe · próximo pagamento por adiantamento ou com motivo pouco claro · custo máximo acima de 1,3 vez o mínimo · trinca aumentando |
| **Acompanhamento regular** | Nenhum dos casos acima |

Cada número leva a origem: **com base em documento**, **estimado pelo proprietário** ou **a levantar**. O resultado diz que nada foi conferido pela Entre Colunas.

## Próxima ação e convites

**Sua próxima ação:** até quatro itens, por prioridade: reorganizar o caixa antes da data negativa; decidir o que fica para depois; pedir a composição do próximo pagamento; reunir medição, materiais pagos e orçamento do que falta; pedir a folha de três colunas (serviço que falta, valor que ainda será pago, data prevista, começando pelos cinco itens mais caros); resolver o que depende do proprietário; combinar datas e responsáveis por escrito; organizar a pasta de documentos. O valor a conciliar e o que falta para terminar nunca são somados.

**Onde a Entre Colunas entra** (a ordem segue a situação; a ajuda escolhida na tela 5 vem primeiro):
1. Conferir uma medição antes da próxima parcela: avaliação técnica delimitada, com escopo e honorários antes da visita.
2. Um plano para terminar com a equipe que já está aqui: levantamento do saldo de serviços, orçamento para terminar e sequência das etapas (Pré-obra aplicada à retomada).
3. Avaliar a Entre Colunas para assumir a gestão da conclusão: depois de vistoria de entrada, registro da situação recebida e conferência financeira.
4. Um engenheiro avaliar um problema técnico na obra: aparece quando há sinal técnico marcado.

**Mensagem do WhatsApp** (cerca de 1.500 caracteres): classificação, obra, contratação, quem coordena e quem confere, datas, pagamentos, situação até a entrega, caixa de 30 dias, entregas e atrasos, próximo pagamento, decisão dos próximos sete dias, por que procurou agora, convite escolhido, nome, bairro e origem.

## Casos de teste (abrir com `#teste`)

| Caso | Dados principais | Resultado esperado |
|---|---|---|
| Obra equilibrada com materiais antecipados | Combinado R$ 600 mil · pago R$ 300 mil · medição R$ 250 mil em planilha · R$ 50 mil em material fora da medição · custo para terminar R$ 280 a 300 mil cotado · disponível R$ 180 mil + R$ 60 mil próprios + R$ 100 mil de financiamento · deve R$ 10 mil | Acompanhamento regular · diferença R$ 0 · sobra de R$ 30 a 50 mil |
| Obra com falta de caixa | Combinado R$ 520 mil · pago R$ 300 mil · medição R$ 250 mil · R$ 30 mil em material · custo para terminar R$ 230 mil estimado · disponível R$ 120 mil + R$ 100 mil de entradas · deve R$ 15 mil · 1 de 3 entregas aceita | Replanejamento prioritário · faltam R$ 25 mil · R$ 20 mil a conciliar |
| Obra sem medição confiável | Pago R$ 180 mil · só impressão de 70% · sem custo para terminar · medição verbal conferida pelo empreiteiro · próximo pagamento com motivo pouco claro | Dados insuficientes · pedir a folha de três colunas |
| Porta 1 | Perigo · infiltração para entender · trinca para documentar · banheiro com reparo definido · reparo definido que voltou | SCN-VERMELHO · SCN-DIAGNOSTICO · SCN-LAUDO · SCN-REPARO · SCN-DIAGNOSTICO |

## O que veio do ChatGPT e o que foi adaptado

**Incorporado:** a promessa e a primeira tela; as perguntas da porta do problema; as cinco telas do Raio-X; os quatro indicadores; a classificação em quatro níveis; os rótulos de origem dos números; a pergunta-chave; não dizer que a Entre Colunas conferiu documentos; não transformar impressão em reais; não pedir CPF nem extrato; os três convites; os três casos de teste; a folha de três colunas como próxima ação.

**Adaptado:**
- Fotos vão pelo WhatsApp, porque a página não recebe arquivos.
- Resultado na hora, na própria página, em vez de Google Forms com planilha preenchida à mão. O lead chega pelo WhatsApp com o resumo.
- O índice de 0 a 100 da v2 saiu: a classificação em quatro níveis explica melhor e não passa uma precisão que os dados não têm.
- O “pago a mais” da v2 (percentual da obra × orçamento) virou “a conciliar”, que desconta material e adiantamento com destino identificado.
- A projeção de prazo da v2 deu lugar às entregas prometidas, com as causas separadas entre proprietário, equipe e fatores externos.

## Pendente de decisão do Aruak

- Preço e formato dos três convites, principalmente o “plano para terminar com a equipe atual” (Pré-obra aplicada à retomada).
- Os pesos das etapas (usados só quando o cliente marca as etapas): conferir com as obras da Entre Colunas.
- O limite de conciliação (R$ 3.000 ou 3%) e a faixa larga de custo (30%).
- Se quer de volta o custo mensal do atraso (aluguel enquanto não muda), que estava na v2.
- O link do assistente (variável `ASSISTENTE_URL`) e o compartilhamento público da página.
