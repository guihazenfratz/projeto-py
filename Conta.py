class Contas:
    def __init__(self, titular, numero):
        self.titular = titular.nome
        self.numero = numero.telefone1
        self._saldo = 0.0

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado")
        else:
            print("Saldo insuficiente")

    def deposito(self, valor):
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
