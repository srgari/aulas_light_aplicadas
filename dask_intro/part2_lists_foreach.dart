main() {
  var listaNomes = ['ana', 'bia', 'carlos', 'denise'];
  var nomesTerminadosemA = listaNomes.where((nome) => nome.endsWith('a'));
  print(nomesTerminadosemA);
  nomesTerminadosemA.forEach(print);
  nomesTerminadosemA.forEach((yo) => print('nome: $yo'));
}
