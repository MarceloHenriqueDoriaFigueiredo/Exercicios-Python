# -*- coding: utf-8 -*-

# Faça um algoritmo em Python para ler dois números inteiros e informar se,
# estes números são iguais ou diferentes.

numero_1 = (int(input("Digite o primeiro numero: ")))
numero_2 = (int(input("Digite o segundo numero: ")))

if numero_1 == numero_2:
  print("os numeros são iguais")
elif numero_2 == numero_1:
  print("os numeros são iguais")
else:
  print("os numeros são diferentes")
