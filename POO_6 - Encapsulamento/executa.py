from conta import Conta

conta1 = Conta(200.00)
conta2 = Conta(500.00)
conta3 = Conta(-200.00)

#print(conta1.saldo)
print(conta1.get_saldo())
print(conta2.get_saldo())
print(conta3.get_saldo())

conta3.set_saldo(conta1.get_saldo() + conta2.get_saldo())
print(conta3.get_saldo())