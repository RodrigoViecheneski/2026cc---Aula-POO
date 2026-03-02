from conta import Conta
# c1 é um atributo de referencia para o objeto.
c1 = Conta('123-4', 'Rodrigo', 120.0, 1000.0)
c2 = Conta('1-4', 'Rodrigo', 120.0, 1000.0 )

print(c1.saldo)
print(c2.saldo)

c1.transfere(c2,100.0)
print(c1.saldo)
print(c2.saldo)
