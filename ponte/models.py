from django.db import models

# Create your models here.

class Ponte(models.Model):
    nome = models.CharField(max_length=50)
    peso_linear = models.FloatField()
    peso_metade = models.FloatField()

    def __str__(self):
        return self.nome

class Barra(models.Model):
    ponte = models.ForeignKey(Ponte, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    cm = models.FloatField()
    esforco_interno = models.FloatField()
    tipo = models.CharField(max_length=5)
    n_fios = models.FloatField()
    n_fios_revisados = models.FloatField()

    class Meta:
        verbose_name_plural = 'Barras'

    def __str__(self):
        return self.nome