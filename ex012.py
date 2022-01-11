# -*- coding: utf-8 -*-

quant_paes = (int(input("informe a quantidade de paes vendidos no dia: ")))
quant_broas = (int(input("informe a quantidade de broas vendidas no dia: ")))

valor_total = (quant_paes * 0.12) + (quant_broas * 1.50)
poupanca = valor_total * 10/100

print ("foi arrecadado um total de RS: ", valor_total)
print ("ele deve guarda na poupanca: ", poupanca)
