from funcoes import *


def jogar(RODADAS_MAXIMAS):
    try:
        [jogadores, propriedades] = inicializacao()
    except:
        fechar_jogo()
    contador_turnos = 1
    jogadores_ativos = jogadores
    while contador_turnos < RODADAS_MAXIMAS:
        print_status(contador_turnos, jogadores)
        for i in jogadores:
            # turno pode retornar id de propriedades que devem ser liberadas
            if i.getAtivo() == True:
                turno(i, propriedades)
                # print('********\n\n')
            else:
                jogadores_ativos.remove(i)
                if len(jogadores_ativos) == 1:
                    RODADAS_MAXIMAS = 0
                    print(' @@@@@ JOGO ACABOU @@@@@@')
                    return jogadores_ativos[0]
        contador_turnos += 1
    return define_vencedor(jogadores)

    print('\n\n\n****** ENCERROU ******\n\n\n')
    for p in propriedades:
        print('PROPRIEDADE ' + str(p.getId()))
        if (not p.getProprietario()):
            print('VAZIA')
        else:
            print(p.getProprietario().getNome())


vencedores = []
i = 0
while i < 500:
    vencedores.append(jogar(RODADAS_MAXIMAS).getNome())
    i += 1

win = {x: vencedores.count(x) for x in vencedores}
print(win)
# for v in vencedores:
#    if v == None:
#        print('Vazio')
#    else:
#        print(v.getNome())


#   __TO_DO__
# - TODOS OS COMPORTAMENTOS
# - SALDO NEGATIVO -> SOMENTE PARA ALUGUEL  *DONE!*
# - SALDO NEGATIVO = DERROTA DO JOGADOR     *DONE!*
# - DERROTA -> LIBERAR PROPRIEDADES COMPRADAS CASO TENHA *DONE!*
# - VITORIA:
#   -- MAIS DE 1000 RODADAS
#   -- VENCE QUEM TEM MAIS COINS
#   -- EM EMPATE, VENCE QUEM JOGAR PRIMEIRO NA ORDEM
# - README


# contador_turnos = 1
# while contador_turnos <= ROADAS_MAXIMAS:
#    print('*** TURNO ' + str(contador_turnos) + ' ***')
#    for jogador in jogadores:
#        confere_jogadores_ativos
#        turno(jogador, propriedades)
#    contador_turnos += 1
