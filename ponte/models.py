from django.db import models
from django.contrib.auth.models import User

# Create your models here.
tipos = {'T': 'Tração', 'C': 'Compressão'}
class Ponte(models.Model):
    nome_ponte = models.CharField(max_length=50)
    peso_linear = models.FloatField(blank=True, null=True)
    peso_metade = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nome_ponte

class Barra(models.Model):
    ponte = models.ForeignKey(Ponte, on_delete=models.CASCADE)
    nome_barra = models.CharField(max_length=50)
    cm = models.FloatField()
    esforco_interno = models.FloatField()
    tipo = models.CharField(max_length=1, choices=tipos)
    n_fios = models.FloatField(blank=True, null=True)
    n_fios_revisado = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Barras'

    def __str__(self):
        return self.nome_barra