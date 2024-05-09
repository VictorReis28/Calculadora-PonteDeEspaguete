from django.contrib import admin
from django.urls import path

from ponte.views import index, Login_Register, get_barras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('get-barras/', get_barras, name='get-barras'),
    path('usuario/',Login_Register, name='Login_Register'),
]
