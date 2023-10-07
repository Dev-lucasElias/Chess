from classes.controles.controle_tabuleiro import ControleTabuleiro
from classes.controles.controle_player import ControlePlayer
from classes.telas.tela_central import TelaCentral


class ControleCentral:
    def __init__(self):
        self.__controle_player = ControlePlayer()
        self.__controle_tabuleiro = ControleTabuleiro()
        self.__tela_central = TelaCentral()


