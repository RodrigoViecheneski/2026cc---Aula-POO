class Funcionario:
    def __init__(self, nome, cpf, cargo, salario):
        self._nome = nome
        self._cpf = cpf
        self._cargo = cargo
        self._salario = salario

    def get_bonificacao(self):
        acrescimo = self._salario * 0.10
        self.salarioAtualizado = self._salario + acrescimo