from Cliente import Clientes
from Conta import Contas
c1 = Clientes("Guilherme", "(15)99722-5739")
conta1 = Contas(c1, c1,)
print(f"nome={conta1.titular} telefone:{conta1.telefone} saldo:{conta1.saldo}")
conta1.saldo = float(input("DIgite o valor do saldo:"))
print(f"nome={conta1.titular} telefone:{conta1.telefone} saldo:{conta1.saldo}")
conta1.deposito(float(input("Digite o valor do deposito: ")))
conta1.estrato()
conta1.saque(float(input("Digite o valor do saque: ")))
conta1.estrato()
