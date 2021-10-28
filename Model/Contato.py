from Model.Pessoa import Pessoa
class Contato(Pessoa):

    def __init__(self, nome, endereco, bairro, cep, cidade, estado, id_empresa):
        self.nome = nome
        self.endereco = endereco