# -*- coding: utf-8 -*-

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
