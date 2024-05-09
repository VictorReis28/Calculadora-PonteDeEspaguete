from django.shortcuts import render
from .models import Ponte

# Create your views here.

def index(request):
    pontes = Ponte.objects.order_by('id')
    context = {'pontes': pontes}
    return render(request, 'ponte/pages/home.html', context)


def Login_Register(request):
    return render(request, 'ponte/pages/Login_Register.html')