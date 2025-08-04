#!/usr/bin/env python3
"""
Script para configurar automaticamente o repositório Git e fazer upload para GitHub
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Executa um comando e mostra o resultado"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Sucesso!")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ {description} - Erro!")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Erro ao executar: {e}")
        return False
    return True

def check_git_installed():
    """Verifica se o Git está instalado"""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def main():
    print("🚀 Configurando repositório Git para Calculadora Python")
    print("=" * 60)
    
    # Verificar se Git está instalado
    if not check_git_installed():
        print("❌ Git não está instalado. Por favor, instale o Git primeiro.")
        print("📥 Download: https://git-scm.com/downloads")
        return
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("calculadora.py"):
        print("❌ Arquivo calculadora.py não encontrado!")
        print("💡 Certifique-se de estar no diretório do projeto.")
        return
    
    # Inicializar Git
    if not run_command("git init", "Inicializando repositório Git"):
        return
    
    # Adicionar arquivos
    if not run_command("git add .", "Adicionando arquivos ao Git"):
        return
    
    # Fazer primeiro commit
    if not run_command('git commit -m "Initial commit: Calculadora completa em Python"', 
                      "Fazendo primeiro commit"):
        return
    
    # Configurar branch main
    if not run_command("git branch -M main", "Configurando branch main"):
        return
    
    print("\n🎉 Repositório Git configurado com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Crie um repositório no GitHub:")
    print("   - Acesse: https://github.com/new")
    print("   - Nome: calculadora-completa-python")
    print("   - Descrição: Calculadora científica completa desenvolvida em Python")
    print("   - Visibilidade: Public")
    print("   - NÃO inicialize com README (já temos um)")
    print("\n2. Conecte o repositório local ao GitHub:")
    print("   git remote add origin https://github.com/SEU_USUARIO/calculadora-completa-python.git")
    print("   git push -u origin main")
    print("\n3. Substitua 'SEU_USUARIO' pelo seu username do GitHub")
    
    # Perguntar se quer configurar o remote
    print("\n" + "=" * 60)
    username = input("🔗 Digite seu username do GitHub (ou pressione Enter para pular): ").strip()
    
    if username:
        remote_url = f"https://github.com/{username}/calculadora-completa-python.git"
        if run_command(f"git remote add origin {remote_url}", "Adicionando remote origin"):
            print(f"\n✅ Remote configurado: {remote_url}")
            print("\n💡 Agora você pode fazer push com: git push -u origin main")
        else:
            print("\n❌ Erro ao configurar remote. Configure manualmente.")
    else:
        print("\n⏭️ Pulando configuração do remote. Configure manualmente quando criar o repositório.")

if __name__ == "__main__":
    main() 