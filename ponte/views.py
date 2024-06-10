from django.shortcuts import get_object_or_404, render, redirect
from .models import Ponte, Barra
from .forms import PonteForm, BarraForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.urls import reverse
import json

# Create your views here.

def index(request, id_ponte = None):
    pontes = Ponte.objects.order_by('id')
    if id_ponte:
        barras = Barra.objects.get(ponte_id=id_ponte)

    form_ponte = PonteForm()
    '''if request.method == 'GET':
         
    form_barra = BarraForm()'''

    if request.method == 'POST':
        form_ponte = PonteForm(request.POST)
        if form_ponte.is_valid():
            form_ponte.save()  
            return HttpResponseRedirect(reverse('index'))
        
        else:
            return render(request, 'ponte.html', {'pontes': pontes, 'form_ponte': form_ponte})
        
    else:
        return render(request, 'ponte.html', {'pontes': pontes, 'form_ponte': form_ponte})

def get_barras(request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            if request.method == 'GET':
                id_ponte = request.GET.get('data_id')
                barras = list(Barra.objects.filter(ponte_id=id_ponte).values())
                return JsonResponse({'barras': barras})
            else:
                return JsonResponse({'status': 'Invalid request'}, status=400)
        else:
            return HttpResponseBadRequest('Invalid request')
        
def add_barras(request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            if request.method == 'GET':
                id_ponte = request.GET.get('data_id')
                barras = list(Barra.objects.filter(ponte_id=id_ponte).values())
                return JsonResponse({'barras': barras})
            else:
                return JsonResponse({'status': 'Invalid request'}, status=400)
        else:
            return HttpResponseBadRequest('Invalid request')
        
def delete_barras(request, barraid):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            barra = get_object_or_404(Barra, id = barraid)
            if request.method == 'POST':
                barra.delete()
                return JsonResponse({'status': 'Todo deleted!'})
            else:
                return JsonResponse({'status': 'Invalid request'}, status=400)
        else:
            return HttpResponseBadRequest('Invalid request')

def todos(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            todos = list(Barra.objects.all().values())
            return JsonResponse({'context': todos})
        if request.method == 'POST':
            data = json.load(request)
            todo = data.get('payload')
            print(todo)
            if todo['tipo'] == 'T':
                n_fios = (float(todo['esforco_interno'])/42.67)
            else:
                n_fios = ((float(todo['esforco_interno']) * (float(todo['cm']) * 10) ** 2 / 27906 * 1 ** 4) ** (1/2))
            n_fios_revisado = n_fios * 1.1
            t =10 # Numero de casas
            n_fios = int(n_fios * 10**t)/10**t
            n_fios_revisado = int(n_fios_revisado * 10**t)/10**t
            Barra.objects.create(ponte_id=todo['ponte_id'], nome_barra=todo['nome_barra'], cm=todo['cm'], esforco_interno=todo['esforco_interno'], tipo=todo['tipo'], n_fios=n_fios, n_fios_revisado=n_fios_revisado)
            return JsonResponse({'status': 'Todo added!'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def todo(request, todoId):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        todo = list(Barra.objects.filter(ponte_id=todoId).values())
        ponte = get_object_or_404(Ponte, id=todoId)
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('payload')
            if ((updated_values['peso_linear']) != '') or (ponte.peso_linear == None):
                ponte.peso_linear = updated_values['peso_linear']
                todas = 0
                for barra in todo:
                    aux = float(barra['cm']) * float(barra['n_fios_revisado'])
                    todas += aux
                ponte.peso_metade = todas * (float(ponte.peso_linear))
                ponte.save()

                return JsonResponse({'status': 'Todo updated!'})
            if ((updated_values['peso_linear']) == '') and (ponte.peso_linear != None):
                return JsonResponse({'status': 'Todo updated!'})

        if request.method == 'DELETE':
            todo.delete()
            return JsonResponse({'status': 'Todo deleted!'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')


"""
def Nova_barra(request):
    if request.method != 'POST':
        form = BarraForm()
    else:
        form = BarraForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, )
"""

def Login_Register(request):
    return render(request, 'Login_Register.html')