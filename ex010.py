# -*- coding: utf-8 -*-

# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo 
# para calcular seu peso ideal, utilizando as seguintes fórmulas:
# para homens:72,7 * altura – 58; para mulheres:62,1 * altura – 44,7

altura = (float(input("informe a altura: ")))
sexo = (input("informe o sexo: "))

if (sexo == "masculino"):
  peso_ideal_m = (72.7 * altura) - 58
  print ("o peso ideal e: ", peso_ideal_m)

elif (sexo == "feminino"):
  peso_ideal_f = (62.1 * altura) - 44.7
  print ("o peso ideal e: ", peso_ideal_f)
