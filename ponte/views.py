from django.shortcuts import render, get_object_or_404, redirect
from .models import Ponte, Barra
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        pontes = Ponte.objects.filter(autor=request.user).order_by('-id')
        return render(request, 'ponte/pages/home.html', context={'pontes': pontes})
    else:
        return render(request, 'ponte/pages/homeNL.html')


def ponte_detail(request, username, ponte_id):
    ponte = get_object_or_404(Ponte, id=ponte_id, autor__username=username)
    barras = Barra.objects.filter(ponte=ponte)

    resultado_total = calcular_resultado_total(request, username, ponte_id)

    return render(request, 'ponte/pages/resultados.html', {'ponte': ponte, 'barras': barras, 'resultado_total': resultado_total})

def adicionar_barra(request, username, ponte_id):
    if request.method == 'POST':
        ponte = get_object_or_404(Ponte, id=ponte_id, autor__username=username)
        nome = request.POST.get('nome-barra')
        comprimento = request.POST.get('comprimento-barra')
        esforco_interno = request.POST.get('esforco-interno')
        tipo_esforco = request.POST.get('tipo-esforco')

        Barra.objects.create(
            nome=nome,
            cm=comprimento,
            esforco_interno=esforco_interno,
            tipo=tipo_esforco,
            ponte=ponte
        )
        return redirect('ponte_detail', username=username, ponte_id=ponte_id)
    return redirect('ponte_detail', username=username, ponte_id=ponte_id)

def excluir_barra(request, username, ponte_id, barra_id):
    barra = get_object_or_404(Barra, id=barra_id, ponte__id=ponte_id, ponte__autor__username=username)
    barra.delete()
    return redirect('ponte_detail', username=username, ponte_id=ponte_id)


def calcular_resultado_total(request, username, ponte_id):
    ponte = get_object_or_404(Ponte, id=ponte_id, autor__username=username)
    barras = Barra.objects.filter(ponte=ponte)

    resultado_total = 0

    for barra in barras:
        numero_fios_revisados = barra.calcular_numero_fios_revisados()
        resultado_barra = barra.cm * numero_fios_revisados
        resultado_total += resultado_barra

    ponte.peso_metade = resultado_total
    ponte.save()


@login_required
def criar_ponte(request):
    if request.method == 'POST':
        nome_ponte = request.POST['nome_ponte']
        peso_linear = float(request.POST['peso_linear'])
        
        autor = request.user
        
        ponte = Ponte.objects.create(
            autor=autor,
            nome_ponte=nome_ponte,
            peso_linear=peso_linear
        )
        return redirect('ponte_detail', username=autor.username, ponte_id=ponte.pk)

    else:
        return render(request, 'ponte/partils/home.html')
    
