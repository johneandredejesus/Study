from django.db import models

# Create your models here.

class Livro(models.Model):

    nome = models.CharField(max_length=100, unique=True)
    isbn = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    numero_de_paginas = models.IntegerField()
    editora = models.CharField(max_length=100)
    pais = models.CharField(max_length=40)
    lancamento = models.DateField()

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['id']

    def __str__(self):
        return self.nome


class Capa(models.Model):
    
    livro = models.OneToOneField(Livro, related_name='capas', on_delete=models.CASCADE)
    frente = models.TextField()
    verso = models.TextField()

    class Meta:
        verbose_name = 'Capa'
        verbose_name_plural = 'Capas'
        ordering = ['id']

class Personagem(models.Model):
    
    livros =  models.ManyToManyField(Livro,related_name='personagens')
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Personagem'
        verbose_name_plural = 'Personagens'
        ordering = ['id']
    
    def __str__(self):
        return self.nome


class Detalhe(models.Model):

    personagem = models.ForeignKey(Personagem, related_name='detalhes', on_delete=models.CASCADE)
    detalhe = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Detalhe'
        verbose_name_plural = 'Detalhes'
        ordering = ['id']
    
    def __str__(self):
        return self.detalhe

class Comprar(models.Model):
    
    livro = models.OneToOneField(Livro, related_name='Comprar',  on_delete=models.CASCADE)
    url = models.URLField()
    
    class  Meta:
        verbose_name = 'Comprar'
        verbose_name_plural = 'Comprar'

    def __str__(self):
        return self.url
    




