from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()  # Converte para minúsculas
        email = request.POST.get('email').lower()  # Converte para minúsculas
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Usuário já existente'})
        elif User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email já existente'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('index')

    return render(request, 'usuario/pages/Login_Register.html', {'register': True})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()  # Converte para minúsculas
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return JsonResponse({'error': 'Nome de usuário ou senha incorretos'})

    return render(request, 'usuario/pages/Login_Register.html', {'register': False})