import json
def regulariza (pergunta, inicio, fim):
  while True:
    try:
      valor = int(input(pergunta))
      if inicio <= valor <= fim:
        return (valor)
      return
    except ValueError:
      print("valor inválido, digite entre %d e %d" % (inicio, fim))
def menu():
  print("""
  1- Adicionar contato
  2- Editar contato
  3-Pesquisar contato
  4-Visualisar lista de contatos
  5-Aapagar contato
  6- Sair""")
  return regulariza("Escolha uma opção: ", 1, 6)
while True:
    op = menu()
    if op == 6
        break


def main():
    while True:
        try:
            f = open("meses.txt", encoding="utf8")
            linhas = f.readlines()

            for linha in linhas:
                print(linha.strip())

            break

        except FileNotFoundError:
            print("arquivo não encontrado")
               
if __name__ == '__main__':
    main()
