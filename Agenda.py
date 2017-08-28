import json
import App
class Agenda():
    def __init__(self, proprietario):
        self.proprietario = proprietario
        self.contatos = []

    def AdicionarNovoContato(self, contatos):
        self.contatos.append(contatos)

    def ListarDados(self):
        for contatos in self.contatos:
            print(contatos)
        def __str__(self):
            return "%s" % (self.contatos)

    def PesquisarContato(self, nome):
        nome = nome.lower()
        for a, b in enumerate (Agenda):
            if b [0].lower() == nome:
                return (a)

    def ApagarUmContato(self, nome):
        global agenda
        p = self.Pesquisar(nome)
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

