from classes.controles import tabuleiro_controle
from classes.controles import playerControlador


class ControleCentral:
    def __init__(self):
        self.__controle_player = ControlePlayer(self)

