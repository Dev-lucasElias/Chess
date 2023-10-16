
from classes.controles.controle_jogo import ControleJogo
from classes.controles.controle_player import ControlePlayer
from classes.telas.tela_central import TelaCentral
from classes.telas.tela_regras import TelaRegras
import time

class ControleCentral:
    def __init__(self):
        self.__controle_player = ControlePlayer(self)
        self.__controle_jogo = ControleJogo(self)
        self.__tela_regras = TelaRegras(self)
        self.__tela_central = TelaCentral()

    def chama_controlador_player(self):
        self.__controle_player.abre_tela_player()

    def chama_controlador_tabuleiro(self):
        self.__controle_jogo.abre_tela_jogo()
    
    def buscar_jogador(self,nome_jogador):
        jogador = self.__controle_player.consultar_jogador(nome_jogador)
        return jogador

    def inicia_programa(self):
        possiveis_escolhas = [" Menu Jogador"," Menu Partida", " Menu Regras"]
        tipo_menu = "CENTRAL"
        while True:
            self.__tela_central.limpar_tela()
            opcao_escolhida = self.__tela_central.mostrar_opcoes(possiveis_escolhas,tipo_menu, True)
            if opcao_escolhida == 1:
                self.chama_controlador_player()
                break
            elif opcao_escolhida == 2:
                self.chama_controlador_tabuleiro()
                break
            elif opcao_escolhida == 3:
                self.__tela_regras.mostrar_regras()
                break
            else:
                print("Opção invalida")
                time.sleep(1.5)

            

