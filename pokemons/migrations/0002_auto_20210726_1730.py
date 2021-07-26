# Generated by Django 3.2.5 on 2021-07-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type_one',
            field=models.CharField(blank=True, choices=[('BUG', 'Bug'), ('DAR', 'Dark'), ('DRA', 'Dragon'), ('ELE', 'Electric'), ('FAI', 'Fairy'), ('FIG', 'Fighting'), ('FIR', 'Fire'), ('FLY', 'Flying'), ('GHO', 'Ghost'), ('Grass', 'Grass'), ('GRO', 'Ground'), ('ICE', 'Ice'), ('NOR', 'Normal'), ('POI', 'Poison'), ('PSY', 'Psychic'), ('ROC', 'Rock'), ('STE', 'Steel'), ('WAT', 'Water')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type_two',
            field=models.CharField(blank=True, choices=[('BUG', 'Bug'), ('DAR', 'Dark'), ('DRA', 'Dragon'), ('ELE', 'Electric'), ('FAI', 'Fairy'), ('FIG', 'Fighting'), ('FIR', 'Fire'), ('FLY', 'Flying'), ('GHO', 'Ghost'), ('Grass', 'Grass'), ('GRO', 'Ground'), ('ICE', 'Ice'), ('NOR', 'Normal'), ('POI', 'Poison'), ('PSY', 'Psychic'), ('ROC', 'Rock'), ('STE', 'Steel'), ('WAT', 'Water')], max_length=20, null=True),
        ),
    ]
