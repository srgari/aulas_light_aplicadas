class Pessoa {
  String nome;
  int idade;
  Pessoa(this.nome, this.idade);
}

main() {
  var pessoas = [
    Pessoa('ana', 20),
    Pessoa('bia', 19),
    Pessoa('carlos', 21),
    Pessoa('denise', 18),
  ];
  pessoas.forEach((x) => print('Nome: ${x.nome} \t Idade: ${x.idade}'));
}
