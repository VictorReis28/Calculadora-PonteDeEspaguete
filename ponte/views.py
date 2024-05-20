from django.shortcuts import render
from .models import Ponte

# Create your views here.

def index(request):
    pontes = Ponte.objects.all().order_by('-id')
    return render(request, 'ponte/pages/home.html', context={'pontes': pontes})


def Login_Register(request):
    return render(request, 'ponte/pages/Login_Register.html')
