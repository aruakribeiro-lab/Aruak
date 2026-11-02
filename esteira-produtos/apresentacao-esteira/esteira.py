# -*- coding: utf-8 -*-
"""Gera a apresentação da esteira para a equipe (HTML -> PDF paisagem)."""
import base64, os, sys
D = sys.argv[1] if len(sys.argv) > 1 else '.'
FONTS = open(os.path.join(D, 'fonts.css')).read()
SELO = base64.b64encode(open(os.path.join(D, 'selo600.png'), 'rb').read()).decode()

ST = {  # estágio: (rótulo, classe)
    'pub': ('Publicado', 's-pub'), 'vend': ('Já vende', 's-vend'), 'teste': ('Em teste', 's-teste'),
    'estr': ('Estruturado', 's-estr'), 'cons': ('Sob consulta', 's-cons'), 'op': ('Por oportunidade', 's-op'), 'novo': ('Novo', 's-novo'),
}
def pill(k): l, c = ST[k]; return f'<span class="pill {c}">{l}</span>'

DEG = [
    (1, 'Porta de entrada', 'Grátis. Qualifica sem gastar o tempo do engenheiro.', [
        ('Problema no imóvel', 'Scanner: porta do problema', 'Grátis', 'pub'),
        ('Obra em andamento', 'Scanner: Raio-X da Obra', 'Grátis', 'pub'),
        ('Prédio', 'Dossiê do Prédio', 'Grátis', 'teste')]),
    (2, 'Diagnóstico', 'O cliente paga para decidir com segurança.', [
        ('Problema sem causa clara', 'Visita Diagnóstica', 'R$ 1.200', 'teste'),
        ('Parcela para pagar', 'Conferência da Medição', 'R$ 1.800*', 'estr')]),
    (3, 'Laudos e documentos', 'O cliente compra um documento para mostrar a alguém.', [
        ('Documento técnico', 'Laudo', 'a partir de R$ 3.000', 'vend'),
        ('Receber ou comprar', 'Vistoria de recebimento e de compra', 'R$ 840 a R$ 1.950', 'vend'),
        ('Segurança do trabalho', 'PGR e LTCAT, com PCMSO por médico parceiro', 'sob cotação', 'novo'),
        ('Regularização', 'Regularização de imóveis', 'sob cotação', 'op'),
        ('Disputa', 'Perícia e assistência técnica', 'sob cotação', 'op'),
        ('Prefeitura', 'EIV e EIT', 'sob cotação', 'op')]),
    (4, 'Obras', 'O cliente compra o problema resolvido no imóvel.', [
        ('Antes de começar', 'Estudo de Viabilidade Financeira', 'R$ 2.500', 'teste'),
        ('Antes de começar', 'Orçamento Executivo com Plano de Obra', 'R$ 5.000', 'teste'),
        ('Já começou', 'Plano para Terminar a Obra', 'R$ 4.500 ou R$ 5.500*', 'estr'),
        ('Obra pequena', 'Reparo Rápido', 'preço fechado após medição', 'cons'),
        ('Conduzir a obra', 'Gestão de Obra', 'honorário mensal', 'cons')]),
    (5, 'Parcerias', 'Quem indica clientes e recebe comissão pela venda.', [
        ('Arquitetos', 'Parceria com escritórios de arquitetura', 'Obra fechada: 4% · laudos e vistorias: 10 a 15%', 'teste'),
        ('Corretores', 'Parceria com corretores de imóveis', 'Obra fechada: 4% · laudos e vistorias: 10 a 15%', 'novo')]),
    (6, 'Recorrência', 'O cliente fica e paga todo mês.', [
        ('Condomínio', 'Engenheiro do Condomínio', 'R$ 1.600 ou R$ 2.200/mês', 'teste'),
        ('Escola', 'Engenheiro da Escola (Tip Toy)', 'R$ 1.800/mês compensado', 'op'),
        ('Empresa', 'Engenheiro da Empresa', 'R$ 3.000/mês', 'op')]),
]

def foot(n):
    return f'<div class="foot"><span>ENTRE COLUNAS · Engenharia de Previsibilidade</span><span>Esteira de produtos · versão para discussão · novembro de 2026</span><span>{n}</span></div>'

