from historico import Historico
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

   #métodos SET e GET aplicam o encapsulamento no python
    def get_saldo(self):
        return self._saldo
    