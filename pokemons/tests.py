from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Pokemon, TypeOptions

class PokemonApiTestCase(TestCase):
    def setUp(self):
        self.new_pokemon = Pokemon.objects.create(
            name='Bulbasaur',
            type_one=TypeOptions.choices[1][0],
            type_two=TypeOptions.choices[2][0]
        )

    def test_view(self):
        url = reverse('pokemons:pokemon_list')
        client = APIClient()
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
