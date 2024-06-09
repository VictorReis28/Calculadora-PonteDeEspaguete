from django.shortcuts import render

# Create your views here.

def Login_Register(request):
    return render(request, 'usuario/pages/Login_Register.html')