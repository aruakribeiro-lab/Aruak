/**
 * Scanner da Obra · Via Áurea
 * Recebe os dados do Scanner e grava na planilha onde este script está.
 *
 * Abas criadas automaticamente:
 *  - Leads: uma linha por pessoa, atualizada a cada passo (quem parou no meio também aparece).
 *  - Eventos: histórico de tudo o que aconteceu, uma linha por passo.
 */

var ABA_LEADS = 'Leads';
var ABA_EVENTOS = 'Eventos';
var COLUNAS_LEADS = ['ID', 'Primeiro acesso', 'Último acesso', 'Nome', 'WhatsApp', 'Bairro e cidade', 'Como conheceu',
  'Porta escolhida', 'Última etapa', 'Concluiu?', 'Código do resultado', 'Resumo das respostas', 'Clicou no WhatsApp?'];
var COLUNAS_EVENTOS = ['Data e hora', 'ID', 'Nome', 'Evento', 'Porta', 'Etapa', 'Código'];

function doPost(e) {
  var trava = LockService.getScriptLock();
  trava.waitLock(10000);
  try {
    var d = JSON.parse(e.postData.contents || '{}');
    if (!d.id) return resposta('sem id');
    var planilha = SpreadsheetApp.getActiveSpreadsheet();
    var agora = new Date();

    var eventos = aba(planilha, ABA_EVENTOS, COLUNAS_EVENTOS);
    eventos.appendRow([agora, limpa(d.id), limpa(d.nome), limpa(d.evento), limpa(d.porta), limpa(d.etapa), limpa(d.codigo)]);

    var leads = aba(planilha, ABA_LEADS, COLUNAS_LEADS);
    var linha = acharLinha(leads, d.id);
    if (!linha) {
      leads.appendRow([limpa(d.id), agora, agora, limpa(d.nome), limpa(d.whatsapp), limpa(d.bairro), limpa(d.origem),
        limpa(d.porta), '', 'Não', '', '', 'Não']);
      linha = leads.getLastRow();
    }
    var c = function (nome) { return COLUNAS_LEADS.indexOf(nome) + 1; };
    leads.getRange(linha, c('Último acesso')).setValue(agora);
    if (d.nome) leads.getRange(linha, c('Nome')).setValue(limpa(d.nome));
    if (d.whatsapp) leads.getRange(linha, c('WhatsApp')).setValue(limpa(d.whatsapp));
    if (d.bairro) leads.getRange(linha, c('Bairro e cidade')).setValue(limpa(d.bairro));
    if (d.porta) leads.getRange(linha, c('Porta escolhida')).setValue(limpa(d.porta));
    if (d.evento === 'etapa' && d.etapa) leads.getRange(linha, c('Última etapa')).setValue(limpa(d.etapa));
    if (d.evento === 'resultado') {
      leads.getRange(linha, c('Concluiu?')).setValue('Sim');
      leads.getRange(linha, c('Última etapa')).setValue('Resultado');
      leads.getRange(linha, c('Código do resultado')).setValue(limpa(d.codigo));
      leads.getRange(linha, c('Resumo das respostas')).setValue(limpa(d.resumo));
    }
    if (d.evento === 'whatsapp') leads.getRange(linha, c('Clicou no WhatsApp?')).setValue('Sim');
    return resposta('ok');
  } catch (erro) {
    return resposta('erro: ' + erro);
  } finally {
    trava.releaseLock();
  }
}

function doGet() {
  return resposta('Scanner da Obra · Via Áurea: recebimento ativo.');
}

function aba(planilha, nome, colunas) {
  var a = planilha.getSheetByName(nome);
  if (!a) {
    a = planilha.insertSheet(nome);
    a.appendRow(colunas);
    a.setFrozenRows(1);
    a.getRange(1, 1, 1, colunas.length).setFontWeight('bold');
  }
  return a;
}

function acharLinha(a, id) {
  var n = a.getLastRow();
  if (n < 2) return 0;
  var ids = a.getRange(2, 1, n - 1, 1).getValues();
  for (var i = ids.length - 1; i >= 0; i--) if (String(ids[i][0]) === String(id)) return i + 2;
  return 0;
}

// Evita que um texto digitado pelo visitante vire fórmula na planilha
function limpa(v) {
  if (v === undefined || v === null) return '';
  var s = String(v).slice(0, 5000);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}

function resposta(t) {
  return ContentService.createTextOutput(t).setMimeType(ContentService.MimeType.TEXT);
}
