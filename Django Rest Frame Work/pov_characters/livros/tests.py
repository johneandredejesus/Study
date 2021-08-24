import requests
# Create your tests here.


class TestLivros():

    headers = {'Authorization': 'Token 095967b756d1b5ca0d4141f348332e6bfad0fab6'}
    get_livro = 'http://127.0.0.1:8000/api/v1/livros/1/'
    get_livro_personagem = 'http://127.0.0.1:8000/api/v1/livros/1/personagens/'
    get_livro_capa = 'http://127.0.0.1:8000/api/v1/livros/3/capas/'
    get_livro_comprar = 'http://127.0.0.1:8000/api/v1/livros/1/comprar/'

    def test_get_livro(self):
        resposta = requests.get(self.get_livro, headers=self.headers)
        assert  resposta.json().__len__() > 0

    def test_get_livro_personage(self):

        resposta = requests.get(self.get_livro_personagem, headers=self.headers)
        assert resposta.json()[0]['id'] == 1
    
    def test_get_livro_capa(self):

        resposta = requests.get(self.get_livro_capa, headers=self.headers)
        assert  resposta.json()['frente'] != ''
    
    def test_get_livro_comprar(self):

        resposta = requests.get(self.get_livro_comprar, headers=self.headers)
        assert  resposta.json()['url'] != ''
   

class TestPersonagnes():

    headers = {'Authorization': 'Token 095967b756d1b5ca0d4141f348332e6bfad0fab6'}
    get_datalhes_personagen = 'http://127.0.0.1:8000/api/v1/personagens/1/detalhes/'
    get_personagem = 'http://127.0.0.1:8000/api/v1/personagens/1/'
    get_personagens =  'http://127.0.0.1:8000/api/v1/personagens/'
    get_personagens_livros = 'http://127.0.0.1:8000/api/v1/personagens/1/livros/'

    def test_get_datalhes_personagen(self):

        resposta = requests.get(self.get_datalhes_personagen, headers=self.headers)
        assert resposta.json().__len__() > 0

    def test_get_personagem(self):

        resposta = requests.get(self.get_personagem, headers=self.headers)
        assert resposta.json()['id'] == 1

    def test_get_personagens(self):

        resposta = requests.get(self.get_personagens, headers=self.headers)
        assert resposta.json().__len__() > 0
    
    def test_get_personagens_livros(self):

        resposta = requests.get(self.get_personagens_livros, headers=self.headers)
        assert resposta.json().__len__() > 0