from django.urls import path

from ponte.views import index
from ponte.views import ponte_detail

urlpatterns = [
    path('', index, name='index'),
    path('ponte/<str:username>/<int:ponte_id>/', ponte_detail, name='ponte_detail'),
]