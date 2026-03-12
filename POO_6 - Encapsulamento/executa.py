from conta import Conta
from cliente import Cliente
t1 = Cliente('Rodrigo', 'Viecheneski', '9883336649')
t2 = Cliente('Raphael', 'Boamorte', '11111111111')
# c1 é um atributo de referencia para o objeto.
c1 = Conta('123-4', t1, 120.0, 1000.0)
c2 = Conta('1-4', t2, 3000.0, 1000.0 )

#c1.depositar(1000.0)
#c1.extrato()
#c1.sacar(200.0)
#c1.extrato()
#c2.transfere(c1, 1500.0)
#c1.extrato()
#c2.extrato()
#c2.historico.imprime()

c2.saldo = 100000.00
c2.extrato()