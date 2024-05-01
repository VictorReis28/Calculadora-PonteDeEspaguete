from django.contrib import admin
from django.urls import path

from ponte.views import index
from ponte.views import Login_Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('usuario/',Login_Register, name='Login_Register'),
]
