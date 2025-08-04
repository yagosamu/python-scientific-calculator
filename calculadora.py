import tkinter as tk
from tkinter import ttk
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Completa")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Variáveis
        self.valor_atual = tk.StringVar()
        self.valor_atual.set("0")
        self.operacao_anterior = ""
        self.valor_anterior = 0
        self.novo_numero = True
        
        # Configurar estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        self.criar_interface()
    
    def criar_interface(self):
        # Display
        display_frame = ttk.Frame(self.root)
        display_frame.pack(fill='x', padx=10, pady=10)
        
        self.display = ttk.Entry(display_frame, textvariable=self.valor_atual, 
                                font=('Arial', 20), justify='right', state='readonly')
        self.display.pack(fill='x')
        
        # Botões
        botoes_frame = ttk.Frame(self.root)
        botoes_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Configurar grid
        for i in range(8):
            botoes_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            botoes_frame.grid_columnconfigure(i, weight=1)
        
        # Botões especiais
        botoes_especiais = [
            ('C', 0, 0, 1, 2), ('⌫', 0, 2, 1, 1), ('±', 0, 3, 1, 1), ('÷', 0, 4, 1, 1),
            ('√', 1, 0, 1, 1), ('x²', 1, 1, 1, 1), ('1/x', 1, 2, 1, 1), ('×', 1, 3, 1, 1), ('%', 1, 4, 1, 1),
            ('sin', 2, 0, 1, 1), ('cos', 2, 1, 1, 1), ('tan', 2, 2, 1, 1), ('-', 2, 3, 1, 1), ('log', 2, 4, 1, 1),
            ('7', 3, 0, 1, 1), ('8', 3, 1, 1, 1), ('9', 3, 2, 1, 1), ('+', 3, 3, 1, 1), ('ln', 3, 4, 1, 1),
            ('4', 4, 0, 1, 1), ('5', 4, 1, 1, 1), ('6', 4, 2, 1, 1), ('=', 4, 3, 1, 1), ('π', 4, 4, 1, 1),
            ('1', 5, 0, 1, 1), ('2', 5, 1, 1, 1), ('3', 5, 2, 1, 1), ('e', 5, 4, 1, 1),
            ('0', 6, 0, 1, 2), ('.', 6, 2, 1, 1), ('!', 6, 4, 1, 1),
            ('(', 7, 0, 1, 1), (')', 7, 1, 1, 1), ('^', 7, 2, 1, 1), ('mod', 7, 3, 1, 1), ('|x|', 7, 4, 1, 1)
        ]
        
        for (texto, row, col, rowspan, colspan) in botoes_especiais:
            btn = ttk.Button(botoes_frame, text=texto, command=lambda t=texto: self.clicar_botao(t))
            btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=2, pady=2, sticky='nsew')
    
    def clicar_botao(self, valor):
        if valor.isdigit() or valor == '.':
            self.adicionar_digito(valor)
        elif valor in ['+', '-', '×', '÷', '^', 'mod']:
            self.definir_operacao(valor)
        elif valor == '=':
            self.calcular()
        elif valor == 'C':
            self.limpar()
        elif valor == '⌫':
            self.apagar()
        elif valor == '±':
            self.trocar_sinal()
        elif valor in ['√', 'x²', '1/x', 'sin', 'cos', 'tan', 'log', 'ln', '!', '|x|']:
            self.operacao_unaria(valor)
        elif valor in ['π', 'e']:
            self.adicionar_constante(valor)
        elif valor in ['(', ')']:
            self.adicionar_parenteses(valor)
    
    def adicionar_digito(self, digito):
        if self.novo_numero:
            self.valor_atual.set(digito)
            self.novo_numero = False
        else:
            if digito == '.' and '.' in self.valor_atual.get():
                return
            self.valor_atual.set(self.valor_atual.get() + digito)
    
    def definir_operacao(self, operacao):
        try:
            valor = float(self.valor_atual.get())
            if self.operacao_anterior and not self.novo_numero:
                self.calcular()
            self.valor_anterior = valor
            self.operacao_anterior = operacao
            self.novo_numero = True
        except ValueError:
            pass
    
    def calcular(self):
        try:
            valor_atual = float(self.valor_atual.get())
            if self.operacao_anterior == '+':
                resultado = self.valor_anterior + valor_atual
            elif self.operacao_anterior == '-':
                resultado = self.valor_anterior - valor_atual
            elif self.operacao_anterior == '×':
                resultado = self.valor_anterior * valor_atual
            elif self.operacao_anterior == '÷':
                if valor_atual == 0:
                    self.valor_atual.set("Erro: Divisão por zero")
                    return
                resultado = self.valor_anterior / valor_atual
            elif self.operacao_anterior == '^':
                resultado = self.valor_anterior ** valor_atual
            elif self.operacao_anterior == 'mod':
                resultado = self.valor_anterior % valor_atual
            else:
                return
            
            self.valor_atual.set(str(resultado))
            self.operacao_anterior = ""
            self.novo_numero = True
        except ValueError:
            pass
    
    def operacao_unaria(self, operacao):
        try:
            valor = float(self.valor_atual.get())
            if operacao == '√':
                if valor < 0:
                    self.valor_atual.set("Erro: Raiz de número negativo")
                    return
                resultado = math.sqrt(valor)
            elif operacao == 'x²':
                resultado = valor ** 2
            elif operacao == '1/x':
                if valor == 0:
                    self.valor_atual.set("Erro: Divisão por zero")
                    return
                resultado = 1 / valor
            elif operacao == 'sin':
                resultado = math.sin(math.radians(valor))
            elif operacao == 'cos':
                resultado = math.cos(math.radians(valor))
            elif operacao == 'tan':
                resultado = math.tan(math.radians(valor))
            elif operacao == 'log':
                if valor <= 0:
                    self.valor_atual.set("Erro: Log de número não positivo")
                    return
                resultado = math.log10(valor)
            elif operacao == 'ln':
                if valor <= 0:
                    self.valor_atual.set("Erro: Ln de número não positivo")
                    return
                resultado = math.log(valor)
            elif operacao == '!':
                if valor < 0 or valor != int(valor):
                    self.valor_atual.set("Erro: Fatorial inválido")
                    return
                resultado = math.factorial(int(valor))
            elif operacao == '|x|':
                resultado = abs(valor)
            
            self.valor_atual.set(str(resultado))
            self.novo_numero = True
        except ValueError:
            pass
    
    def adicionar_constante(self, constante):
        if constante == 'π':
            self.valor_atual.set(str(math.pi))
        elif constante == 'e':
            self.valor_atual.set(str(math.e))
        self.novo_numero = True
    
    def adicionar_parenteses(self, parentese):
        # Implementação básica - pode ser expandida para expressões complexas
        if parentese == '(':
            self.valor_atual.set('(' + self.valor_atual.get())
        else:
            self.valor_atual.set(self.valor_atual.get() + ')')
        self.novo_numero = False
    
    def limpar(self):
        self.valor_atual.set("0")
        self.operacao_anterior = ""
        self.valor_anterior = 0
        self.novo_numero = True
    
    def apagar(self):
        valor_atual = self.valor_atual.get()
        if len(valor_atual) > 1:
            self.valor_atual.set(valor_atual[:-1])
        else:
            self.valor_atual.set("0")
            self.novo_numero = True
    
    def trocar_sinal(self):
        try:
            valor = float(self.valor_atual.get())
            self.valor_atual.set(str(-valor))
        except ValueError:
            pass

def main():
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main() 