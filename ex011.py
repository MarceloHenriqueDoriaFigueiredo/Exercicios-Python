# -*- coding: utf-8 -*-

numero = int(input("Informe um numero: "))
soma_par = 0
soma_impar = 0
for elemento in range(0,numero+1):
    #print(elemento)
    if elemento % 2 == 0:
        soma_par = soma_par + elemento
    else:
        soma_impar = soma_impar + elemento

print("a soma dos pares:", soma_par)
print("a soma dos impares:" , soma_impar)
