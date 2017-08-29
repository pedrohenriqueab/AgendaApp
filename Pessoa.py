import datetime

class Pessoa(object):
    
    def main(self, nome, nascimento, email):
        self.nome = nome
        self.nascimento = nascimento(datetime.date)
        self.email = email
