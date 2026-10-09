# Gestão de medicação em ambiente hospitalar

Pré-tese de **Diogo André da Silva Esteves**, do Mestrado em Engenharia Bioinformática da Universidade do Minho.

O trabalho propõe uma plataforma que reúna fluxos clínico-farmacêuticos dispersos por diferentes sistemas. A proposta segue uma abordagem de *Design Science Research* e descreve o desenvolvimento e a avaliação de uma solução web para apoiar os processos de gestão da medicação.

[**Ler a pré-tese em PDF**](pre-tese.pdf) · [Resumo](preamble/Abstract.tex) · [Capítulos](chapters/)

## O que está neste repositório

- [Documento principal](pre-tese.tex) e [capítulos](chapters/): fontes LaTeX da pré-tese.
- [Bibliografia](pre-tese.bib): referências utilizadas.
- [Estilo](pre-tese.sty), [capas](covers/) e [imagens](images/): composição do documento.

O título original é *Optimization and Standardization of Medication Management Processes in Hospital Environments*. O resumo apresenta objetivos e uma avaliação prevista; não demonstra, por si só, resultados de eficácia ou a utilização de uma plataforma em produção.

Este é o repositório da pré-tese, não da dissertação final. O PDF está versionado, mas a correspondência entre esse ficheiro e a revisão atual das fontes não foi verificada por recompilação.

<details>
<summary>Editar e compilar as fontes</summary>

É necessário um ambiente LaTeX com **XeLaTeX** e **BibTeX**. Os pacotes usados estão declarados em [pre-tese.sty](pre-tese.sty) e no [documento principal](pre-tese.tex).

Executar a partir da raiz do repositório, num ambiente já preparado:

```sh
xelatex pre-tese.tex
bibtex pre-tese
xelatex pre-tese.tex
xelatex pre-tese.tex
```

Esta sequência acompanha o uso de `fontspec` e da bibliografia nas fontes; não foi executada nesta revisão. A compilação pode exigir ajustes no ambiente e nos pacotes disponíveis.

Manter as fontes NewsGotT incluídas na raiz: o estilo usa essas famílias nas capas. Os acrónimos atuais são uma lista no documento principal; este projeto não requer uma etapa `makeglossaries` para essa lista.

O modelo de composição é identificado na documentação original como baseado no template da Universidade do Minho. Essa atribuição não define, por si só, uma licença de reutilização.

</details>
