# -*- coding: utf-8 -*-

informe_temp_atual = float(input("informe a temperatura atual: "))

if (informe_temp_atual > 0) and (informe_temp_atual <= 15):
	print ("Muito frio")
elif (informe_temp_atual >= 16) and (informe_temp_atual <= 23):
	print ("Frio")
elif (informe_temp_atual >= 24) and (informe_temp_atual <= 26):
	print ("Agradavel")
elif (informe_temp_atual >= 27) and (informe_temp_atual <= 30):
	print ("Calor")
elif (informe_temp_atual >= 31):
	print ("Muito Quente")
