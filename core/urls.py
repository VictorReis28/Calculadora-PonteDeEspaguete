from django.contrib import admin
from django.urls import path

from ponte.views import home
from resultados.views import resultados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('resultados', resultados,name='resultados')
]
