from historico import Historico
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

   #métodos SET e GET aplicam o encapsulamento no python
    @property # Decorator transforma um método em atrivuto(encapsulamento elegante e seguro)
    def saldo(self):
        return self._saldo
    
    @saldo.setter # controla a modificação, possibilita validação antes de alterar o valor, sintaxe limpa
    def saldo(self, saldo):
        if(saldo >= 0):
            self._saldo += saldo
        else:
             print("Saldo não pode ser negativo!")

# Matheus, Iverton, Maruan, Otavio, Isaque