# Calculadora Completa em Python

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://www.python.org/)

Uma calculadora científica avançada desenvolvida em Python usando tkinter com interface gráfica moderna e funcionalidades matemáticas completas.

## 🚀 Funcionalidades

### 🔢 Operações Básicas
- **Adição (+)**: Soma dois números
- **Subtração (-)**: Subtrai dois números
- **Multiplicação (×)**: Multiplica dois números
- **Divisão (÷)**: Divide dois números
- **Potenciação (^)**: Eleva um número à potência de outro
- **Módulo (mod)**: Retorna o resto da divisão

### ⚡ Operações Avançadas
- **Raiz quadrada (√)**: Calcula a raiz quadrada de um número
- **Quadrado (x²)**: Eleva um número ao quadrado
- **Recíproco (1/x)**: Calcula o inverso de um número
- **Valor absoluto (|x|)**: Retorna o valor absoluto de um número
- **Fatorial (!)**: Calcula o fatorial de um número inteiro

### 📐 Funções Trigonométricas
- **Seno (sin)**: Calcula o seno de um ângulo em graus
- **Cosseno (cos)**: Calcula o cosseno de um ângulo em graus
- **Tangente (tan)**: Calcula a tangente de um ângulo em graus

### 📊 Funções Logarítmicas
- **Logaritmo decimal (log)**: Calcula o logaritmo na base 10
- **Logaritmo natural (ln)**: Calcula o logaritmo natural (base e)

### 🧮 Constantes Matemáticas
- **π (pi)**: Valor de pi (3.14159...)
- **e**: Número de Euler (2.71828...)

### 🎛️ Funções de Controle
- **C**: Limpa a calculadora
- **⌫**: Apaga o último dígito
- **±**: Troca o sinal do número
- **=**: Executa a operação
- **()**: Parênteses para expressões (implementação básica)

## 🚀 Como Executar

1. Certifique-se de ter Python instalado no seu sistema
2. O tkinter já vem incluído com a instalação padrão do Python
3. Execute o arquivo:

```bash
python calculadora.py
```

## 🖥️ Interface

A calculadora possui uma interface intuitiva com:
- Display grande para mostrar números e resultados
- Botões organizados em grid para fácil acesso
- Layout responsivo e moderno
- Tratamento de erros para operações inválidas

## ⚠️ Tratamento de Erros

A calculadora inclui tratamento para:
- Divisão por zero
- Raiz quadrada de números negativos
- Logaritmo de números não positivos
- Fatorial de números negativos ou não inteiros
- Entradas inválidas

## 💡 Exemplos de Uso

1. **Operação básica**: Digite `5 + 3 =` para obter `8`
2. **Potenciação**: Digite `2 ^ 3 =` para obter `8`
3. **Função trigonométrica**: Digite `30` e clique em `sin` para obter o seno de 30°
4. **Constante**: Clique em `π` para inserir o valor de pi
5. **Fatorial**: Digite `5` e clique em `!` para obter `120`

## 📋 Requisitos

- Python 3.x
- tkinter (incluído na instalação padrão do Python)
- math (biblioteca padrão do Python)

## 🏗️ Estrutura do Código

O código está organizado em uma classe `Calculadora` com métodos para:
- `criar_interface()`: Configura a interface gráfica
- `clicar_botao()`: Processa cliques nos botões
- `calcular()`: Executa operações matemáticas
- `operacao_unaria()`: Processa funções de um argumento
- Métodos auxiliares para limpar, apagar, etc.

A calculadora está pronta para uso e pode ser facilmente expandida com novas funcionalidades!

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- Python Software Foundation
- Tkinter developers
- Comunidade Python

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório! 