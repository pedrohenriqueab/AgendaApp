import datetime
from Model.Agenda import Agenda
from Model.Pessoa import Pessoa
class Contato(Pessoa):
 #Definição de atributos e funções da classe Pessoa   
    def __init__(self, criacao, nome, nascimento, email):
        super(self, Pessoa).__init__(nome, nascimento, email)
        self.criacao = criacao

    def listarTelefone(self):
            for e in self.contatos:
                listarDados(e[0], e[1], e[2])
