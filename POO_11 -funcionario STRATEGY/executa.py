from funcionario import Funcionario
from impostoSalario import ImpostoSalario
from inss import INSS
from irrf import IRRF
from fgts import FGTS

funcionario = Funcionario('Maruan', 4000.00)
imposto_salario = ImpostoSalario()

print(funcionario.salario)
INSS = imposto_salario.calcular(funcionario.salario, INSS())
IRRF = imposto_salario.calcular(funcionario.salario, IRRF())
FGTS = imposto_salario.calcular(funcionario.salario, FGTS())

print(INSS)
print(IRRF)
print(FGTS)
print(funcionario.salario - (INSS + IRRF + FGTS))