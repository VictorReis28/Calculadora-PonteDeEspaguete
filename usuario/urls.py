from django.urls import path
from .views import register_view, login_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('usuario/', login_view, name='login'),
    path('usuario/register/', register_view, name='register'),
    path('usuario/login/', login_view, name='login'),
    path('usuario/logout/', LogoutView.as_view(next_page='/'), name='logout'),

]