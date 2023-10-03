from abc import ABC, abstractmethod


class Peca(ABC):
    @abstractmethod
    def __init__(self, cor: str, posicao: list) -> None:
        if cor == 'branca' or cor == 'preta':
            self.__cor = cor
        else:
            raise ValueError('A cor deve ser preta ou branca')
        if (
            isinstance(posicao, list) and
            len(posicao) == 2 and
            all(0 <= item <= 7 and isinstance(item, int) for item in posicao)
        ):
            self.__posicao = posicao
        else:
            raise ValueError('A posição deve ser uma lista com dois inteiros entre 0 e 7')
        self.__x = self.__posicao[0]
        self.__y = self.__posicao[1]


    @abstractmethod
    def possiveis_movimentos(self) -> list:
        movimentos = list()
        #extend list
        return movimentos
    
    @property
    def cor(self):
        return self.__cor
    
    @property
    def posicao(self):
        return self.__posicao
    @posicao.setter
    def posicao(self, posicao: list):
        if (
            isinstance(posicao, list) and
            len(posicao) == 2 and
            all(0 <= item <= 7 and isinstance(item, int) for item in posicao)
        ):
            self.__posicao = posicao
        else:
            raise ValueError('A posição deve ser uma lista com dois inteiros entre 0 e 7')


    def mover_reto_cima(self, casas) -> None:
        tabuleiro = get_tabuleiro()
        movimentos = list()
        x = self.__x
        y = self.__y
        for _ in range(casas):
            y -= 1
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

    def mover_reto_baixo(self, casas) -> None:
        tabuleiro = get_tabuleiro()
        movimentos = list()
        x = self.__x
        y = self.__y
        for _ in range(casas):
            y += 1
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

    def mover_reto_esquerda(self, casas) -> None:
        tabuleiro = get_tabuleiro()
        movimentos = list()
        x = self.__x
        y = self.__y
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

    def mover_reto_direita(self, casas) -> None:
        tabuleiro = get_tabuleiro()
        movimentos = list()
        x = self.__x
        y = self.__y
        for _ in range(casas):
            x += 1
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

    def mover_diagonal_esquerda_cima(self, casas) -> None:
        pass

    def mover_diagonal_esquerda_baixo(self, casas) -> None:
        pass

    def mover_diagonal_direita_cima(self, casas) -> None:
        pass

    def mover_diagonal_direita_baixo(self, casas) -> None:
        pass