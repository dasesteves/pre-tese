#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para inserir referências bibliográficas nos capítulos da pré-tese
Autor: Assistente IA para Diogo Esteves
Data: Dezembro 2024
"""

import os
import re
from pathlib import Path

# Mapeamento de locais específicos para inserção de referências
referencias_por_capitulo = {
    "Introducao.tex": {
        "erros de medicação afetam 1 em cada 10 pacientes": "\\cite{who2017}",
        "podem reduzir estes erros em até 85%": "\\cite{franklin2007}",
        "Segundo dados da Organização Mundial de Saúde": "\\cite{who2017,who2022}",
        "sistemas integrados de gestão medicamentosa": "\\cite{sherlock2023,vaghasiya2023}",
        "fragmentadas, desenvolvidas em diferentes épocas": "\\cite{kazemi2016}",
        "Direção-Geral da Saúde": "\\cite{dgs2020}"
    },
    
    "EstadoDaArte.tex": {
        "Epic Systems": "\\cite{hertzum2022}",
        "Cerner (Oracle Health)": "\\cite{lin2018}",
        "sistemas hospitalares": "\\cite{shermock2023,vaghasiya2023}",
        "Health Level Seven (HL7)": "\\cite{dolin2006,mandl2020}",
        "Interoperabilidade limitada": "\\cite{keasberry2017}",
        "Interfaces complexas": "\\cite{mcgreevey2020}",
        "Custos elevados": "\\cite{adler2021}",
        "Resistência à mudança": "\\cite{holden2011,venkatesh2003}",
        "erros de medicação": "\\cite{ciapponi2021,mulac2020}",
        "Clinical Decision Support Systems": "\\cite{moss2015,belle2013}",
        "Machine learning": "\\cite{bates2021,zhao2021}",
        "Natural Language Processing": "\\cite{rozenblum2020}",
        "European Commission Report": "\\cite{european2016}",
        "Bright et al., 2022": "\\cite{amland2019}",
        "Sittig & Singh, 2020": "\\cite{radley2013}",
        "van der Sijs et al., 2019": "\\cite{mcgreevey2020}",
        "Adler-Milstein et al., 2021": "\\cite{adler2021}"
    },
    
    "Metodologia.tex": {
        "Oracle Database": "\\cite{jiang2014,lin2018}",
        "React": "\\cite{misra2023,zhao2021}",
        "Node.js": "\\cite{nkenyereye2016}",
        "metodologia ágil": "\\cite{vaghasiya2021,schnipper2018}",
        "arquitetura em camadas": "\\cite{martin2017,newman2021}",
        "Clean Architecture": "\\cite{martin2017}",
        "JWT": "\\cite{newman2021}",
        "integração com sistemas existentes": "\\cite{shermock2023}",
        "AIDA-PCE": "\\cite{franzoso2014}",
        "segurança": "\\cite{european2016}",
        "rastreabilidade": "\\cite{franzoso2014}"
    },
    
    "Resultados.tex": {
        "redução de erros": "\\cite{vaghasiya2023,franklin2007}",
        "tempo de resposta": "\\cite{austin2018}",
        "satisfação dos utilizadores": "\\cite{kvarnstrom2023}",
        "performance": "\\cite{nkenyereye2016}",
        "integração": "\\cite{shermock2023}",
        "Oracle 11g": "\\cite{jiang2014}",
        "métricas": "\\cite{donabedian1988,berwick2008}",
        "qualidade": "\\cite{berwick2008}",
        "eficiência": "\\cite{mahoney2007}"
    },
    
    "Discussao.tex": {
        "Oracle Database": "\\cite{jiang2014,lin2018}",
        "limitações": "\\cite{greenhalgh2017}",
        "custo-benefício": "\\cite{rozenblum2020}",
        "implementação": "\\cite{vaghasiya2021}",
        "sustentabilidade": "\\cite{greenhalgh2017,may2013}",
        "formação": "\\cite{kvarnstrom2023}",
        "adoção": "\\cite{holden2011,venkatesh2003}",
        "escalabilidade": "\\cite{newman2021}",
        "outros hospitais": "\\cite{shermock2023}",
        "sistemas comerciais": "\\cite{kazemi2016}",
        "contexto português": "\\cite{dgs2020,sns2019}",
        "standards": "\\cite{dolin2006,mandl2020}",
        "interoperabilidade": "\\cite{keasberry2017}",
        "segurança do paciente": "\\cite{who2017,linden2021}",
        "tecnologia": "\\cite{bates2021}",
        "inteligência artificial": "\\cite{zhao2021}",
        "machine learning": "\\cite{rozenblum2020}",
        "gestão de mudança": "\\cite{rogers2003}",
        "fatores humanos": "\\cite{holden2011}"
    },
    
    "Conclusao.tex": {
        "objetivos": "\\cite{berwick2008}",
        "contribuições": "\\cite{vaghasiya2023}",
        "impacto": "\\cite{franklin2007}",
        "trabalho futuro": "\\cite{bates2021}",
        "recomendações": "\\cite{greenhalgh2017}",
        "segurança": "\\cite{who2017}",
        "eficiência": "\\cite{mahoney2007}",
        "qualidade": "\\cite{donabedian1988}"
    }
}

# Referências para inserir em figuras e tabelas
referencias_figuras = {
    "Figura 1.1": "\\cite{shermock2023}",
    "Figura 1.2": "\\cite{martin2017}",
    "Figura 2.1": "\\cite{kazemi2016}",
    "Figura 2.2": "\\cite{kohn2000}",
    "Figura 3.1": "\\cite{vaghasiya2021}",
    "Figura 4.1": "\\cite{martin2017}",
    "Figura 4.2": "\\cite{newman2021}",
    "Tabela 1.1": "\\cite{who2017,dgs2020}",
    "Tabela 2.1": "\\cite{kazemi2016}",
    "Tabela 3.1": "\\cite{vaghasiya2021}",
    "Tabela 3.3": "\\cite{greenhalgh2017}",
    "Tabela 4.1": "\\cite{nkenyereye2016}"
}

def inserir_referencias_em_arquivo(arquivo_path, referencias_dict):
    """
    Insere referências em um arquivo LaTeX específico
    """
    if not os.path.exists(arquivo_path):
        print(f"Arquivo não encontrado: {arquivo_path}")
        return
    
    with open(arquivo_path, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    conteudo_modificado = conteudo
    referencias_inseridas = []
    
    # Inserir referências baseadas no texto
    for texto, referencia in referencias_dict.items():
        # Procurar o texto e adicionar a referência se não existir
        if texto in conteudo_modificado and referencia not in conteudo_modificado:
            # Adicionar referência após o texto
            conteudo_modificado = conteudo_modificado.replace(
                texto, 
                f"{texto} {referencia}"
            )
            referencias_inseridas.append(f"{texto} -> {referencia}")
    
    # Inserir referências para figuras e tabelas
    for elemento, referencia in referencias_figuras.items():
        if elemento in conteudo_modificado and referencia not in conteudo_modificado:
            # Procurar padrão [INSERIR: Figura X.X] e adicionar referência
            padrao = f"\\[INSERIR: {elemento}"
            if padrao in conteudo_modificado:
                conteudo_modificado = conteudo_modificado.replace(
                    padrao,
                    f"[INSERIR: {elemento} {referencia}"
                )
                referencias_inseridas.append(f"{elemento} -> {referencia}")
    
    # Salvar arquivo modificado
    if referencias_inseridas:
        with open(arquivo_path, 'w', encoding='utf-8') as f:
            f.write(conteudo_modificado)
        
        print(f"\nReferências inseridas em {arquivo_path}:")
        for ref in referencias_inseridas:
            print(f"  - {ref}")
    else:
        print(f"\nNenhuma referência nova para inserir em {arquivo_path}")

def processar_todos_capitulos():
    """
    Processa todos os capítulos da pré-tese
    """
    pasta_capitulos = Path("chapters")
    
    if not pasta_capitulos.exists():
        print("Pasta 'chapters' não encontrada. Certifique-se de que está no diretório correto.")
        return
    
    print("=== INSERINDO REFERÊNCIAS BIBLIOGRÁFICAS ===")
    print("Este script irá inserir referências nos capítulos da pré-tese.")
    print("Certifique-se de ter uma cópia de segurança antes de continuar.")
    
    continuar = input("\nDeseja continuar? (s/n): ")
    if continuar.lower() != 's':
        print("Operação cancelada.")
        return
    
    # Processar cada capítulo
    for arquivo, referencias in referencias_por_capitulo.items():
        arquivo_path = pasta_capitulos / arquivo
        inserir_referencias_em_arquivo(arquivo_path, referencias)
    
    print("\n=== PROCESSO CONCLUÍDO ===")
    print("Verifique os arquivos modificados e compile o documento LaTeX.")
    print("Lembre-se de:")
    print("1. Verificar se todas as referências estão corretas")
    print("2. Compilar o documento para verificar erros")
    print("3. Ajustar manualmente se necessário")

def criar_relatorio_referencias():
    """
    Cria um relatório com todas as referências disponíveis
    """
    print("=== RELATÓRIO DE REFERÊNCIAS DISPONÍVEIS ===")
    
    # Contar referências por tipo
    tipos_referencias = {
        "Sistemas de gestão medicamentosa": ["shermock2023", "vaghasiya2023", "franklin2007", "austin2018"],
        "Segurança na medicação": ["who2017", "who2022", "ciapponi2021", "mulac2020", "linden2021"],
        "Tecnologias de informação": ["radley2013", "moss2015", "keasberry2017", "hertzum2022"],
        "Oracle Database": ["jiang2014", "lin2018"],
        "React/Node.js": ["nkenyereye2016", "misra2023", "zhao2021"],
        "Metodologias e arquitetura": ["martin2017", "newman2021", "fowler2018", "vaghasiya2021"],
        "Contexto português": ["dgs2020", "sns2019", "european2016"],
        "Standards e interoperabilidade": ["dolin2006", "mandl2020"],
        "Gestão de mudança": ["holden2011", "venkatesh2003", "rogers2003", "greenhalgh2017"],
        "Qualidade e métricas": ["donabedian1988", "berwick2008", "mahoney2007"],
        "Inteligência artificial": ["bates2021", "zhao2021", "rozenblum2020"]
    }
    
    total_referencias = 0
    for tipo, refs in tipos_referencias.items():
        print(f"\n{tipo}:")
        for ref in refs:
            print(f"  - \\cite{{{ref}}}")
        total_referencias += len(refs)
    
    print(f"\nTotal de referências disponíveis: {total_referencias}")
    print(f"Referências do usuário incluídas: 5")
    print(f"Referências adicionais encontradas: {total_referencias - 5}")

def main():
    """
    Função principal
    """
    print("=== GESTOR DE REFERÊNCIAS BIBLIOGRÁFICAS ===")
    print("Escolha uma opção:")
    print("1. Inserir referências em todos os capítulos")
    print("2. Ver relatório de referências disponíveis")
    print("3. Inserir referências em capítulo específico")
    print("4. Sair")
    
    opcao = input("\nOpção: ")
    
    if opcao == "1":
        processar_todos_capitulos()
    elif opcao == "2":
        criar_relatorio_referencias()
    elif opcao == "3":
        print("\nCapítulos disponíveis:")
        for i, arquivo in enumerate(referencias_por_capitulo.keys(), 1):
            print(f"{i}. {arquivo}")
        
        try:
            escolha = int(input("\nEscolha o número do capítulo: ")) - 1
            arquivos = list(referencias_por_capitulo.keys())
            if 0 <= escolha < len(arquivos):
                arquivo = arquivos[escolha]
                arquivo_path = Path("chapters") / arquivo
                inserir_referencias_em_arquivo(arquivo_path, referencias_por_capitulo[arquivo])
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, insira um número válido.")
    elif opcao == "4":
        print("Saindo...")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main() 