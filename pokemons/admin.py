from django.contrib import admin

# Register your models here.
from .models import Pokemon

class PokemonAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'type_one',
        'type_two',
        'total',
        'hp',
        'attack',
        'defense',
        'sp_attack',
        'sp_def',
        'speed',
        'generation',
        'legendary'
    ]

admin.site.register(Pokemon, PokemonAdmin)
