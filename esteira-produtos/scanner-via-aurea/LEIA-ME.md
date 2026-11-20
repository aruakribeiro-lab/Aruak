# Scanner da Obra · Via Áurea, com planilha de contatos

Esta pasta tem o Scanner pronto para ficar num link próprio e gravar numa planilha Google todo mundo que começa, mesmo quem não termina.

- `index.html`: o Scanner completo, em um arquivo só.
- `apps-script.gs`: o código que recebe os dados na planilha.

São três passos, uma vez só. Leva uns 15 minutos.

## 1. Criar a planilha e o receptor (Google)

1. Entre em sheets.google.com com a conta da empresa e crie uma planilha em branco chamada **Scanner da Obra · Contatos**.
2. No menu da planilha: **Extensões > Apps Script**.
3. Apague o que estiver escrito, cole todo o conteúdo do arquivo `apps-script.gs` e clique em **Salvar**.
4. Clique em **Implantar > Nova implantação**. Em "Tipo", escolha **App da Web**.
   - Executar como: **Eu**.
   - Quem pode acessar: **Qualquer pessoa**.
5. Clique em **Implantar**, autorize com a sua conta (o Google avisa que o app não foi verificado: clique em "Avançado" e em "Acessar"; o app é seu).
6. Copie o **URL do app da Web** (termina em `/exec`).

## 2. Colocar o endereço no Scanner

Mande o URL para o Claude, que atualiza o arquivo. Ou faça você mesmo: abra o `index.html` num editor de texto, procure a linha

```
var SHEETS_URL = '';
```

e cole o URL entre as aspas.

## 3. Publicar o link próprio (Netlify, grátis)

1. Entre em app.netlify.com/drop e crie uma conta.
2. Arraste a pasta `scanner-via-aurea` (com o `index.html` dentro) para a página.
3. O Netlify gera um link. Em **Site configuration > Change site name** você pode trocar para algo como `scanner-via-aurea.netlify.app`.

Para atualizar depois, é só arrastar a pasta de novo em **Deploys**.

## O que aparece na planilha

**Aba Leads:** uma linha por pessoa, atualizada a cada passo: nome, WhatsApp, bairro, como conheceu, porta escolhida, última etapa, se concluiu, código do resultado, resumo das respostas e se clicou no WhatsApp. Quem parou no meio aparece com "Concluiu? Não" e a última etapa em que parou.

**Aba Eventos:** o histórico de cada passo, com data e hora.

## Cuidados

- O visitante autoriza na primeira tela a guarda dos dados e o contato pelo WhatsApp (LGPD). A planilha deve ficar só com quem atende.
- Para conferir se está funcionando, faça um Scanner de teste e veja a linha aparecer na aba Leads.
- O link do claude.ai continua funcionando, mas **não grava na planilha**: o claude.ai não deixa a página enviar dados para fora. Para divulgar, use o link do Netlify.
