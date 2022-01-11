# -*- coding: utf-8 -*-

lado_1 = (int(input("digite o primeiro lado: ")))
lado_2 = (int(input("digite o segundo lado: ")))
lado_3 = (int(input("digite o terceiro lado: ")))

if lado_1 == lado_2 and lado_1 == lado_3:
  print ("o triangulo e equilatero")
elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
  print ("o triangulo e isoceles")
elif lado_1 != lado_2 and lado_3 or lado_2 != lado1 and lado_3 or lado_1 != lado_3:
  print ("o triangulo e escaleno")
