# coding: utf-8

from loja.models import Cantor, Disco, Genero
from rest_framework import serializers


class CantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cantor
        fields = ('nome',)


class DiscoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disco
        fields = ('titulo', 'genero', 'cantor', 'ano_lancamento', 'valor')


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('nome',)