def head(kick, title, sub=''):
    return f'<div class="kick">{kick}</div><h1>{title}</h1>' + (f'<p class="sub">{sub}</p>' if sub else '')

def capa():
    return f'''<section class="pg cover">
<img class="selo" src="data:image/png;base64,{SELO}" alt="Selo da Construtora Entre Colunas">
<div class="ctext">
<div class="brand">ENTRE COLUNAS</div>
<div class="tag">Engenharia de Previsibilidade · Goiânia</div>
<h1>Nossa esteira<br>de produtos</h1>
<p>Seis degraus, do primeiro contato até o cliente que fica com a gente. Uma proposta para olharmos juntos e ajustarmos antes de colocar em prática.</p>
<div class="meta">Versão para discussão com a equipe · novembro de 2026</div>
</div></section>'''

CURTO = {'Scanner: porta do problema': 'Scanner do problema', 'Scanner: Raio-X da Obra': 'Raio-X da Obra',
    'Vistoria de recebimento e de compra': 'Vistoria', 'PGR e LTCAT, com PCMSO por médico parceiro': 'Segurança do trabalho: PGR, LTCAT e PCMSO',
    'Regularização de imóveis': 'Regularização', 'Perícia e assistência técnica': 'Perícia e assistência técnica',
    'Estudo de Viabilidade Financeira': 'Viabilidade Financeira', 'Orçamento Executivo com Plano de Obra': 'Orçamento Executivo',
    'Engenheiro da Escola (Tip Toy)': 'Engenheiro da Escola'}

def escada():
    cols = ''
    for n, nome, desc, br in DEG:
        items = ''.join(f'<li>{CURTO.get(b[1], b[1]) if n != 5 else b[0]}</li>' for b in br)
        cls = 'step dash' if n == 5 else 'step'
        cols += f'''<div class="{cls}" style="height:{58 + n * 7}%"><div class="num">{n}</div><div class="sn">{nome}</div><div class="sd">{desc}</div><ul>{items}</ul></div>'''
    return f'''<section class="pg">{head('A esteira em uma página', 'Seis degraus, do primeiro contato ao cliente que fica')}
<div class="stairs">{cols}</div>
<div class="legend"><div><b>Como ler:</b> cada entrega termina com a oferta do degrau seguinte. Os degraus 3 e 4 correm lado a lado: o cliente pode entrar direto em qualquer um, e um laudo de defeito costuma terminar numa obra.</div>
<div><b>O degrau 5 é diferente:</b> o parceiro não compra, ele indica. Arquitetos e corretores alimentam todos os outros degraus e recebem comissão: 4% sobre obra fechada e de 10% a 15% sobre laudos e vistorias de recebimento.</div></div>
{foot(2)}</section>'''

def caminhos():
    J = [
        ('Tenho um problema no imóvel', ['Scanner', 'Visita Diagnóstica', 'Laudo ou Reparo Rápido', 'Recorrência, se for prédio'], 'navy'),
        ('Vou começar uma obra', ['Scanner ou arquiteto', 'Estudo de Viabilidade Financeira', 'Orçamento Executivo', 'Gestão de Obra'], 'navy'),
        ('Já estou no meio da obra', ['Raio-X da Obra', 'Conferência da Medição', 'Plano para Terminar', 'Gestão da conclusão ou a equipe dele termina'], 'navy'),
        ('Vou comprar ou receber um imóvel', ['Scanner ou corretor', 'Vistoria de compra ou de recebimento', 'Regularização ou laudo', 'Reparo ou obra'], 'navy'),
        ('Cuido de um prédio', ['Dossiê do Prédio', 'Implantação', 'Engenheiro do Condomínio todo mês'], 'gold'),
        ('Tenho uma empresa', ['PGR e LTCAT', 'Revisão periódica', 'Engenheiro da Empresa'], 'gold'),
    ]
    rows = ''
    for t, steps, c in J:
        chips = '<span class="arr">→</span>'.join(f'<span class="chip {c}">{s}</span>' for s in steps)
        rows += f'<div class="jr"><div class="jt">{t}</div><div class="js">{chips}</div></div>'
    return f'''<section class="pg">{head('Os caminhos do cliente', 'Por onde cada cliente entra e para onde ele sobe', 'O cliente não precisa conhecer a esteira. Ele chega com uma situação, e a esteira mostra o próximo passo.')}
<div class="journeys">{rows}</div>
<div class="note">Arquitetos trazem principalmente o caminho de quem vai começar uma obra. Corretores trazem o de quem vai comprar ou receber um imóvel.</div>
{foot(3)}</section>'''

