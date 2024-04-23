from django.contrib import admin
from django.urls import path

from ponte.views import home
from ponte.views import Login_Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('usuario/',Login_Register, name='Login_Register'),
]
