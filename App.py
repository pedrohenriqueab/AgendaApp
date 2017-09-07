from Model.Agenda import Agenda
from Model.Pessoa import Pessoa
from Model.Contato import Contato
from Model.Telefone import Telefone
def menuAgenda():
    while True:
        print("""                         MENU
            1- Adicionar novo contato
            2- Pesquisar contato
            3- Visualizar lista de contatos
            4- Quantidade de Contatos
            5- Apagar um contato           
            6- Sair""")

        opcao = int(input("              Escolha uma opção: "))

        if opcao == 6:
 +            break
 +      elif opcao == 1:
 +            cont.AdicionarNovoContato()
 +      elif opcao == 2:
 +            cont.PesquisarContato()
 +      elif opcao == 3:
 +            cont.ListarDados()
 +      elif opcao == 4:
 +            cont.QuantidadeDeContatos()
 +      elif opcao == 5:
 +            cont.ApagarUmContato()
    return opcao

def main():
    menuAgenda()


if __name__ == '__main__':
    main()