def card(n, nome, desc, br):
    rows = ''.join(f'<tr><td class="b">{b[0]}</td><td class="p">{b[1]}</td><td class="v">{b[2]}</td><td>{pill(b[3])}</td></tr>' for b in br)
    return f'''<div class="card"><div class="ch"><span class="cn">{n}</span><div><div class="ct">{nome}</div><div class="cd">{desc}</div></div></div>
<table><thead><tr><th>Braço</th><th>Produto</th><th>Preço</th><th>Situação</th></tr></thead><tbody>{rows}</tbody></table></div>'''

def detalhe(idx, page, title):
    if idx == [0, 1, 2]:
        cards = '<div class="stackc">' + card(*DEG[0]) + card(*DEG[1]) + '</div>' + card(*DEG[2])
        idx = [0, 1]
    else:
        cards = ''.join(card(*DEG[i]) for i in idx)
    return f'''<section class="pg">{head('Degraus em detalhe', title)}<div class="cards c{len(idx)}">{cards}</div>
<p class="small">* Preços propostos, ainda em validação. “Por oportunidade”: atendemos quando aparece, mas não entra nas metas até 18/12.</p>{foot(page)}</section>'''

def parcerias():
    return f'''<section class="pg">{head('Degrau 5 · Parcerias', 'Arquitetos e corretores: quem mais vai trazer clientes', 'A conversa com o parceiro é outra. Ele não compra nada: indica, e cada indicação coloca a reputação dele em jogo.')}
<div class="two">
<div class="pcard"><div class="ph">Arquitetos <span class="pill s-teste">Em teste</span></div>
<p><b>O que o arquiteto ganha:</b> o projeto vira obra construída e entra no portfólio do escritório. A autoria é preservada, o cliente não abandona o projeto por causa do orçamento, e a Entre Colunas não faz projeto, então não disputa o cliente.</p>
<p><b>O que ele traz:</b> Estudo de Viabilidade Financeira, Orçamento Executivo, Gestão de Obra e Visita Diagnóstica.</p>
<p><b>Como começa:</b> dois escritórios conhecidos, um projeto real de cada, conversa de 30 minutos e reunião com o proprietário. Se o mesmo escritório trouxer um segundo cliente, abrimos a rede de arquitetos em janeiro.</p></div>
<div class="pcard"><div class="ph">Corretores <span class="pill s-novo">Novo</span></div>
<p><b>O que o corretor ganha:</b> a venda não trava. Imóvel regularizado, vistoria antes da compra e menos desistência na hora de assinar.</p>
<p><b>O que ele traz:</b> Vistoria de compra, Regularização de imóveis, Laudo e Reparo Rápido antes da venda.</p>
<p><b>O que muda para nós:</b> corretor precisa de resposta em horas, não em dias. A regularização deixa de ser só “por oportunidade” e passa a ser central.</p>
<p><b>Ainda a desenhar:</b> abordagem, mensagens e o teste com os primeiros corretores.</p></div>
</div>
<div class="band"><div class="rates"><div><span class="big">4%</span><span class="rl">sobre obra fechada</span></div><div><span class="big">10 a 15%</span><span class="rl">sobre laudos e vistorias de recebimento</span></div></div><div><b>Comissão por venda indicada, para arquitetos e corretores.</b> É comissão pela venda, como a do corretor, e não reserva técnica. Ela pode virar desconto para o cliente ou pagamento ao profissional, conforme o acordo entre os técnicos envolvidos.</div></div>
<div class="kpis"><div><b>Indicações</b><span>por parceiro, por mês</span></div><div><b>Conversão</b><span>indicações que viram contrato</span></div><div><b>Receita</b><span>por parceiro</span></div><div><b>Tempo de resposta</b><span>da indicação ao primeiro contato</span></div></div>
{foot(6)}</section>'''

