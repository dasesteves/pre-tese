# Pré-Tese - Optimization and Standardization of Medication Management Processes in Hospital Environments

## Descrição
Este projeto contém a estrutura LaTeX para a pré-tese do Mestrado em Engenharia Bioinformática da Universidade do Minho.

**Autor:** Diogo André da Silva Esteves  

## Estrutura do Projeto

```
pre-tese/
├── chapters/           # Capítulos da pré-tese
│   ├── Introducao.tex
│   ├── EstadoDaArte.tex
│   ├── PlanoDeTrabalho.tex
│   ├── Metodologia.tex
│   ├── Resultados.tex
│   ├── Discussao.tex
│   └── Conclusao.tex
├── preamble/           # Páginas iniciais
│   ├── Abstract.tex
│   └── Acknowledgements.tex
├── covers/             # Capas
│   ├── Covers.tex
│   └── BackCover.tex
├── images/             # Imagens e logos
│   ├── logos/
│   └── logosB/
├── pre-tese.tex       # Arquivo principal
├── pre-tese.sty       # Arquivo de estilo
├── pre-tese.bib       # Bibliografia
└── README.md          # Este arquivo
```

## Requisitos do Sistema

### LaTeX
- **Compilador:** XeLaTeX (obrigatório devido às fontes personalizadas)
- **Distribuição:** TeX Live (recomendado) ou MiKTeX

### Packages LaTeX Necessários
- fontspec
- babel
- geometry
- hyperref
- natbib
- glossaries
- amsmath, amsthm, amssymb
- graphicx
- pgfgantt (para diagramas de Gantt)
- E outros listados em `pre-tese.sty`

## Configuração do VS Code

### Extensões Recomendadas
1. **LaTeX Workshop** - Essencial para compilação e preview
2. **LaTeX Utilities** - Funções adicionais úteis
3. **PDF Viewer** - Visualização integrada de PDFs
4. **Code Spell Checker** - Verificação ortográfica
5. **Portuguese - Code Spell Checker** - Dicionário português

### Configuração das Settings (settings.json)
```json
{
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "xelatex",
            "tools": ["xelatex"]
        }
    ],
    "latex-workshop.latex.autoClean.run": "onBuilt"
}
```

## Como Compilar

### Usando VS Code
1. Abra o arquivo `pre-tese.tex`
2. Use Ctrl+Alt+B (ou Cmd+Option+B no Mac) para compilar
3. O PDF será gerado automaticamente

### Linha de Comando
```bash
xelatex pre-tese.tex
bibtex pre-tese
makeglossaries pre-tese
xelatex pre-tese.tex
xelatex pre-tese.tex
```

## Estrutura dos Capítulos

### 1. Introdução
- Contexto e enquadramento
- Definição do problema
- Objetivos (geral e específicos)
- Organização da tese

### 2. Estado da Arte
- Domínio científico/biológico
- Domínio tecnológico/informático
- Relação entre os domínios
- Lacunas identificadas

### 3. Plano de Trabalho
- Pipeline geral do projeto
- Calendarização das tarefas
- Diagrama de Gantt
- Recursos necessários
- Riscos e mitigação

### 4. Metodologia
- Abordagem metodológica geral
- Metodologia de desenvolvimento de software
- Tecnologias e ferramentas
- Validação e avaliação

### 5. Resultados
- [A preencher conforme o progresso]

### 6. Discussão
- [A preencher conforme o progresso]

### 7. Conclusões e Trabalho Futuro
- Resumo dos resultados
- Principais contribuições
- Limitações identificadas
- Trabalho futuro

## Edição dos Conteúdos

### Para Começar
1. Edite o arquivo `preamble/Abstract.tex` com o resumo
2. Atualize os nomes dos orientadores em `pre-tese.tex`
3. Preencha os capítulos seguindo a estrutura fornecida
4. Adicione referências bibliográficas em `pre-tese.bib`

### Gestão de Referências
- Use o formato BibTeX em `pre-tese.bib`
- Cite referencias com `\cite{key}`
- Use `\citep{key}` para citações entre parênteses

### Glossários e Acrónimos
- Defina acrónimos com `\newacronym{key}{abrev}{definição}`
- Use `\gls{key}` para referenciar

## Troubleshooting

### Problemas Comuns
1. **Erro de compilação:** Verifique se está usando XeLaTeX
2. **Fontes não encontradas:** As fontes NewsGotT são opcionais
3. **Packages em falta:** Instale via tlmgr ou MiKTeX Package Manager

### Suporte
- Documentação LaTeX: https://www.latex-project.org/help/documentation/
- VS Code LaTeX Workshop: https://github.com/James-Yu/LaTeX-Workshop

## Licença
Este template é baseado no template oficial da Universidade do Minho. 
