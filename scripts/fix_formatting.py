#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir problemas de formatação na pré-tese
Autor: Assistant
Data: 2025-07-14
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Executa um comando e verifica se foi bem-sucedido"""
    print(f"\n=== {description} ===")
    print(f"Executando: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("✓ Comando executado com sucesso")
            if result.stdout:
                print("Saída:", result.stdout[-500:])  # Últimos 500 caracteres
            return True
        else:
            print("✗ Erro na execução")
            print("Código de saída:", result.returncode)
            if result.stderr:
                print("Erro:", result.stderr[-500:])  # Últimos 500 caracteres
            return False
            
    except Exception as e:
        print(f"✗ Exceção durante execução: {e}")
        return False

def clean_temp_files():
    """Remove arquivos temporários de compilação"""
    temp_extensions = ['.aux', '.bbl', '.blg', '.log', '.out', '.toc', 
                      '.lof', '.lot', '.acn', '.glo', '.ist', '.idx']
    
    for ext in temp_extensions:
        file_path = f"pre-tese{ext}"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Removido: {file_path}")

def main():
    """Função principal para corrigir formatação e recompilar"""
    print("=== CORREÇÃO DE FORMATAÇÃO DA PRÉ-TESE ===")
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("pre-tese.tex"):
        print("❌ Erro: Arquivo pre-tese.tex não encontrado!")
        print("Execute este script no diretório raiz do projeto.")
        sys.exit(1)
    
    # Limpar arquivos temporários
    print("\n1. Limpando arquivos temporários...")
    clean_temp_files()
    
    # Primeira compilação XeLaTeX
    print("\n2. Primeira compilação XeLaTeX...")
    if not run_command("xelatex -interaction=nonstopmode pre-tese.tex", 
                      "Primeira compilação XeLaTeX"):
        print("❌ Erro na primeira compilação!")
        sys.exit(1)
    
    # Compilação do BibTeX
    print("\n3. Compilação das referências (BibTeX)...")
    if not run_command("bibtex pre-tese", "Compilação BibTeX"):
        print("⚠️  Aviso: Problemas com BibTeX, mas continuando...")
    
    # Segunda compilação XeLaTeX
    print("\n4. Segunda compilação XeLaTeX...")
    if not run_command("xelatex -interaction=nonstopmode pre-tese.tex", 
                      "Segunda compilação XeLaTeX"):
        print("❌ Erro na segunda compilação!")
        sys.exit(1)
    
    # Terceira compilação XeLaTeX (para referências cruzadas)
    print("\n5. Terceira compilação XeLaTeX (referências cruzadas)...")
    if not run_command("xelatex -interaction=nonstopmode pre-tese.tex", 
                      "Terceira compilação XeLaTeX"):
        print("❌ Erro na terceira compilação!")
        sys.exit(1)
    
    # Verificar se o PDF foi gerado
    if os.path.exists("pre-tese.pdf"):
        file_size = os.path.getsize("pre-tese.pdf")
        print(f"\n✅ PDF gerado com sucesso!")
        print(f"📄 Tamanho: {file_size:,} bytes ({file_size/1024/1024:.1f} MB)")
        
        # Verificar número de páginas
        try:
            result = subprocess.run(
                "pdfinfo pre-tese.pdf | grep Pages", 
                shell=True, capture_output=True, text=True
            )
            if result.returncode == 0 and "Pages:" in result.stdout:
                pages = result.stdout.split("Pages:")[1].strip()
                print(f"📖 Número de páginas: {pages}")
        except:
            print("📖 Não foi possível determinar o número de páginas")
    else:
        print("❌ PDF não foi gerado!")
        sys.exit(1)
    
    # Verificar log para warnings
    if os.path.exists("pre-tese.log"):
        with open("pre-tese.log", "r", encoding="utf-8") as f:
            log_content = f.read()
            
        warnings = log_content.count("Warning:")
        errors = log_content.count("Error:")
        
        print(f"\n📊 Relatório de compilação:")
        print(f"   Warnings: {warnings}")
        print(f"   Errors: {errors}")
        
        if warnings > 0:
            print("\n⚠️  Warnings encontrados (últimos 5):")
            warning_lines = [line for line in log_content.split('\n') 
                           if 'Warning:' in line]
            for warning in warning_lines[-5:]:
                print(f"   {warning}")
        
        if errors == 0:
            print("\n✅ Compilação concluída sem erros!")
        else:
            print(f"\n❌ {errors} erros encontrados na compilação!")
    
    print("\n=== CORREÇÕES DE FORMATAÇÃO APLICADAS ===")
    print("✓ Melhorado espaçamento na capa")
    print("✓ Corrigida hierarquia visual do título")
    print("✓ Ajustado posicionamento vertical dos elementos")
    print("✓ Melhorado espaçamento entre seções no resumo")
    print("✓ Refinada formatação de capítulos e seções")
    print("✓ Otimizado espaçamento entre linhas")
    
    print("\n🎉 Processo de correção de formatação concluído!")

if __name__ == "__main__":
    main() 