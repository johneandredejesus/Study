

import 'humano.dart';

class Pessoa extends Humano {

  String _nome = '';

  String getNome() => _nome;

  int _idade = 0;

  int getIdade() => _idade; 

  String _sexo = '';

  String getSexo() => _sexo; 
  
  Pessoa({String nome='', int idade=0, String sexo='', double altura = 0, double peso=0}):
  super(altura: altura, peso: peso){
     _nome = nome;
     _idade = idade;
     _sexo = sexo;
  }
}

class Pessoa2{

  String nome = '';
  int idade = 0;
  String sexo = '';

  Pessoa2({this.nome = '', this.idade=0, this.sexo=''});
   
}

class Pessoa3{

  final String nome = 'Lucas';
  final int idade = 20;
  final String sexo = 'M';

}