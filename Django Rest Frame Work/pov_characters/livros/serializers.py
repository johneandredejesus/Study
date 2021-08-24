from rest_framework.serializers import ModelSerializer
from .models import Personagem, Detalhe, Livro, Capa, Comprar


class DetalheSerializer(ModelSerializer):

    class Meta:

        model = Detalhe
        fields = ('detalhe', )


class PersonagemSerializer(ModelSerializer):
    
    detalhes = DetalheSerializer(many=True, read_only=True)

    class Meta:
        model = Personagem
        fields = ('id', 'nome', 'detalhes')



class CapaSerializer(ModelSerializer):

    class Meta:

        model = Capa
        fields = ('frente', 'verso')

class LivroSerializer(ModelSerializer):
   
    capa = CapaSerializer(read_only=True)

    class Meta:

        model = Livro
        fields = ('id', 'nome', 'isbn', 'autor', 'numero_de_paginas',
                  'editora', 'pais', 'lancamento', 'capa')


class ComprarSerializer(ModelSerializer):

    class Meta:

        model = Comprar
        fields = ('url', )