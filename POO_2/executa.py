from conta import Conta
# c1 é um atributo de referencia para o objeto.
c1 = Conta('123-4', 'Rodrigo', 120.0, 1000.0)
c2 = Conta('123-4', 'Rodrigo', 120.0, 1000.0 )
print(c2.saldo)
c1.depositar(100.0)
print(c1.saldo)
c2.depositar(50.0)
print(c2.saldo)
print(c1.saldo)
if(c1 == c2):
    print("Contas iguais")
else:
    print("Contas diferentes")

