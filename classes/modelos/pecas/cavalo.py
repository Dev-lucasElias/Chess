from classes.modelos.pecas.peca import Peca

class Cavalo(Peca):
    def __init__(self, cor: str, posicao: list) -> None:
        super().__init__(cor, posicao)
        self.__tipo = 'cavalo'

    @property
    def tipo(self) -> str:
        return self.__tipo

    def mover_cima1_cavalo(self, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        x -= 1
        y -= 2
        if (x < 0) or (y < 0):
            return movimentos
        if tabuleiro[x][y] == None:
            movimentos.append([x,y])
            return movimentos
        else:
            if tabuleiro[x][y].cor != self.cor:
                movimentos.append([x,y])
                return movimentos
        return movimentos

    def mover_cima2_cavalo(self, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        x += 1
        y -= 2
        if (x > 7) or (y < 0):
            return movimentos
        if tabuleiro[x][y] == None:
            movimentos.append([x,y])
            return movimentos
        else:
            if tabuleiro[x][y].cor != self.cor:
                movimentos.append([x,y])
                return movimentos
        return movimentos

    def mover_baixo1_cavalo(self, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        x -= 1
        y += 2
        if (x < 0) or (y > 7):
            return movimentos
        if tabuleiro[x][y] == None:
            movimentos.append([x,y])
            return movimentos
        else:
            if tabuleiro[x][y].cor != self.cor:
                movimentos.append([x,y])
                return movimentos
        return movimentos

    def mover_baixo2_cavalo(self, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        x += 1
        y += 2
        if (x > 7) or (y > 7):
            return movimentos
        if tabuleiro[x][y] == None:
            movimentos.append([x,y])
            return movimentos
        else:
            if tabuleiro[x][y].cor != self.cor:
                movimentos.append([x,y])
                return movimentos
        return movimentos

    def mover_esqueda1_cavalo(self, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        x -= 2
        y -= 1
        if (x < 0) or (y < 0):
            return movimentos
        if tabuleiro[x][y] == None:
            movimentos.append([x,y])
            return movimentos
        else:
            if tabuleiro[x][y].cor != self.cor:
                movimentos.append([x,y])
                return movimentos
        return movimentos

    def mover_esqueda2_cavalo(self, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        x -= 2
        y += 1
        if (x < 0) or (y > 7):
            return movimentos
        if tabuleiro[x][y] == None:
            movimentos.append([x,y])
            return movimentos
        else:
            if tabuleiro[x][y].cor != self.cor:
                movimentos.append([x,y])
                return movimentos
        return movimentos

    def mover_direita1_cavalo(self, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        x += 2
        y -= 1
        if (x > 7) or (y < 0):
            return movimentos
        if tabuleiro[x][y] == None:
            movimentos.append([x,y])
            return movimentos
        else:
            if tabuleiro[x][y].cor != self.cor:
                movimentos.append([x,y])
                return movimentos
        return movimentos

    def mover_direita2_cavalo(self, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        x += 2
        y += 1
        if (x > 7) or (y > 7):
            return movimentos
        if tabuleiro[x][y] == None:
            movimentos.append([x,y])
            return movimentos
        else:
            if tabuleiro[x][y].cor != self.cor:
                movimentos.append([x,y])
                return movimentos
        return movimentos

    def possiveis_movimentos(self, tabuleiro_parametro: list) -> list:
        tabuleiro = tabuleiro_parametro
        x = self.posicao[0]
        y = self.posicao[1]
        movimentos = list()
        movimentos.extend(self.mover_cima1_cavalo(tabuleiro, x, y))
        movimentos.extend(self.mover_cima2_cavalo(tabuleiro, x, y))
        movimentos.extend(self.mover_baixo1_cavalo(tabuleiro, x, y))
        movimentos.extend(self.mover_baixo2_cavalo(tabuleiro, x, y))
        movimentos.extend(self.mover_esquerda1_cavalo(tabuleiro, x, y))
        movimentos.extend(self.mover_esquerda2_cavalo(tabuleiro, x, y))
        movimentos.extend(self.mover_direita1_cavalo(tabuleiro, x, y))
        movimentos.extend(self.mover_direita2_cavalo(tabuleiro, x, y))
        return movimentos