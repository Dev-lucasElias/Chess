
from classes.controles.controle_jogo import ControleJogo
from classes.controles.controle_player import ControlePlayer
from classes.telas.tela_central import TelaCentral


class ControleCentral:
    def __init__(self):
        self.__controle_player = ControlePlayer(self)
        self.__controle_jogo = ControleJogo(self)
        self.__tela_central = TelaCentral()

    def chama_controlador_player(self):
        self.__controle_player.abre_tela_player()

    def chama_controlador_tabuleiro(self):
        self.__controle_jogo.abre_tela_jogo()
    
    def buscar_jogador(self,nome_jogador):
        jogador = self.__controle_player.consultar_jogador(nome_jogador)
        return jogador

    def inicia_programa(self):
        possiveis_escolhas = [" Menu Jogador"," Menu Partida"]
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
            else:
                print("digite a opcao correta!")

            

