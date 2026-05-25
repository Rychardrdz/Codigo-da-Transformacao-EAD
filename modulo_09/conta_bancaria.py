class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, saque):
        self.message = f"Saldo insuficiente! Saldo: R${saldo}, Tentativa de saque: R${saque}"
        super().__init__(self.message)

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        print(f"Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}")

minha_conta = ContaBancaria(500)

try:
    minha_conta.sacar(600)
except SaldoInsuficienteError as e:
    print(f"Alerta do Sistema: {e}")