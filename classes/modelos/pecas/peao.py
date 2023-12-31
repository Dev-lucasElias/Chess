from classes.modelos.pecas.peca import Peca

class Peao(Peca):
    def __init__(self, cor: str, posicao: list) -> None:
        super().__init__(cor, posicao)
        self.__tipo = 'PEAO'

    @property
    def tipo(self) -> str:
        return self.__tipo

    def mover_cima_peao(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            if self.cor == 'branco':
                x -= 1
            elif self.cor == 'preto':
                x += 1
            if (x < 0) or (x > 7):
                return movimentos
            if tabuleiro[x][y] == None:
                movimentos.append([x,y])
            else:
                return movimentos
        return movimentos
    
    def mover_diagonal_esquerda_peao(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            y -= 1
            if self.cor == 'branco':
                x -= 1
            elif self.cor == 'preto':
                x += 1
            if (y < 0) or (x < 0) or (x > 7) or (y > 7):
                return movimentos
            if tabuleiro[x][y] == None:
                return movimentos
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos

    def mover_diagonal_direita_peao(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            y += 1
            if self.cor == 'branco':
                x -= 1
            elif self.cor == 'preto':
                x += 1
            if (y < 0) or (x < 0) or (x > 7) or (y > 7):
                return movimentos
            if tabuleiro[x][y] == None:
                return movimentos
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos

    def possiveis_movimentos(self, tabuleiro_parametro: list) -> list:
        casas = 1
        tabuleiro = tabuleiro_parametro
        x = self.posicao[0]
        y = self.posicao[1]
        movimentos = list()
        movimentos.extend(self.mover_cima_peao(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_diagonal_esquerda_peao(casas, tabuleiro, x, y))
        movimentos.extend(self.mover_diagonal_direita_peao(casas, tabuleiro, x, y))

        return movimentos