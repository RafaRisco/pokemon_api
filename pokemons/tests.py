from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Pokemon, TypeOptions

class PokemonApiTestCase(TestCase):
    def setUp(self):
        self.new_pokemon = Pokemon.objects.create(
            name='Bulbasaur',
            type_one=TypeOptions.DARK,
            type_two=TypeOptions.DRAGON
        )


    def test_view(self):
        url = reverse('pokemons:all_pokemon_list')
        client = APIClient()
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pokemon_in_view(self):
        url = reverse('pokemons:all_pokemon_list')
        client = APIClient()
        response = client.get(url, format='json')
        response_type_one = response.data[0]['type_one']
        response_type_two = response.data[0]['type_two']
        self.assertEqual(self.new_pokemon.type_one, response_type_one)
        self.assertEqual(self.new_pokemon.type_two, response_type_two)

    def test_pokemon_not_in_view(self):
        url = reverse('pokemons:filtered_pokemon_list', kwargs={'filter': 'Electric'})
        client = APIClient()
        response = client.get(url, format='json')
        self.assertEqual(len(response.data), 0)
