# -*- coding: utf-8 -*-

# Faça um algoritmo em Python para ler três valores reais e informar se estes
# podem ou não formar os lados de um triângulo e qual tipo de triângulo seria:
# Equilátero, Isóscele ou Escaleno;

lado_1 = (int(input("digite o primeiro lado: ")))
lado_2 = (int(input("digite o segundo lado: ")))
lado_3 = (int(input("digite o terceiro lado: ")))

if lado_1 == lado_2 and lado_1 == lado_3:
  print ("o triangulo e equilatero")
elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
  print ("o triangulo e isoceles")
elif lado_1 != lado_2 and lado_3 or lado_2 != lado1 and lado_3 or lado_1 != lado_3:
  print ("o triangulo e escaleno")
