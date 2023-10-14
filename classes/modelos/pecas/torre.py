from classes.modelos.pecas.peca import Peca

class Torre(Peca):
    def __init__(self, cor: str, posicao: list) -> None:
        super().__init__(cor, posicao)
        self.__tipo = 'TORRE '

    @property
    def tipo(self) -> str:
        return self.__tipo

    def possiveis_movimentos(self, tabuleiro_parametro: list) -> list:
        casas = 7
        tabuleiro = tabuleiro_parametro
        x = self.posicao[0]
        y = self.posicao[1]
        movimentos = list()
        movimentos.extend(self.mover_reto_baixo(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_reto_cima(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_reto_esquerda(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_reto_direita(casas, tabuleiro, x, y))
        return movimentos