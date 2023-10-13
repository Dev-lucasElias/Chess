from classes.modelos.jogada import Jogada

class Jogo:

    def __init__(self, jogador_partida, tabuleiro) -> None:
        self.__jogador_partida = jogador_partida
        self.__turno_atual = 0
        self.__historico_jogadas = []
        self.__resultado_tabuleiro = tabuleiro

    @property
    def resultado_tabuleiro(self) -> list:
        return self.__resultado_tabuleiro
	
    @resultado_tabuleiro.setter
    def resultado_tabuleiro(self, resultado_tabuleiro) -> None:
        if isinstance(resultado_tabuleiro, list):
            self.__resultado_tabuleiro = resultado_tabuleiro
    
    #turno par = vez das brancas, turno impar = vez das pretas
    @property
    def turno_atual(self) -> int:
        return self.__turno_atual
    
    @turno_atual.setter
    def turno_atual(self, turno_atual) -> None:
        if isinstance(turno_atual, int):
            self.__turno_atual = turno_atual

    def registra_jogada(self, jogador,peca, posicao_inical, posicao_final, resultado_tabuleiro):
        jogada = Jogada(jogador, peca, posicao_inical, posicao_final, resultado_tabuleiro, self.__turno_atual)
        self.__historico_jogadas.append(jogada)
        self.__turno_atual += 1
        self.resultado_tabuleiro = resultado_tabuleiro
