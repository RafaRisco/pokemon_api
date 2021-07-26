import csv
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','pokemon_api.settings')

import django
django.setup()

from pokemons.models import Pokemon


with open("pokemon.csv", 'r', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    print('populating the database...')
    pokemons_created = 0
    for row in reader:
        created = Pokemon.objects.get_or_create(
            name=row[1],
            type_one=row[2],
            type_two=row[3],
            total=row[4],
            hp=row[5],
            attack=row[6],
            defense=row[7],
            sp_attack=row[8],
            sp_def=row[9],
            speed=row[10],
            generation=row[11],
            legendary=row[12]
            )
        pokemons_created += 1
        print(pokemons_created, 'pokemons created!')
    print('pokemons created!')
