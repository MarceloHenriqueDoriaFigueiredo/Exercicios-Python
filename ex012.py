# -*- coding: utf-8 -*-

# A padaria “Pão Bom” vende certa quantidade de pães franceses e uma quantidade de broas a cada dia. 
# Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou 
# com a venda dos pães e broas (juntos), e quanto' deve guardar numa conta de poupança (10% do total arrecadado). 
# Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, 
# faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.

quant_paes = (int(input("informe a quantidade de paes vendidos no dia: ")))
quant_broas = (int(input("informe a quantidade de broas vendidas no dia: ")))

valor_total = (quant_paes * 0.12) + (quant_broas * 1.50)
poupanca = valor_total * 10/100

print ("foi arrecadado um total de RS: ", valor_total)
print ("ele deve guarda na poupanca: ", poupanca)
