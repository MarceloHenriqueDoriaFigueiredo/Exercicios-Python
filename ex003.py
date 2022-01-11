# -*- coding: utf-8 -*-

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
