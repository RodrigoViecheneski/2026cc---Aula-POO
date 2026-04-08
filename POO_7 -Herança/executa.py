from funcionario import Funcionario
from gerente import Gerente

gerente = Gerente('Iverton',
                  '763426437436',
                  'gerente',
                  30000.00,
                  '1234',
                  5
                  )
#print(gerente.get_bonificacao())
#print(vars(gerente))
#gerente.autentica('1234')

funcionario = Funcionario('Bruno', '738747743', 'Analista', 3000.00)
print(funcionario.get_bonificacao())
print(vars(funcionario))