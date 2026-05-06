from funcionario import Funcionario
from impostoSalario import ImpostoSalario

funcionario = Funcionario('Jean', 10000.00)
imposto_salario = ImpostoSalario()

print(funcionario.salario)

INSS = imposto_salario.calcular(funcionario.salario, 'INSS')
print(INSS)
IRRF = imposto_salario.calcular(funcionario.salario, 'IRRF')
print(IRRF)

FGTS = imposto_salario.calcular(funcionario.salario, 'FGTS')
print(FGTS)

salarioLiquido = funcionario.salario - (FGTS + IRRF +INSS) 
print(salarioLiquido)