from funcionario import Funcionario
from gerente import Gerente
from controleDeBonificacoes import ControleDeBonificacoes
#Polimorfismo é a capacidade de um objeto poder ser referenciado de várias formas

if __name__ == '__main__':
    funcionario = Funcionario('Maruan', '098878766', 'analista', 3000.00)
    print('Bonificação funcionário: {}'.format(funcionario.get_bonificacao()))

    gerente = Gerente('Iverton', '887383788', 'Administrativo', 9000.00, '1234', 0)
    print('Bonificação gerente: {}'.format(gerente.get_bonificacao()))

    controle = ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)

    print("Total: {}".format(controle.total_bonificacoes))

    #Testes de execução