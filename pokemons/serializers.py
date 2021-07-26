from rest_framework import serializers

from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = [
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
