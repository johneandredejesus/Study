from django.contrib.admin import ModelAdmin, register
from .models import Capa, Detalhe, Livro, Personagem, Comprar
# Register your models here.

@register(Capa)
class CapaAdmin(ModelAdmin):

    list_display = ('livro', 'frente', 'verso')

@register(Detalhe)
class DetalheAdmin(ModelAdmin):

    list_display = ('personagem', 'detalhe')

    def __str__(self):
        return self.personagem

@register(Livro)
class LivroAdmin(ModelAdmin):

    list_display = ('nome', 'isbn', 'autor', 'numero_de_paginas', 'editora', 'pais', 'lancamento')

    def __str__(self):
        return self.nome

@register(Personagem)
class  PersonagemAdmin(ModelAdmin):

    list_display = ('nome', 'livros_relacionados')
    
    def livros_relacionados(self, obj):

        return [livro.nome for livro in obj.livros.all()]

    def __str__(self):
        return self.nome


@register(Comprar)
class ComprarAdmin(ModelAdmin):

    list_display = ('url', 'livro')
    
    def livros_relacionado(self, obj):

        return [livro.nome for livro in obj.livros.all()]

    def __str__(self):
        return self.url