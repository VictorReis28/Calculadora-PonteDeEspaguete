from decimal import Decimal
from math import sqrt


class Ponte:
    def __init__(self, peso, capacidade, n_barras, geometria, descricao_teste, n_teste):
        self.peso = None
        self.capacidade = None
        self.n_barras = None
        self.geometria = None
        self.descricao_teste = None
        self.n_teste = None

    def inserir_atributosPonte(self):
        self.peso = Barra.inserir_atributosBarra(Barra.peso) * self.n_barras
        self.capacidade = int(input("insira a capacidade EM GRAMAS"))
        self.n_barras = int(input("insira o numero de barras da ponte"))
        self.geometria = input("insira a geometria da ponte")
        self.descricao_teste = input("insira a descricao do teste")
        self.n_teste = int(input("insira o numero do teste"))
        if self.peso >= 1000:
            print("ponte invalida")
        else:
            return self.peso

    def mostrar_atributosPonte(self):
        print("peso: ", self.peso)
        print("capacidade: ", self.capacidade)
        print("n_barras: ", self.n_barras)
        print("geometria: ", self.geometria)
        print("descricao_teste: ", self.descricao_teste)
        print("n_teste: ", self.n_teste)
