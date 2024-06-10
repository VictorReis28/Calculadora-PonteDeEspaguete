from django.db import models
from django.contrib.auth.models import User
import math

tipos = {'T': 'Tração', 'C': 'Compressão'}

class Ponte(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_ponte = models.CharField(max_length=50)
    peso_linear = models.FloatField(null=True, blank=True)
    peso_metade = models.FloatField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='ponte/covers/%Y/%m/%d/', default='', blank=True)

    def __str__(self):
        return self.nome_ponte

class Barra(models.Model):
    ponte = models.ForeignKey(Ponte, on_delete=models.CASCADE, related_name='barras')
    nome = models.CharField(max_length=50)
    cm = models.FloatField(null=True)
    esforco_interno = models.FloatField(null=True)
    tipo = models.CharField(max_length=1, choices=tipos)
    n_fios = models.FloatField(null=True, blank=True)
    n_fios_revisados = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Barras'

    def __str__(self):
        return self.nome

    def calcular_numero_fios(self):
        if self.tipo == 'C':
            return math.sqrt((self.esforco_interno * (self.cm * 10) ** 2) / (27906 * 1 ** 4))
        elif self.tipo == 'T':
            return self.esforco_interno / 42.67
        else:
            return 0 
    
    def calcular_numero_fios_revisados(self):
        numero_fios = self.calcular_numero_fios()
        numero_fios_revisados = numero_fios + (numero_fios * 0.1) 
        return numero_fios_revisados
