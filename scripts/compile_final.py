#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para compilação final completa do documento
Limpa arquivos temporários e compila o documento final
"""

import os
import subprocess
import glob
import sys

def cleanup_temp_files():
    """Remove arquivos temporários de compilação"""
    temp_extensions = ['.aux', '.bbl', '.blg', '.log', '.out', '.toc', '.lof', '.lot', '.idx', '.glo', '.acn']
    
    print("🧹 Limpando arquivos temporários...")
    
    for ext in temp_extensions:
        files = glob.glob(f"pre-tese{ext}")
        for file in files:
            try:
                os.remove(file)
                print(f"   ✓ Removido: {file}")
            except FileNotFoundError:
                pass
    
    print("   ✓ Limpeza concluída!")

def run_command(cmd, description):
    """Executa um comando e retorna o resultado"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"   ⚠️  Warning: {description} completou com código {result.returncode}")
        else:
            print(f"   ✓ {description} bem-sucedido!")
        return result.returncode == 0
    except Exception as e:
        print(f"   ❌ Erro em {description}: {e}")
        return False

def compile_document():
    """Compila o documento XeLaTeX completo"""
    print("\n📄 Iniciando compilação completa...")
    
    # Primeira compilação
    if not run_command("xelatex -interaction=nonstopmode pre-tese.tex", "Primeira compilação XeLaTeX"):
        return False
    
    # Processamento de bibliografia
    if not run_command("bibtex pre-tese", "Processamento de bibliografia"):
        return False
    
    # Segunda compilação
    if not run_command("xelatex -interaction=nonstopmode pre-tese.tex", "Segunda compilação XeLaTeX"):
        return False
    
    # Terceira compilação (final)
    if not run_command("xelatex -interaction=nonstopmode pre-tese.tex", "Terceira compilação XeLaTeX"):
        return False
    
    return True

def check_output():
    """Verifica se o PDF foi gerado corretamente"""
    pdf_file = "pre-tese.pdf"
    if os.path.exists(pdf_file):
        size = os.path.getsize(pdf_file)
        print(f"\n📋 PDF gerado com sucesso!")
        print(f"   📄 Arquivo: {pdf_file}")
        print(f"   💾 Tamanho: {size:,} bytes ({size/1024/1024:.1f} MB)")
        
        # Contar páginas através do log
        log_file = "pre-tese.log"
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                log_content = f.read()
                if "Output written on" in log_content:
                    for line in log_content.split('\n'):
                        if "Output written on" in line and "pages" in line:
                            print(f"   📖 {line.strip()}")
                            break
        
        return True
    else:
        print(f"\n❌ PDF não foi gerado!")
        return False

def main():
    """Função principal"""
    print("🎯 COMPILAÇÃO FINAL DO DOCUMENTO")
    print("=" * 50)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("pre-tese.tex"):
        print("❌ Erro: Arquivo pre-tese.tex não encontrado!")
        print("   Execute este script no diretório raiz do projeto.")
        sys.exit(1)
    
    # Etapa 1: Limpeza
    cleanup_temp_files()
    
    # Etapa 2: Compilação
    if compile_document():
        print("\n🎉 COMPILAÇÃO CONCLUÍDA COM SUCESSO!")
        
        # Etapa 3: Verificação
        if check_output():
            print("\n✅ Documento pronto para submissão!")
            print("   O arquivo pre-tese.pdf foi gerado sem erros.")
        else:
            print("\n⚠️  Documento compilado mas com problemas no PDF.")
            sys.exit(1)
    else:
        print("\n❌ FALHA NA COMPILAÇÃO!")
        print("   Verifique os erros acima e tente novamente.")
        sys.exit(1)

if __name__ == "__main__":
    main() 