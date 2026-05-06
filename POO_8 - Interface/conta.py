class Conta:
    def __init__(self, titular, numero, saldo=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if valor >0:
            self.saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def detalhes(self):
        return f"Conta: {self.numero}\nTitular: {self.titular}\nSaldo: R$ {self.saldo:.2f}" 