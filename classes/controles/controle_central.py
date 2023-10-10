
from classes.controles.controle_jogo import ControleJogo
from classes.controles.controle_player import ControlePlayer
from classes.telas.tela_central import TelaCentral
import os


class ControleCentral:
    def __init__(self):
        self.__controle_player = ControlePlayer(self)
        self.__controle_jogo = ControleJogo(self)
        self.__tela_central = TelaCentral()

    def chama_controlador_player(self):
        self.__controle_player.abre_tela_player()

    def chama_controlador_tabuleiro(self):
        self.__controle_jogo.abre_tela_jogo()

    def inicia_programa(self):
        while True:
            opcao_escolhida = self.__tela_central.mostrar_opcoes_iniciais()
            if opcao_escolhida == 1:
                os.system('cls' if os.name == 'nt' else 'clear') or None
                self.chama_controlador_player()
                break
            elif opcao_escolhida == 2:
                os.system('cls' if os.name == 'nt' else 'clear') or None
                self.chama_controlador_tabuleiro()
                break
            else:
                print("digite a opcao correta!")
                os.system('cls' if os.name == 'nt' else 'clear') or None

            

