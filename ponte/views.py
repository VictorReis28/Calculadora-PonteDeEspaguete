from django.shortcuts import get_object_or_404, render, redirect
from .models import Ponte, Barra
from .forms import PonteForm, BarraForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.urls import reverse

# Create your views here.

def index(request, id_ponte = None):
    pontes = Ponte.objects.order_by('id')
    if id_ponte:
        barras = Barra.objects.get(ponte_id=id_ponte)

    form_ponte = PonteForm()
    
    form_barra = BarraForm()
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
        
def delete_barras(request):
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