from decimal import Decimal
from math import sqrt


class Fio:
    def __init__(self, comprimento, peso):
        self.comprimento = comprimento
        self.peso = peso

    def inserir_atributos(self):
        self.comprimento = Decimal(input("insira o comprimento"))
        self.peso = Decimal(
            input("insira o peso de um fio de macarrao do comprimento desejado")
        )

    def mostrar_atributos(self):
        print("comprimento: ", self.comprimento)
        print("peso: ", self.peso)
