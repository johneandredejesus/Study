class Humano{

  double _altura = 0;

  double getAltura() => _altura;

  double _peso = 0;

  double getPeso() => _peso;

  Humano({double altura=0, double peso=0}){
    _altura = altura;
    _peso = peso;
  }

  double imc() => _peso/ (_altura * _altura);
  
}