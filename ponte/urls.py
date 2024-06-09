from django.urls import path

from ponte.views import index

urlpatterns = [
    path('', index, name='index'),
]