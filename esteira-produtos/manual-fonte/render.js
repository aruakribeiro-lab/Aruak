const {chromium} = require('playwright');
(async () => {
  const [,, html, pdf] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + html, {waitUntil: 'load'});
  const foot = `<div style="width:100%;font-family:'DejaVu Sans',Arial,sans-serif;font-size:6.6pt;color:#7a868c;padding:0 15mm;display:flex;justify-content:space-between;">
  <span>ENTRE COLUNAS&nbsp;&nbsp;/&nbsp;&nbsp;Manual operacional das seis frentes&nbsp;&nbsp;/&nbsp;&nbsp;v1.0 · 01.11.2026</span>
  <span><span class="pageNumber"></span> de <span class="totalPages"></span></span></div>`;
  await p.pdf({path: pdf, format: 'A4', printBackground: true, preferCSSPageSize: true,
    outline: true, tagged: true, displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: foot,
    margin: {top: '14mm', bottom: '17mm', left: '15mm', right: '15mm'}});
  await b.close();
})();
