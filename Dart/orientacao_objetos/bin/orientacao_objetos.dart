import '../src/pessoa.dart';
void main(List<String> arguments) {
  
  print('\nPessoa 1 ');

  var pessoa =  Pessoa(nome:'johne', idade: 31, sexo: 'M',altura: 1.70, peso: 100);
  print('Nome: ${pessoa.getNome()}');
  print('Idade: ${pessoa.getIdade()}');
  print('Sexo: ${pessoa.getSexo()}');
  print('IMC: ${pessoa.imc()}');
  
  print('\nPessoa 2 ');

  var pessoa2 =  Pessoa2(nome:'pedro', idade: 25, sexo: 'M');
  print(pessoa2.nome);
  print(pessoa2.idade);
  print(pessoa2.sexo);

  print('\nPessoa 3');

  var pessoa3 =  Pessoa3();
  print(pessoa3.nome);
  print(pessoa3.idade);
  print(pessoa3.sexo);
}
