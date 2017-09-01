import json
from Model.Pessoa import *
from Model.Contato import Contato
from Model.Telefone import Telefone


class Agenda():
    def __init__(self, proprietario):
        self.proprietario = proprietario
        self.contatos = []
        
   def AdicionarNovoContato(self):
            nome = input("Nome do contato: ")
            codigoPais = input("Digite o codigo do País: ")
            ddd = input("ddd: ")
            numero = input ("digite o número: ")
            email = input("Email: ")
            con = Contato()
            numero = Telefone(codigoPais, ddd, numero)
            self.contatos[Pessoa] = numero
            var jsoncontato =  {
                    "Contatos: [""nome": "nome",
                                "numero": "numero",
                                "email": "email",]}

    def ListarDados(self):
        for contatos in self.contatos:
            print(contatos)
        def __str__(self):
            return "%s" % (self.contatos)

    def PesquisarContato(self, nome):
        nome = nome.lower()
        for a, b in enumerate (contatos):
            if b [0].lower() == nome:
                return (a)

    def ApagarUmContato(self, nome):
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
        return len(self.contatos)

    def SalvarContato(self):
        pass
