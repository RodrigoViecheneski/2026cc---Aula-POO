from imposto import Imposto

class FGTS(Imposto):
    def calcular(self, valor: float):
        return valor * 0.15