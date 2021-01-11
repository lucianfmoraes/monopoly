import random
import constantes


class Jogador:
    def __init__(self, id, comportamento, ativo):
        self.id = id
        self.nome = 'Jogador ' + str(id)
        self.comportamento = comportamento
        self.coins = 300
        self.propriedades = []
        self.posicao = 1
        self.rodadas = 0
        self.ativo = ativo

    # GETTERS & SETTERS
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getComportamento(self):
        return self.comportamento

    def getCoins(self):
        return self.coins

    def setCoins(self, coins):
        self.coins = coins

    def somaCoins(self, coins):
        self.setCoins(self.getCoins() + coins)

    def subtraiCoins(self, coins):
        self.setCoins(self.getCoins() - coins)

    def getPropriedades(self):
        return self.propriedades

    def setPropriedades(self, propriedade):
        self.propriedades.append(propriedade)

    def getPosicao(self):
        return self.posicao

    def setPosicao(self, posicao):
        self.posicao = posicao

    def getRodadas(self):
        return self.rodadas

    def setRodadas(self, rodada):
        self.rodadas(rodada)

    def getAtivo(self):
        return self.ativo

    def setAtivo(self, ativo):
        self.ativo = ativo

    # FUNCOES DO JOGADOR
    def jogar_dado(self):
        return random.randint(1, 6)

    def conferir_saldo(self):
        if self.coins < 0:
            self.ativo = False

    def andar_tabuleiro(self):
        if self.ativo == False:
            return None
        valor_dado = self.jogar_dado()
        nova_posicao = self.posicao + valor_dado
        print(self.nome.upper() + ' SALDO = ' + str(self.getCoins()))
        print('POSICAO ANTERIOR: ' + str(self.posicao))
        print('VALOR DADO: ' + str(valor_dado))
        if nova_posicao > 20:
            self.posicao = nova_posicao - 20
            self.coins = self.coins + 100
        else:
            self.posicao = nova_posicao

        print('POSICAO ATUAL: ' + str(self.posicao)+'\n')
        return nova_posicao

    def comprar_propriedade(self, propriedade):
        if not propriedade:
            return
        # SE PROPRIEDADE ESTÁ SEM DONO E JOGADOR TEM COM SALDO
        if (not propriedade.getProprietario() and self.getCoins() >= propriedade.getVenda()):
            # PAGA PELA COMRA | PROPRIEDADE É DO JOGADOR | JOGADOR TEM A PROPRIEDADE
            self.subtraiCoins(propriedade.getVenda())
            self.setPropriedades(propriedade)
            propriedade.setProprietario(self)
            propriedade_nome = str(propriedade.getId())
            jogador_nome = self.getNome()
            print('$ $ $ ' + jogador_nome + ' COMPROU PROPRIEDADE ' +
                  propriedade_nome + ' $ $ $')

    def pagar_aluguel(self, propriedade):
        if (not propriedade or not propriedade.getProprietario()):
            return
        else:
            aluguel = propriedade.getAluguel()
            self.subtraiCoins(aluguel)
            propriedade.getProprietario().somaCoins(aluguel)
            jogador_nome = self.getNome()
            propriedade_nome = str(propriedade.getId())
            proprietario_nome = propriedade.getProprietario().getNome()
            print('! ! ! ' + jogador_nome + ' PAGOU ' + str(aluguel) + ' DE ALUGUEL PARA ' +
                  proprietario_nome + ' PROPRIEDADE ' + propriedade_nome + ' ! ! !')
            if self.getCoins() < 0:
                self.setAtivo(False)
                print('** ' + jogador_nome +
                      ' PERDEU O JOGO | SALDO: ' + str(self.getCoins()) + ' **')
