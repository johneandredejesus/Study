from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Capa, Comprar, Personagem, Livro, Detalhe
from .serializers import PersonagemSerializer, DetalheSerializer, LivroSerializer, CapaSerializer, ComprarSerializer

# Create your views here.

class LivroViewSet(ReadOnlyModelViewSet):

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    @action(detail=True, methods=['get'])
    def capas(self, request, pk=None):
        
        capa = Capa.objects.filter(livro_id=pk).first()
        serializer = CapaSerializer(capa)

        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def personagens(self, request, pk=None):
        
        livro = self.get_object()
        personagens = livro.personagens.all()
        serializer = PersonagemSerializer(personagens, many=True)

        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def comprar(self, request, pk):

        comprar = Comprar.objects.filter(livro_id=pk).first()
        serializer = ComprarSerializer(comprar)

        return Response(serializer.data)



class PersonagenViewSet(ReadOnlyModelViewSet):

    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer

    @action(detail=True, methods=['get'])
    def livros(self, request, pk=None):
        
        personagem = self.get_object()
        livros = personagem.livros.all()
        serializer = LivroSerializer(livros, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None):

        detalhes = Detalhe.objects.filter(personagem_id=pk)
        serializer = DetalheSerializer(detalhes, many=True)
 
        return Response(serializer.data)



