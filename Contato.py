import datetime
from Model.Agenda import *
from Model.Pessoa import Pessoa
class Contato(Pessoa):
    def __init__(self, criacao, nome, nascimento, email):
        super(self, Pessoa).__init__(nome, nascimento, email)
        self.criacao = criacao(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

    def listarTelefone(self):
            print("\n\n\n-------")
            for e in self.contatos:
                listarDados(e[0], e[1], e[2])
            print("-------\n")
