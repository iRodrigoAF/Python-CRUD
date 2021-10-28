class Pessoa:
    def __init__(self, nome, endereco, bairro, cep, cidade, estado, id_empresa):
        self.nome = nome
        self.endereco = endereco
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.id_empresa = id_empresa

# Para alterar os dados
    def setNome(self, nome): self.nome = nome

    def setEndereco(self, endereco): self.endereco = endereco

    def setBairro(self, bairro): self.bairro = bairro

    def setCEP(self, cep): self.cep = cep

    def setCidade(self, cidade): self.cidade = cidade

    def setEstado(self, estado): self.estado = estado

#Mostrar os dados
    def getNome(self): return self.nome

    def getEndereco(self): return self.endereco

    def getBairro(self): return self.bairro

    def getCEP(self): return self.cep

    def getCidade(self): return self.cidade

    def getEstado(self): return self.estado

    def getIdEmpresa(self): return self.id_empresa
