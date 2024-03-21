from decimal import Decimal
from math import sqrt


class Barra:
    def __init__(
        self, comprimento, n_fios, peso, nome, esforco_interno, tipo_de_esforco
    ):
        self.comprimento = None
        self.n_fios = None
        self.peso = None
        self.nome = None
        self.esforco_interno = None
        self.tipo_de_esforco = None

    def inserir_atributosBarra(self):
        self.comprimento = Decimal(input("insira o comprimento da barra"))
        self.n_fios = Decimal(input("insira o numero de fios da barra"))
        self.peso = Decimal(input("insira o peso da barra"))
        self.nome = input("insira o nome da barra")
        self.tipo_de_esforco("insira o tipo de esforco da barra")

    def mostrar_atributosBarra(self):
        print("comprimento: ", self.comprimento)
        print("n_fios: ", self.n_fios)
        print("peso: ", self.peso)
        print("nome: ", self.nome)
        print("esforco_interno: ", self.esforco_interno)
        print("tipo_de_esforco: ", self.tipo_de_esforco)

    def calcular_fio(self):
        self.esforco_interno = Decimal(input("insira o esforço interno da barra"))
        if self.tipo_de_esforco == "C":
            resultadoc = sqrt(
                (self.esforco_interno * self.comprimento**2) / 27906 * 1**4
            )
            print("o numero de fios necessarios é: ", resultadoc)
            self.n_fios = resultadoc
        elif self.tipo_de_esforco == "T":
            resultadot = self.esforco_interno / Decimal(42.67)
            print("o numero de fios necessarios é: ", resultadot)
            self.n_fios = resultadot
        else:
            print("tipo invalido")

    def calcular_peso(self):
        self.peso = self.n_fios * Fio.inserir_atributos(self.peso)
        print("o peso da barra é: ", self.peso)
