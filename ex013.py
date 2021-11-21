# -*- coding: utf-8 -*-

# Joãozinho é um piscicultor em Propriá. Joãozinho precisa de um programa que receba 
# como entrada o preço de custo do peixe, o valor do imposto a ser pago e o percentual de lucro. 
#Portanto, faça um programa em Python que com base nos dados de entrada calcule o valor do peixe para Joãozinho.

custo_peixe = float(input("informe o valor do peixe: R$ "))
imposto_pago = float(input("informe o valor do imposto: R$ "))
perc_lucro = float(input("informe o percentual do lucro: "))
lucro_1 = perc_lucro * custo_peixe/ 100
valor_peixe = custo_peixe + imposto_pago + lucro_1
print ("o valor do peixe e R$", valor_peixe)
