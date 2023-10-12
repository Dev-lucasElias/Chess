from classes.modelos.jogada import Jogada

class Jogo:

    def __init__(self, jogador_partida, tabuleiro) -> None:
        self.__jogador_partida = jogador_partida
        self.__turnoAtual = 0
        self.__historico_jogadas = []
        self.__resultado_tabuleiro = tabuleiro

    @property
    def resultado_tabuleiro(self) -> list:
        return self.__resultado_tabuleiro
	
    @resultado_tabuleiro.setter
    def resultado_tabuleiro(self, resultado_tabuleiro) -> None:
        if isinstance(resultado_tabuleiro, list):
            self.__resultado_tabuleiro = resultado_tabuleiro

    def registra_jogada(self, jogador,peca, posicao_inical, posicao_final, resultado_tabuleiro):
        jogada = Jogada(jogador, peca, posicao_inical, posicao_final, resultado_tabuleiro)
        self.__historico_jogadas.append(jogada)
        self.__turnoAtual += 1
        self.resultado_tabuleiro = resultado_tabuleiro