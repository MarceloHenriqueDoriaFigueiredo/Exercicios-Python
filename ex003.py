# -*- coding: utf-8 -*-

# Faça um algoritmo em Python para ler duas variáveis inteiras A e B e garantir que A e B fiquem em ordem crescente, 
# ou seja, a variável A deverá armazenar o menor valor fornecido e a variável B o maior.

a = int(input("digite a primeira variavel: "))
b = int(input("digite a segunda variavel: "))
crescente = int(input("digite qualquer variavel: "))

if a < b:
  print(a,b)
else:
  crescente = b
  b = a
  a = crescente
  print (a,b)
