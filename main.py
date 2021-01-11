from funcoes import *

try:
    [jogadores, propriedades] = inicializacao()
except:
    fechar_jogo()
count = 1
while count < 50:
    players = []
    print(' * RODADA ' + str(count) + ' *  \n')
    for b in jogadores:
        if b.getAtivo():
            print('J ATIVOS: ' + b.getNome())
    for i in jogadores:
        turno(i, propriedades)
    print('********\n\n')
    count += 1


#   __TO_DO__
# - TODOS OS COMPORTAMENTOS
# - SALDO NEGATIVO -> SOMENTE PARA ALUGUEL
# - SALDO NEGATIVO = DERROTA DO JOGADOR
# - DERROTA -> LIBERAR PROPRIEDADES COMPRADAS CASO TENHA
# - VITORIA:
#   -- MAIS DE 1000 RODADAS
#   -- VENCE QUEM TEM MAIS COINS
#   -- EM EMPATE, VENCE QUEM JOGAR PRIMEIRO NA ORDEM
# - README


#contador_turnos = 1
# while contador_turnos <= ROADAS_MAXIMAS:
#    print('*** TURNO ' + str(contador_turnos) + ' ***')
#    for jogador in jogadores:
#        confere_jogadores_ativos
#        turno(jogador, propriedades)
#    contador_turnos += 1
