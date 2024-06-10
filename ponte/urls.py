from django.urls import path

from ponte.views import index
from ponte.views import ponte_detail, adicionar_barra, excluir_barra

urlpatterns = [
    path('', index, name='index'),
    path('ponte/<str:username>/<int:ponte_id>/', ponte_detail, name='ponte_detail'),
    path('ponte/<str:username>/<int:ponte_id>/adicionar_barra/', adicionar_barra, name='adicionar_barra'),
    path('ponte/<str:username>/<int:ponte_id>/excluir_barra/<int:barra_id>/', excluir_barra, name='excluir_barra'),
]