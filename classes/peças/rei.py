from peca import Peca

class Rei(Peca):
    def __init__(self, cor: str, posicao: list) -> None:
        super().__init__(cor, posicao)
        self.__tipo = 'rei'

    def possiveis_movimentos(self) -> list:
        casas = 1
        tabuleiro = controle_jogo.tabuleiro()
        x = self.posicao[0]
        y = self.posicao[1]
        movimentos = list()
        movimentos.extend(self.mover_diagonal_inferior_direita(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_diagonal_superior_direita(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_diagonal_inferior_esquerda(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_diagonal_superior_esquerda(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_reto_baixo(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_reto_cima(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_reto_esquerda(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_reto_direita(casas, tabuleiro, x, y))
        return movimentos