from modelos.jogada import Jogada

class Jogo:

    def __init__(self, jogador_partida) -> None:
        self.__jogador_partida = jogador_partida
        self.__turnoAtual = None
        self.__historico_jogadas = []

    def registra_jogada(self, jogador,peca, posicao_inical, posicao_final):
        jogada = Jogada(jogador, peca, posicao_inical, posicao_final)
        self.__historico_jogadas.append(jogada)