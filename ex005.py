# -*- coding: utf-8 -*-

# Joãozinho, um piscicultor, deseja aumentar sua produção e para isso precisa
# recorrer a um empréstimo. Um Banco concederá crédito aos seus clientes de
#acordo com a produção do ano anterior. Faça um algoritmo que leia o valor
# da produção e calcule e imprima o valor do crédito de acordo com a tabela
# abaixo.
#
# Produção                                 valor
# Até R$ 120.000,00                        25%
# de R$ 120.000,01 até 500.000,00          30%
# A partir de R$ 500.000,01                45%

informe_producao = (float(input("informe o valor de produção: ")))

if informe_producao >= 0 or informe_producao <= 120000:
  opcao_1 = informe_producao * 25/100
  print ("o valor de credito e R$: ", opcao_1)

elif informe_producao >= 1200001 or informe_producao <= 500000:
  opcao_2 = informe_producao * 30/100
  print ("o valor de credito e R$: ", opcao_2)

else:
  opcao_3 = informe_producao * 45/100
  print ("o valor de credito e R$: ", opcao_3)
