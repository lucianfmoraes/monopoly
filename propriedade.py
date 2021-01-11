class Propriedade:
    def __init__(self, id, venda, aluguel, proprietario, posicao):
        self.id = id
        self.venda = int(venda)
        self.aluguel = int(aluguel)
        self.proprietario = proprietario
        self.posicao = posicao

    def getId(self):
        return self.id
        # teste
        # teste

    def setId(self, id):
        self.id = id

    def getVenda(self):
        return self.venda

    def setVenda(self, venda):
        self.venda = venda

    def getAluguel(self):
        return self.aluguel

    def setAluguel(self, aluguel):
        self.aluguel = aluguel

    def getProprietario(self):
        return self.proprietario

    def setProprietario(self, proprietario):
        self.proprietario = proprietario

    def getPosicao(self):
        return self.posicao
