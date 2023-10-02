from abc import ABC, abstractmethod


class Peca(ABC):
    @abstractmethod
    def __init__(self, cor, tipo, posicao) -> None:
        pass

    @abstractmethod
    def possiveis_movimentos(self) -> list:
        pass

    def limite(self, valor) -> None:
        pass

    def mover_lado_cima(self, casas) -> None:
        pass

    def mover_lado_baixo(self, casas) -> None:
        pass

    def mover_lado_esquerda(self, casas) -> None:
        pass

    def mover_lado_direita(self, casas) -> None:
        pass

    def mover_diagonal_esquerda_cima(self, casas) -> None:
        pass

    def mover_diagonal_esquerda_baixo(self, casas) -> None:
        pass

    def mover_diagonal_direita_cima(self, casas) -> None:
        pass

    def mover_diagonal_direita_baixo(self, casas) -> None:
        pass