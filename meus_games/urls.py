from django.urls import path
from meus_games.views import principal, contato, produtos


urlpatterns = [
    
    path('', principal),
    path('contato', contato),
    path('produtos', produtos),
]