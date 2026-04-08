from conta import Conta

#conta1 = Conta(200.00)
#conta2 = Conta(500.00)
#conta3 = Conta(-200.00)

#conta1.saldo = -300.00

#print(conta1.saldo)

conta1 = Conta(-1000.00)
conta1.saldo += 300.00
print(conta1.saldo)
conta1.saldo += 5000.00
conta1.saldo = conta1.saldo + 5000.00
print(conta1.saldo)
