from django.db import models

# Create your models here.

class TypeOptions(models.TextChoices):
    BUG = 'BUG', 'Bug'
    DARK = 'DAR', 'Dark'
    DRAGON = 'DRA', 'Dragon'
    ELECTRIC = 'ELE', 'Electric'
    FAIRY = 'FAI', 'Fairy'
    FIGHTING = 'FIG', 'Fighting'
    FIRE = 'FIR', 'Fire'
    FLYING = 'FLY', 'Flying'
    GHOST = 'GHO', 'Ghost'
    GRASS = 'GRA', 'Grass'
    GROUND = 'GRO', 'Ground'
    ICE = 'ICE', 'Ice'
    NORMAL = 'NOR', 'Normal'
    POISON = 'POI', 'Poison'
    PSYCHIC = 'PSY', 'Psychic'
    ROCK = 'ROC', 'Rock'
    STEEL = 'STE', 'Steel'
    WATER = 'WAT', 'Water'

class Pokemon(models.Model):
    name        = models.CharField(max_length=225)
    type_one    = models.CharField(max_length=3, choices=TypeOptions.choices, blank=True, null=True)
    type_two    = models.CharField(max_length=3, choices=TypeOptions.choices, blank=True, null=True)
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
