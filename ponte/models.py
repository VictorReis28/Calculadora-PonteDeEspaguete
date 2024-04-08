from django.db import models

# Create your models here.

class barra(models.Model):
    id_barra = models.AutoField(primary_key=True)
    cm = models.FloatField()
    esforco_interno = models.FloatField()
    tipo = models.CharField(max_length=5)
    n_fios = models.FloatField()


class ponte(models.Model):
    id_ponte = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    barras = barra.objects.all()
    peso_linear = models.FloatField()
    peso_metade = models.FloatField()