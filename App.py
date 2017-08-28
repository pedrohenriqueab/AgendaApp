from Model.Agenda import Agenda
from Model.Pessoa import Pessoa
from Model.Contato import Contato
from Model.Telefone import *
def menu():
    def regulariza(pergunta, inicio, fim):
        while True:
            try:
                valor = int(input(pergunta))
                if inicio <= valor <= fim:
                    return (valor)
                return
            except ValueError:
                print("valor inválido, digite entre %d e %d" % (inicio, fim))

    print("""
  1- Adicionar novo contato
  2- Pesquisar contato
  3- Visualizar lista de contatos
  4- Quantidade de Contatos
  5- Apagar um contato
  6- Sair""")
    return regulariza("Escolha uma opção: ", 1, 6)


while True:
    opção = menu()
    if opção == 6:
        break
    elif opção == 1:
        Agenda.AdicionarNovoContato:()
    elif opção == 2:
        Agenda.PesquisarContato:()
    elif opção == 3:
        Agenda.ListarDados:()
    elif opção == 4:
        Agenda.QuantidadeDeContatos:()
    elif opção == 5:
        Agenda.ApagarUmContato:()

def main():
    def nome():
        return (input("Nome: "))

    def telefone():
        return (input("Telefone: "))
if __name__=='__main__':
    main()
