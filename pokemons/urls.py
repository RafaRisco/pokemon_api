from django.urls import path

from .views import PokemonList

urlpatterns = [
    path('pokemon_list/', PokemonList.as_view(), name='pokemon_list'),
    path('<str:filter>/pokemon_list/', PokemonList.as_view(), name='pokemon_list'),
]
