from Model.Agenda import Agenda
from Model.Pessoa import Pessoa
from Model.Contato import Contato
from Model.Telefone import Telefone #Main do programa

def menuAgenda():
   #Imprime na tela do usuário o Menu para com as seguintes opções:
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
              break
       elif opcao == 1:
              aux1.AdicionarNovoContato()
       elif opcao == 2:
              aux1.PesquisarContato()
       elif opcao == 3:
              aux1.ListarDados()
       elif opcao == 4:
              aux1.QuantidadeDeContatos()
       elif opcao == 5:
              aux1.ApagarUmContato()
    return opcao

def criarAgenda():
   #Apresenta ao usuário a opção de Criar Agenda 
    print("""                         MENU
            1- Criar Agenda          
            2- Sair""")
    opcao1 = int(input("              Escolha uma opção: "))

        if opcao1 == 2:
             break
      elif opcao1 == 1:
             aux1 = input(Pessoa(nome, nascimento, email))
             menuAgenda()
    return opcao1

def main():
    criarAgenda()


if __name__ == '__main__':
    main()
