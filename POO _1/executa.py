from conta import Conta

conta = Conta('123-4', 'Rodrigo', 120.0, 1000.0)

#type(conta)
#print(conta.numero)
#print(conta.titular)
#print(conta.saldo)
#conta.depositar(50.0)
#print(conta.saldo)
#conta.sacar(100.0)
#conta.extrato()
print(conta.saldo)

consegui = conta.sacar(222)
if(consegui):
    print("Consegui sacar")
    print("Restam ainda: {}".format(conta.saldo))
else:
    print("Não consegui sacar")
    print("Tenho apenas: {}".format(conta.saldo))