from conta import Conta
from cliente import Cliente
t1 = Cliente('Rodrigo', 'Viecheneski', '9883336649')
t2 = Cliente('Raphael', 'Boamorte', '11111111111')
# c1 é um atributo de referencia para o objeto.
c1 = Conta('123-4', t1, 120.0, 1000.0)
c2 = Conta('1-4', t2, 120.0, 1000.0 )

print(c1.titular.nome)
print(c2.titular.nome)

print(c1.titular.sobrenome)
print(c2.titular.cpf)

print(c1.__dict__)
print(c1.titular.__dict__)