def situacao():
    from collections import Counter
    c = Counter(b[3] for _, _, _, br in DEG for b in br)
    order = ['vend', 'pub', 'teste', 'estr', 'cons', 'novo', 'op']
    tiles = ''.join(f'<div class="tile {ST[k][1]}"><b>{c[k]}</b><span>{ST[k][0]}</span></div>' for k in order)
    return f'''<section class="pg">{head('Onde estamos hoje', f'{sum(c.values())} produtos, e o que mais destrava o crescimento')}
<div class="tiles">{tiles}</div>
<div class="two">
<div><h2>O que já funciona</h2><ul class="lst"><li><b>Laudo e Vistoria vendem:</b> são mais de 100 vistorias entregues. É a base que paga as contas hoje.</li>
<li><b>O Scanner está publicado</b>, com o Raio-X para quem já está no meio da obra.</li></ul>
<h2>O que ainda precisa de prova</h2><ul class="lst"><li>Diagnóstico, Obras e Condomínio estão em teste, sem contrato medido no formato novo.</li>
<li>A recorrência depende de um só piloto, o Edifício Trípoli.</li></ul></div>
<div><h2>O que mais destrava</h2><ol class="lst"><li>Liberar o link do Scanner para clientes.</li><li>Definir o apoio técnico de orçamento, que faz o Estudo de Viabilidade, o Orçamento Executivo e o Plano para Terminar pagarem a meta.</li>
<li>Fechar a proposta do Trípoli.</li><li>Começar a parceria com os dois primeiros escritórios e desenhar a dos corretores.</li><li>Medir horas reais nas próximas visitas, vistorias e obras.</li></ol></div>
</div>{foot(7)}</section>'''

def perguntas():
    Q = ['A divisão entre <b>Laudos e documentos</b> (o cliente compra um papel) e <b>Obras</b> (o cliente compra o problema resolvido) faz sentido para quem atende o cliente?',
         'Falta algum serviço que já fazemos? Tem algum aqui que não deveríamos oferecer?',
         'Os preços batem com o que vocês ouvem dos clientes?',
         'Quais arquitetos e corretores vocês conhecem que poderiam ser os primeiros parceiros?',
         'Em qual degrau vocês sentem que perdemos mais clientes hoje? Por quê?',
         'Qual pergunta os clientes mais fazem e ainda não tem resposta na esteira?']
    qs = ''.join(f'<div class="q"><div class="qn">{i + 1}</div><div class="qt">{q}<div class="lines"><i></i><i></i></div></div></div>' for i, q in enumerate(Q))
    return f'''<section class="pg">{head('Para a nossa conversa', 'Queremos ouvir vocês', 'Anote aqui o que pensar. Toda opinião ajuda a esteira a ficar mais perto do dia a dia do escritório.')}
<div class="qs">{qs}</div>{foot(8)}</section>'''

