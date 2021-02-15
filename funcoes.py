import time
import os
import sys
from constantes import *
from propriedade import *
from jogador import *
from datetime import datetime


def inicializacao():
    arquivo_configuracao = open(CAMINHO_ARQUIVO_CONFIG, 'r')
    propriedades = carregar_propriedades(arquivo_configuracao)
    p1 = Jogador(1, COMPORTAMENTO_1, True)
    p2 = Jogador(2, COMPORTAMENTO_2, True)
    p3 = Jogador(3, COMPORTAMENTO_3, True)
    p4 = Jogador(4, COMPORTAMENTO_4, True)
    jogadores = sorteio_ordem_jogadores([p1, p2, p3, p4])
    return [jogadores, propriedades]


def fechar_jogo():
    print('Erro ao iniciar o jogo.\nObs: ~Bankrupt/gameConfig.txt')
    time.sleep(5)
    sys.exit()


def carregar_propriedades(arquivo_configuracao):
    contador = 1
    posicao = contador
    config = []
    for linha in arquivo_configuracao:
        config.append(
            Propriedade(
                contador,
                linha.split()[0],
                linha.split()[1],
                None,
                posicao
            )
        )
        contador = contador + 1
        posicao = contador
    return config


def sorteio_ordem_jogadores(jogadores):
    quantidade_jogadores = len(jogadores)
    lista_sorteada = []
    log = 'ORDEM DOS JOGADORES NOS TURNOS: '
    while len(lista_sorteada) < quantidade_jogadores:
        lista_sorteada.append(random.choice(jogadores))
        log += ' ' + lista_sorteada[-1].getNome() + ' '
        jogadores.remove(lista_sorteada[-1])
    print(log)
    return lista_sorteada


def print_status(count, jogadores):
    players = []
    #print(' * RODADA ' + str(count) + ' *  \n')
    # for b in jogadores:
    #    if b.getAtivo():
    #print('J ATIVOS: ' + b.getNome())
    # print('\n')


def comprar_ou_pagar_aluguel(jogador, propriedade):
    # PROPRIEDADE SEM DONO
    if (not propriedade.getProprietario()):
        decisao_compra(jogador, propriedade)
    # PROPRIEDADE DO PROPRIO JOGADOR
    elif (propriedade.getProprietario() == jogador):
        return
    # PROPRIEDADE TEM DONO E NÃO É DO PROPRIO JOGADOR
    else:
        jogador.pagar_aluguel(propriedade)


def decisao_compra(jogador, propriedade):
    comportamento = jogador.getComportamento()
    if comportamento == COMPORTAMENTO_1:
        jogador.comprar_propriedade(propriedade)
    elif comportamento == COMPORTAMENTO_2:
        if propriedade.getAluguel() > 50:
            jogador.comprar_propriedade(propriedade)
        else:
            return
    elif comportamento == COMPORTAMENTO_3:
        if (jogador.getCoins() - propriedade.getAluguel() >= 80):
            jogador.comprar_propriedade(propriedade)
        else:
            return
    else:
        # BOOLEANO RANDOMICO
        if (bool(random.getrandbits(1))):
            jogador.comprar_propriedade(propriedade)
        else:
            return


def define_vencedor(jogadores):
    saldo_coin = 0
    for j in jogadores:
        if j.getAtivo() == True:
            if j.getCoins() > saldo_coin:
                saldo_coin = j.getCoins()
                vencedor = j
    print('@@@@ VENCEDOR : ' + vencedor.getNome() + '  @@@@')
    return vencedor


def turno(jogador, propriedades):
    jogador.andar_tabuleiro()
    # new
    #pIndex = jogador.getPosicao() - 1
    #comprar_ou_pagar_aluguel(jogador, propriedades[pIndex])
    # if (jogador.getAtivo() == False):
    #    for p in propriedades:
    #        if (p.getProprietario() == jogador):
    #            jogador.perdeu_jogo()
    for p in propriedades:
        if (p.getPosicao() == jogador.getPosicao()):
            comprar_ou_pagar_aluguel(jogador, p)
