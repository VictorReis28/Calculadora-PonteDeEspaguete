from django.db import models
from django.contrib.auth.models import User

# Create your models here.

tipos = {'T': 'Tração', 'C': 'Compressão'}
class Ponte(models.Model):
    models.ForeignKey(User, on_delete=models.CASCADE)
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
    ponte = models.ForeignKey(Ponte, on_delete=models.CASCADE)
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