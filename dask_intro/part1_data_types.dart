//comment

int lele = 10;
//lele = 15; essa merda quebra

var inteiro2 = 10;
double inteiro3 = 10;
dynamic lala = 30.0;
dynamic texto = 'sergio';

int? aInt;

final idade = 33;

void sergio() {
  print('funcao sergio yo');
}

void main(args) {
  int inteiro = 10;
  inteiro = 15;
  print(inteiro);
  print('Hello, World!');
  if (aInt is int) {
    print('o valor de aInt é $aInt');
  } else {
    print(' essa merda tá vazia! ó: $aInt');
  }
  print(lala * 2); // 60.0
  print(texto * 2); // sergiosergio

  print(aInt); // isso é nulo
  sergio();
  print(args);

  print(args.elementAt(0));
  print(args[0]);
  print(args[0] * 2);
  print(int.parse(args.elementAt(0)));
  print(int.parse(args.elementAt(0)) * 2);
}
