import os

os.system('cls' if os.name == 'nt' else 'clear')

# Classe para o Fluxo de Caixa Mensal
class FluxoDeCaixaMensal:
    def __init__(self, salario):
        self.salario = salario
        self.aluguel = 0.0
        self.luz = 0.0
        self.fornecedor = 0.0
        self.outras_despesas = 0.0
        self.receitas = 0.0
        self.saldo = 0.0

    def adicionar_receita(self, valor):
        self.receitas += valor
        self.saldo += valor

    def adicionar_despesa(self, tipo, valor):
        if tipo == "aluguel":
            self.aluguel += valor
        elif tipo == "luz":
            self.luz += valor
        elif tipo == "fornecedor":
            self.fornecedor += valor
        else:
            self.outras_despesas += valor
        self.saldo -= valor

    def calcular_despesas_totais(self):
        return self.aluguel + self.luz + self.fornecedor + self.outras_despesas

    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def mostrar_despesas(self):
        print("\nDespesas Detalhadas:")
        print(f"Aluguel: R$ {self.aluguel:.2f}")
        print(f"Luz: R$ {self.luz:.2f}")
        print(f"Fornecedor: R$ {self.fornecedor:.2f}")
        print(f"Outras Despesas: R$ {self.outras_despesas:.2f}")
        print(f"Despesas Totais: R$ {self.calcular_despesas_totais():.2f}")

    def mostrar_receitas(self):
        print(f"Total de Receitas: R$ {self.receitas:.2f}")

    def resumo(self):
        self.mostrar_receitas()
        self.mostrar_despesas()
        self.mostrar_saldo()

    def previsto(self):
        return self.salario - self.calcular_despesas_totais() if self.calcular_despesas_totais() <= self.salario else 0.0000000000000001
    
    def realizado(self):
        return self.receitas - self.calcular_despesas_totais()

# Função para coletar dados de um mês específico
def coletar_dados_mes(mes, salario):
    print(f"\n--- Mês {mes} ---")
    aluguel = float(input('Digite o valor do aluguel: '))
    luz = float(input('Digite o valor da luz: '))
    fornecedor = float(input('Digite o valor do fornecedor: '))
    outras = float(input('Outras despesas: '))
    
    fluxo = FluxoDeCaixaMensal(salario)
    fluxo.adicionar_receita(salario)
    fluxo.adicionar_despesa("aluguel", aluguel)
    fluxo.adicionar_despesa("luz", luz)
    fluxo.adicionar_despesa("fornecedor", fornecedor)
    fluxo.adicionar_despesa("outras", outras)
    
    return fluxo

# Configurações iniciais
Salario_User = 3000.00 # Salário do usuário
fluxos_mensais = []

# Coletar dados para 4 meses
for mes in range(1, 5):
    fluxo = coletar_dados_mes(mes, Salario_User)
    fluxos_mensais.append(fluxo)

# Mostrar resumo dos 4 meses
for i, fluxo in enumerate(fluxos_mensais, start=1):
    print(f"\nResumo do Mês {i}:")
    fluxo.resumo()
    print(f'Previsto: R$ {fluxo.previsto():.2f}')
    print(f'Realizado: R$ {fluxo.realizado():.2f}')
    print('------------------------------------------')

# Mostrar resumo geral dos 4 meses
saldo_total = sum(fluxo.saldo for fluxo in fluxos_mensais)
despesas_totais = sum(fluxo.calcular_despesas_totais() for fluxo in fluxos_mensais)
receitas_totais = sum(fluxo.receitas for fluxo in fluxos_mensais)

print("\nResumo Geral dos 4 Meses:")
print(f"Receitas Totais: R$ {receitas_totais:.2f}")
print(f"Despesas Totais: R$ {despesas_totais:.2f}")
print(f"Saldo Final: R$ {saldo_total:.2f}")