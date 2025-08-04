# Configuração do Repositório GitHub

## Passos para criar o repositório no GitHub

### 1. Criar o repositório no GitHub
1. Acesse [github.com](https://github.com)
2. Clique em "New repository" ou "Novo repositório"
3. Configure o repositório:
   - **Nome**: `calculadora-completa-python`
   - **Descrição**: `Calculadora científica completa desenvolvida em Python com interface gráfica usando tkinter`
   - **Visibilidade**: Public
   - **NÃO** inicialize com README (já temos um)
4. Clique em "Create repository"

### 2. Inicializar o repositório local
```bash
# Inicializar git no diretório do projeto
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Initial commit: Calculadora completa em Python"

# Adicionar o repositório remoto (substitua SEU_USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU_USUARIO/calculadora-completa-python.git

# Fazer push para o GitHub
git branch -M main
git push -u origin main
```

### 3. Estrutura do projeto
```
calculadora-completa-python/
├── calculadora.py      # Código principal da calculadora
├── README.md           # Documentação do projeto
├── requirements.txt    # Dependências (opcional)
├── .gitignore         # Arquivos a serem ignorados
├── LICENSE            # Licença MIT
└── GITHUB_SETUP.md   # Este arquivo
```

### 4. Funcionalidades da Calculadora
- ✅ Operações básicas (+, -, ×, ÷)
- ✅ Funções trigonométricas (sin, cos, tan)
- ✅ Funções logarítmicas (log, ln)
- ✅ Operações avançadas (√, x², 1/x, !, |x|)
- ✅ Constantes matemáticas (π, e)
- ✅ Interface gráfica moderna
- ✅ Tratamento de erros

### 5. Como executar
```bash
python calculadora.py
```

### 6. Requisitos
- Python 3.x
- tkinter (incluído no Python)
- math (biblioteca padrão)

## Próximos passos após criar o repositório

1. **Adicionar badges** no README.md:
   - Status do build
   - Versão do Python
   - Licença

2. **Criar releases** para versões estáveis

3. **Adicionar issues templates** para bugs e features

4. **Configurar GitHub Actions** para CI/CD (opcional)

5. **Adicionar screenshots** da interface no README

## Contribuição

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Faça as alterações
4. Abra um Pull Request

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes. 