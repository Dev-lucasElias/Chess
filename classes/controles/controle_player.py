from classes.telas.tela_player import TelaPlayer
from classes.modelos.player import Player
from classes.controles.controle_central import ControleCentral


class ControlePlayer:

    def __init__(self, controlador_central: ControleCentral):
        self.__tela_player = TelaPlayer()
        self.__lista_player = [Player]
        self.__controlador_central = controlador_central

    def adiciona_player(self):
        nome, cpf = self.__tela_player.pergunta_dados()
        self.__lista_player.append(Player(nome,cpf))

    def exclui_player(self):
        nome = self.__tela_player.pergunta_dados_excluir()
        ##-----REMOVER PLAYER DA LISTA---------


    def abre_tela_player(self):
        while True:
            opcao_escolhida = self.__tela_player.mostra_opcoes()
            if opcao_escolhida == 1: #adicionar player
                self.adiciona_player()
                break
            elif opcao_escolhida == 2: #excluir player
                self.exclui_player()
                break
            elif opcao_escolhida == 3: #voltar ao menu anterior
                self.__controlador_central.inicia_programa()
            else:
                print("Opção escolhida invalida")
