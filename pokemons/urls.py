from django.urls import path

from .views import PokemonList

urlpatterns = [
    path('pokemon_list/', PokemonList.as_view(), name='all_pokemon_list'),
    path('<str:filter>/pokemon_list/', PokemonList.as_view(), name='filtered_pokemon_list'),
]
