from classes.modelos.pecas.peca import Peca

class Bispo(Peca):
    def __init__(self, cor: str, posicao: list) -> None:
        super().__init__(cor, posicao)
        self.__tipo = 'bispo'

    @property
    def tipo(self) -> str:
        return self.__tipo

    def possiveis_movimentos(self, tabuleiro_parametro: list) -> list:
        casas = 7
        tabuleiro = tabuleiro_parametro
        x = self.posicao[0]
        y = self.posicao[1]
        movimentos = list()
        movimentos.extend(self.mover_diagonal_inferior_direita(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_diagonal_superior_direita(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_diagonal_inferior_esquerda(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_diagonal_superior_esquerda(casas, tabuleiro, x, y))
        return movimentos