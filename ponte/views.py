from django.shortcuts import render, get_object_or_404
from .models import Ponte, Barra

# Create your views here.

def index(request):
    pontes = Ponte.objects.all().order_by('-id')
    return render(request, 'ponte/pages/home.html', context={'pontes': pontes})


def ponte_detail(request, username, ponte_id):
    ponte = get_object_or_404(Ponte, id=ponte_id, autor__username=username)
    barras = Barra.objects.filter(ponte=ponte)
    return render(request, 'ponte/pages/resultados.html', {'ponte': ponte, 'barras': barras})