class Jogada:
    def __init__(self,jogador,peca, posicao_inical, posicao_final, resultado_tabuleiro, turno_jogada) -> None:
        self.__jogador = jogador
        self.__peca = peca
        self.__posicao_inicial = posicao_inical #self.transforma_posicao_em_letra(posicao_inical)
        self.__posicao_final =posicao_final# self.transforma_posicao_em_letra(posicao_final)
        self.__resultado_tabuleiro = resultado_tabuleiro
        self.__turno_jogada = turno_jogada

    @property
    def jogador(self):
        return self.__jogador
    @property
    def peca(self):
        return self.__peca
    @property
    def posicao_inicial(self):
        return self.__posicao_inicial
    @property
    def posicao_final(self):
        return self.__posicao_final
    @property
    def resultado_tabuleiro(self):
        return self.__resultado_tabuleiro
    @property
    def turno_jogada(self):
        return self.__turno_jogada
    
    def transforma_posicao_em_letra(self,posicao):
        posicao_tratada = posicao
        if posicao[0] == 0:
            posicao_tratada[0] = "a"
        elif posicao[0] == 1:
            posicao_tratada[0] = "b"
        elif posicao[0] == 2:
            posicao_tratada[0] = "c"
        elif posicao[0] == 3:
            posicao_tratada[0] = "d"
        elif posicao[0] == 4:
            posicao_tratada[0] = "e"
        elif posicao[0] == 5:
            posicao_tratada[0] = "f"
        elif posicao[0] == 6:
            posicao_tratada[0] = "g"
        elif posicao[0] == 7:
            posicao_tratada[0] = "h"
        posicao_tratada[1] = str(posicao[1])
        posicao_tratada_final = posicao_tratada[0]+posicao_tratada[1]
        return posicao_tratada_final
