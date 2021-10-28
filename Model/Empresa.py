class Empresa:
    def __init__(self, razao_social, endereco):
        self.razao_social = razao_social
        self.endereco = endereco

# para alterar os dados
    def setRazaoSocial(self, razao_social): self.razao_social = razao_social

    def setEndereco(self, endereco): self.endereco = endereco


#Mostrar os dados
    def getRazaoSocial(self): return self.razao_social

    def getEndereco(self): return self.endereco
