# Fonte do Manual Operacional das seis frentes

Gera `../Manual_Operacional_Entre_Colunas_6_Frentes.pdf`. Todas as contas saem de `calc.py`; cada frente tem seu arquivo (`s1_scanner.py` a `s6_condo.py`), mais estrutura da empresa (`s7`), quadro de ações (`s8`) e dúvidas (`s9`).

Para regerar (Python 3 com pypdf, Node com Playwright, poppler-utils):

```bash
python3 build.py && node render.js "$PWD/manual.html" "$PWD/manual.pdf" && python3 pages.py manual.pdf && python3 build.py pages.json && node render.js "$PWD/manual.html" "$PWD/manual.pdf" && python3 conferencia.py manual.pdf
```

`conferencia.py` recalcula os números do consolidado de 01/11/2026 de forma independente e confere se aparecem no PDF, além de checar as seis fichas e o título da última seção.
