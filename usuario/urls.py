from django.urls import path

from usuario.views import Login_Register

urlpatterns = [
    path('usuario/',Login_Register, name='Login_Register'),
]