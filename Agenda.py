import json
from Model.Pessoa import Pessoa
from Model.Contato import Contato
from Model.Telefone import Telefone


class Agenda():
  #Define o proprietário da agenda  
    def __init__(self, proprietario):
        self.proprietario = proprietario
        self.contatos = []
        
   def AdicionarNovoContato(self):
   #Adiciona um novo contato 
            nome = input("Nome do contato: ")
            email = input("Email: ")
            numero = input(Telefone(codigoPais, ddd, numero))
            self.contatos[Pessoa] = numero
            var jsoncontato =  {
                    "Contatos: [""nome": "nome",
                                "numero": "numero",
                                "email": "email",]}

    def ListarDados(self):
       #Lista os contatos já adicionados 
        for contatos in self.contatos:
            print(contatos)
        def __str__(self):
            return "%s" % (self.contatos)

    def PesquisarContato(self, nome):
      #Pesquisa um contato na agenda 
        nome = nome.lower()
        for a, b in enumerate (contatos):
            if b [0].lower() == nome:
                return (a)

    def ApagarUmContato(self, nome):
       #Apaga um contato a partir da pesquisa do nome 
        global agenda
        p = self.PesquisarContato(nome)
        if p != None:
            del agenda[p]
        while True:
            try:
                p == None
                break
            except:
                print("Contato não encontrado.")

    def QuantidadeDeContatos(self):
       #Retorna a quantidade de contatos presentes na Agenda 
        return len(self.contatos)

    def SalvarContato(self):
        pass
