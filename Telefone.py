import datetime
class Telefone(object):
    def __init__(self, numero, ddd, codigoPais):
        self.numero = numero
        self.ddd = ddd
        self.codigoPais = codigoPais

class Contato():
    def __init__(self, criacao):
        self.criacao = criacao(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

    def listarTelefone(self):
        pass
