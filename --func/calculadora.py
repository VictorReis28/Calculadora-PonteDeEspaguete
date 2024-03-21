from decimal import Decimal
from math import sqrt

esforco_interno = Decimal(input("Digite o esforço interno EM NEWTONS: "))
tipo = input("Digite o tipo de esforço (tração T ou compressão C): ")
comprimento = Decimal(input("Digite o comprimento da peça EM MILIMETROS: "))
resultadoc = sqrt((esforco_interno * comprimento**2) / 27906 * 1**4)
resultadot = esforco_interno / Decimal(42.67)

if tipo == "C":
    print("o numero de fios necessarios é: ", resultadoc)
elif tipo == "T":
    print("o numero de fios necessarios é: ", resultadot)
else:
    print("tipo invalido")
