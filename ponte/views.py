from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Ponte, Barra
from django.contrib.auth.decorators import login_required
import csv
# Create your views here.

def index(request):
    query = request.GET.get('q')
    pontes = None
    resultados = None
    
    if query:
        resultados = Ponte.objects.filter(nome_ponte__icontains=query, autor=request.user).order_by('-id')
    elif request.user.is_authenticated:
        pontes = Ponte.objects.filter(autor=request.user).order_by('-id')

    return render(request, 'ponte/pages/home.html', {'pontes': pontes, 'resultados': resultados, 'query': query})


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
        numero_fios = barra.calcular_numero_fios()
        numero_fios_revisados = barra.calcular_numero_fios_revisados()

        barra.n_fios = numero_fios
        barra.n_fios_revisados = numero_fios_revisados
        barra.save()

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
    
def exportar_csv(request, username, ponte_id):
    ponte = get_object_or_404(Ponte, id=ponte_id, autor__username=username)
    barras = ponte.barras.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="Ponte: {ponte.autor.username} - {ponte.nome_ponte}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome da Ponte', ponte.nome_ponte])
    writer.writerow(['Autor', ponte.autor.username])
    writer.writerow([]) 

    for barra in barras:
        writer.writerow([])
        writer.writerow(['Nome da Barra', barra.nome])
        writer.writerow(['Comprimento (cm)', barra.cm])
        writer.writerow(['Tipo de Esforco', barra.tipo])
        writer.writerow(['Esforco Interno', barra.esforco_interno])
        writer.writerow(['Numero de Fios', barra.n_fios])
        writer.writerow(['Numero de Fios Revisados', barra.n_fios_revisados])
        writer.writerow([])

    return response

@login_required
def excluir_ponte(request, username, ponte_id):
    ponte = get_object_or_404(Ponte, id=ponte_id, autor__username=username)
    if ponte.autor == request.user:
        ponte.delete()
    return redirect('index')