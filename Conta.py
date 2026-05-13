class Contas:
    def __init__(self, titular, telefone):
        self.titular = titular.nome
        self.telefone = telefone.telefone
        self._saldo = 0.00

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado")
        else:
            print("Saldo insuficiente")

    def deposito(self, valor):
        if valor <= 0:
            print("Nao Pode depositar nada ou numeros negativos")


        self.saldo += valor

    def estrato(self):
        print(
            f"Titular da conta:{self.titular}  Saldo atualizado:{self.saldo}")

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Saldo nao pode ser negativo")
        else:
            self._saldo = valor
