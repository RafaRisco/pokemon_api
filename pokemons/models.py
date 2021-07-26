from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class TypeOptions(models.TextChoices):
    BUG = 'Bug'
    DARK = 'Dark'
    DRAGON = 'Dragon'
    ELECTRIC = 'Electric'
    FAIRY = 'Fairy'
    FIGHTING = 'Fighting'
    FIRE = 'Fire'
    FLYING = 'Flying'
    GHOST = 'Ghost'
    GRASS = 'Grass'
    GROUND = 'Ground'
    ICE = 'Ice'
    NORMAL = 'Normal'
    POISON = 'Poison'
    PSYCHIC = 'Psychic'
    ROCK = 'Rock'
    STEEL = 'Steel'
    WATER = 'Water'

class Pokemon(models.Model):
    name        = models.CharField(max_length=225)
    type_one    = models.CharField(max_length=20, choices=TypeOptions.choices, blank=True, null=True)
    type_two    = models.CharField(max_length=20, choices=TypeOptions.choices, blank=True, null=True)
    total       = models.PositiveIntegerField(default=0)
    hp          = models.PositiveIntegerField(default=0)
    attack      = models.PositiveIntegerField(default=0)
    defense     = models.PositiveIntegerField(default=0)
    sp_attack   = models.PositiveIntegerField(default=0)
    sp_def      = models.PositiveIntegerField(default=0)
    speed       = models.PositiveIntegerField(default=0)
    generation  = models.PositiveIntegerField(default=0)
    legendary   = models.BooleanField(default=False)

    def __str__(self):
        return self.name
