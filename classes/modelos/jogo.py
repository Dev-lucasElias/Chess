from classes.modelos.jogada import Jogada

class Jogo:

    def __init__(self, jogador_partida, tabuleiro) -> None:
        self.__jogador_partida = jogador_partida
        self.__turnoAtual = 0
        self.__historico_jogadas = []
        self.__resultado_tabuleiro = tabuleiro

    def registra_jogada(self, jogador,peca, posicao_inical, posicao_final):
        jogada = Jogada(jogador, peca, posicao_inical, posicao_final)
        self.__historico_jogadas.append(jogada)