from django.contrib import admin
from ponte.models import Ponte, Barra

# Register your models here.
class PonteAdmin(admin.ModelAdmin):
    ...

admin.site.register(Ponte)

class BarraAdmin(admin.ModelAdmin):
    ...

admin.site.register(Barra)