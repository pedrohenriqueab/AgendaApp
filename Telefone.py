import datetime
class Telefone(object):
    def __init__(self,codigoPais, ddd, numero):
        self.codigoPais = codigoPais
        self.ddd = ddd
        self.numero = numero
      

class Contato():
    def __init__(self, criacao):
        self.criacao = criacao(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

    def listarTelefone(self):
        pass
