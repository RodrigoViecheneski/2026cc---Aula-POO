from historico import Historico
class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.transacoes.append("Deposito de {}".format(valor))

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de  {}".format(valor))
            return True
        return False

    def extrato(self):
        print("Numero: {} \nSaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("Tirou extrato - saldo de {}".format(self.saldo))

    def transfere(self, destino, valor):
        retirou = self.sacar(valor)
        if(retirou == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("Transferência de  {} para conta {}".format(valor, destino.numero))
            return True