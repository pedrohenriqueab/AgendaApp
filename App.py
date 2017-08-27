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
  1- Quantidade de contatos
  2- Incluir contato
  3- Apagar contato
  4-Visualisar lista de contatos
  5- Sair""")
  return regulariza("Escolha uma opção: ", 1, 5)
while True:
    op = menu()
    if op == 5
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
