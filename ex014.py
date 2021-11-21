# -*- coding: utf-8 -*-

velocidade_max_permitida = float(input("informe velocidade maxima permitida em uma avenida: "))
velocidade_joao_dirigindo = float(input("informe a velocidade com que joao estava dirigindo: "))

multa = velocidade_max_permitida - velocidade_joao_dirigindo

if (multa == 10):
    print ("multa de 50 reais")

elif (multa > 11) and (multa <= 30):
    print ("multa de 100 reias")

elif (multa > 31):
    print ("multa de 200 reias")

else:
    print ("não recebera multa")