CSS = FONTS + r'''
@page { size: 297mm 210mm; margin: 0; }
:root { --navy:#1b3a5c; --deep:#12283f; --gold:#c9a227; --gink:#8a6a0c; --paper:#f6f3ec; --ink:#14202c; --muted:#5b6774; --line:#d9d3c4; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin:0; font-family:"Source Sans 3", Arial, sans-serif; color:var(--ink); font-size:11.5pt; line-height:1.4; }
.pg { width:297mm; height:210mm; padding:13mm 15mm 16mm; position:relative; overflow:hidden; background:var(--paper); break-after:page; }
.pg:last-child { break-after:auto; }
.kick { font-family:"Barlow Semi Condensed"; font-weight:700; letter-spacing:.14em; text-transform:uppercase; font-size:9pt; color:var(--gink); }
h1 { font-family:"Barlow Semi Condensed"; font-weight:700; font-size:25pt; line-height:1.1; margin:1.5mm 0 1.5mm; color:var(--deep); }
.sub { margin:0 0 4mm; color:var(--muted); font-size:11pt; max-width:220mm; }
h2 { font-family:"Barlow Semi Condensed"; font-size:16pt; color:var(--navy); margin:3mm 0 1.5mm; }
.foot { position:absolute; left:15mm; right:15mm; bottom:7mm; display:flex; justify-content:space-between; font-size:7.5pt; color:var(--muted); border-top:1px solid var(--line); padding-top:2mm; }
/* capa */
.cover { background:var(--navy); color:#fff; display:flex; align-items:center; gap:16mm; padding:0 22mm; border-bottom:6mm solid var(--gold); }
.cover .selo { width:100mm; height:100mm; flex:0 0 auto;  }
.cover .brand { font-family:"Cinzel"; font-weight:700; letter-spacing:.18em; font-size:20pt; color:#fff; }
.cover .tag { color:#c9d6e4; letter-spacing:.06em; font-size:11pt; margin-top:1mm; }
.cover h1 { color:#fff; font-size:46pt; margin:9mm 0 5mm; }
.cover p { font-size:13pt; color:#dfe7f0; max-width:120mm; margin:0; }
.cover .meta { margin-top:10mm; color:var(--gold); font-family:"Barlow Semi Condensed"; font-weight:600; letter-spacing:.08em; text-transform:uppercase; font-size:10pt; }
/* escada */
.stairs { display:flex; align-items:flex-end; gap:3mm; height:128mm; margin-top:2mm; }
.step { flex:1; background:#fff; border:1px solid var(--line); border-top:2.2mm solid var(--navy); border-radius:2mm 2mm 0 0; padding:3mm 3mm 2mm; display:flex; flex-direction:column; }
.step:nth-child(6) { background:var(--navy); color:#fff; border-color:var(--navy); border-top-color:var(--gold); }
.step:nth-child(6) .sd { color:#c9d6e4; } .step:nth-child(6) li { color:#fff; } .step:nth-child(6) .num { color:var(--gold); }
.step.dash { border:1.4px dashed var(--gold); border-top:2.2mm solid var(--gold); background:#fffaf0; }
.num { font-family:"Barlow Semi Condensed"; font-weight:700; font-size:26pt; line-height:1; color:var(--gold); }
.sn { font-family:"Barlow Semi Condensed"; font-weight:700; font-size:15pt; line-height:1.1; margin-top:1mm; }
.sd { font-size:9.2pt; color:var(--muted); margin:1mm 0 2mm; line-height:1.3; }
.step ul { margin:0; padding:0; list-style:none; font-size:9.6pt; line-height:1.3; }
.step li { padding:1mm 0; border-top:1px solid rgba(128,128,128,.25); }
.legend { display:grid; grid-template-columns:1fr 1fr; gap:6mm; margin-top:4mm; font-size:10.5pt; color:var(--ink); }
.legend b { color:var(--navy); }
/* caminhos */
.journeys { display:flex; flex-direction:column; gap:3.2mm; margin-top:2mm; }
.jr { display:grid; grid-template-columns:58mm 1fr; align-items:center; gap:4mm; background:#fff; border:1px solid var(--line); border-radius:2mm; padding:4mm 5mm; }
.jt { font-family:"Barlow Semi Condensed"; font-weight:700; font-size:14pt; color:var(--deep); line-height:1.15; }
.js { display:flex; align-items:center; flex-wrap:wrap; gap:1.5mm; }
.chip { display:inline-block; padding:2mm 3.4mm; border-radius:5mm; font-size:10.5pt; font-weight:600; }
.chip.navy { background:#e3eaf2; color:var(--navy); } .chip.gold { background:#f5ead0; color:var(--gink); }
.js .chip:last-child { background:var(--navy); color:#fff; }
.arr { color:var(--gold); font-weight:700; font-size:12pt; }
.note { margin-top:5mm; font-size:11pt; color:var(--muted); }
/* cards */
.cards { display:grid; gap:5mm; margin-top:2mm; }
.cards.c3 { grid-template-columns:1fr 1fr 1fr; } .stackc { display:flex; flex-direction:column; gap:5mm; } .cards.c2 { grid-template-columns:1fr 1fr; }
.card { background:#fff; border:1px solid var(--line); border-radius:2.5mm; padding:4mm; }
.ch { display:flex; gap:3mm; align-items:center; margin-bottom:3mm; }
.cn { font-family:"Barlow Semi Condensed"; font-weight:700; font-size:22pt; color:#fff; background:var(--navy); width:13mm; height:13mm; border-radius:50%; display:flex; align-items:center; justify-content:center; flex:0 0 auto; }
.ct { font-family:"Barlow Semi Condensed"; font-weight:700; font-size:15pt; color:var(--deep); line-height:1.1; }
.cd { font-size:9.6pt; color:var(--muted); }
.card table { width:100%; border-collapse:collapse; font-size:10.8pt; }
.card th { text-align:left; font-size:8pt; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); border-bottom:1.5px solid var(--navy); padding:1mm 1.2mm; }
.card td { border-bottom:1px solid #ece7db; padding:2.6mm 1.2mm; vertical-align:top; }
.card td.b { color:var(--gink); font-weight:600; width:24%; } .card td.p { font-weight:600; } .card td.v { white-space:normal; width:22%; }
.pill { display:inline-block; font-size:8pt; font-weight:700; padding:.4mm 2mm; border-radius:3mm; white-space:nowrap; }
.s-pub { background:#dbeee3; color:#1f6b45; } .s-vend { background:#1f7a4d; color:#fff; } .s-teste { background:#fbecc9; color:#7a5a00; }
.s-estr { background:#e3eaf2; color:var(--navy); } .s-cons { background:#ece6f3; color:#5a3d7a; } .s-op { background:#ececec; color:#555; } .s-novo { background:var(--gold); color:#fff; }
.small { font-size:8.6pt; color:var(--muted); margin-top:3mm; }
/* parcerias */
.two { display:grid; grid-template-columns:1fr 1fr; gap:6mm; }
.pcard { background:#fff; border:1px solid var(--line); border-top:2mm solid var(--gold); border-radius:2mm; padding:4mm 5mm; font-size:10.6pt; }
.pcard p { margin:0 0 2mm; }
.ph { font-family:"Barlow Semi Condensed"; font-weight:700; font-size:16pt; color:var(--deep); margin-bottom:2mm; display:flex; align-items:center; gap:3mm; }
.band { display:flex; align-items:center; gap:6mm; background:var(--navy); color:#fff; border-radius:2.5mm; padding:4mm 6mm; margin-top:5mm; font-size:10.8pt; }
.band .big { display:block; font-family:"Barlow Semi Condensed"; font-weight:700; font-size:28pt; color:var(--gold); line-height:1; white-space:nowrap; } .rates { display:flex; gap:7mm; flex:0 0 auto; } .rl { display:block; font-size:8.6pt; color:#c9d6e4; max-width:38mm; margin-top:1mm; }
.kpis { display:grid; grid-template-columns:repeat(4,1fr); gap:4mm; margin-top:4mm; }
.kpis div { border-left:1.5mm solid var(--gold); background:#fff; padding:2mm 3mm; }
.kpis b { display:block; font-family:"Barlow Semi Condensed"; font-size:12pt; color:var(--navy); } .kpis span { font-size:9.6pt; color:var(--muted); }
/* situação */
.tiles { display:grid; grid-template-columns:repeat(7,1fr); gap:3mm; margin:2mm 0 4mm; }
.tile { border-radius:2.5mm; padding:5mm 3mm; text-align:center; }
.tile b { display:block; font-family:"Barlow Semi Condensed"; font-size:34pt; line-height:1; } .tile span { font-size:10pt; font-weight:600; }
.lst { margin:0; padding-left:5mm; font-size:12pt; } .lst li { margin-bottom:2.6mm; }
/* perguntas */
.qs { display:grid; grid-template-columns:1fr 1fr; gap:4mm 8mm; margin-top:2mm; }
.q { display:flex; gap:3mm; }
.qn { font-family:"Barlow Semi Condensed"; font-weight:700; font-size:15pt; color:#fff; background:var(--gold); width:9mm; height:9mm; border-radius:50%; display:flex; align-items:center; justify-content:center; flex:0 0 auto; }
.qt { font-size:11.5pt; flex:1; }
.lines i { display:block; border-bottom:1px solid #bfb8a6; height:9mm; }
'''

html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Esteira de produtos · Entre Colunas</title><style>' + CSS + '</style></head><body>' +
        capa() + escada() + caminhos() + detalhe([0, 1, 2], 4, 'Porta de entrada, diagnóstico e laudos') +
        detalhe([3, 5], 5, 'Obras e recorrência') + parcerias() + situacao() + perguntas() + '</body></html>')
open(os.path.join(D, 'esteira.html'), 'w').write(html)
print('ok', len(html))
