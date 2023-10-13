class Jogada:
    def __init__(self,jogador,peca, posicao_inical, posicao_final, resultado_tabuleiro, turno_jogada) -> None:
        self.__jogador = jogador
        self.__peca = peca
        self.__posicao_inicial = posicao_inical
        self.__posicao_final = posicao_final
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
