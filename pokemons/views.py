from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.kwargs:
            filter = self.kwargs['filter']
            query = Pokemon.objects.filter(
                Q(type_one__icontains=filter) |
                Q(type_two__icontains=filter)
            )
        else:
            query = Pokemon.objects.all()
        return query
