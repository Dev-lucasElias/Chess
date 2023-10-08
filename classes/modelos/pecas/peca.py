from abc import ABC, abstractmethod

class Peca(ABC):
    @abstractmethod
    def __init__(self, cor: str, posicao: list) -> None:
        if cor == 'branco' or cor == 'preto':
            self.__cor = cor
        else:
            raise ValueError('A cor deve ser preto ou branco')
        if (
            isinstance(posicao, list) and
            len(posicao) == 2 and
            all(0 <= item <= 7 and isinstance(item, int) for item in posicao)
        ):
            self.__posicao = posicao
        else:
            raise ValueError('A posição deve ser uma lista com dois inteiros entre 0 e 7')
        self.__tipo = None

    @abstractmethod
    def possiveis_movimentos(self) -> list:
        #movimentos = list()
        #x = self.__posicao[0]
        #y = self.__posicao[1]
        #extend list
        #return movimentos
        pass
    
    @property
    def cor(self) -> str:
        return self.__cor
    
    @abstractmethod
    def tipo(self) -> str:
        pass
    
    @property
    def posicao(self) -> list:
        return self.__posicao
    @posicao.setter
    def posicao(self, posicao: list) -> None:
        if (
            isinstance(posicao, list) and
            len(posicao) == 2 and
            all(0 <= item <= 7 and isinstance(item, int) for item in posicao)
        ):
            self.__posicao = posicao
        else:
            raise ValueError('A posição deve ser uma lista com dois inteiros entre 0 e 7')


    def mover_reto_cima(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            y -= 1
            if y < 0:
                return movimentos
            if tabuleiro[x][y] == None:
                movimentos.append([x,y])
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos

    def mover_reto_baixo(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            y += 1
            if y > 7:
                return movimentos
            if tabuleiro[x][y] == None:
                movimentos.append([x,y])
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos

    def mover_reto_esquerda(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            x -= 1
            if x < 0:
                return movimentos
            if tabuleiro[x][y] == None:
                movimentos.append([x,y])
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos

    def mover_reto_direita(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            x += 1
            if x > 7:
                return movimentos
            if tabuleiro[x][y] == None:
                movimentos.append([x,y])
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos

    def mover_diagonal_superior_esquerda(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            x -= 1
            y -= 1
            if (x < 0) or (y < 0):
                return movimentos
            if tabuleiro[x][y] == None:
                movimentos.append([x,y])
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos

    def mover_diagonal_inferior_esquerda(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            x -= 1
            y += 1
            if (x < 0) or (y > 7):
                return movimentos
            if tabuleiro[x][y] == None:
                movimentos.append([x,y])
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos

    def mover_diagonal_superior_direita(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            x += 1
            y -= 1
            if (x > 7) or (y < 0):
                return movimentos
            if tabuleiro[x][y] == None:
                movimentos.append([x,y])
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos

    def mover_diagonal_inferior_direita(self, casas: int, tabuleiro_parametro: list, x_parametro: int, y_parametro: int) -> list:
        tabuleiro = tabuleiro_parametro
        movimentos = list()
        x = x_parametro
        y = y_parametro
        for _ in range(casas):
            x += 1
            y += 1
            if (x > 7) or (y > 7):
                return movimentos
            if tabuleiro[x][y] == None:
                movimentos.append([x,y])
            else:
                if tabuleiro[x][y].cor != self.cor:
                    movimentos.append([x,y])
                    return movimentos
                return movimentos
        return movimentos