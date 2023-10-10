from classes.telas.tela_player import TelaPlayer
from classes.modelos.player import Player
import os

class ControlePlayer:

    def __init__(self, controlador_central):
        self.__tela_player = TelaPlayer()
        self.__lista_player = [Player]
        self.__controlador_central = controlador_central

    def adiciona_player(self):
        nome, cpf = self.__tela_player.pergunta_dados()
        self.__lista_player.append(Player(nome,cpf))
        os.system('cls' if os.name == 'nt' else 'clear') or None
        self.voltar_menu_central()

    def exclui_player(self):
        nome = self.__tela_player.pergunta_dados_excluir()
        for i, pessoa in enumerate(self.__lista_player):
            if pessoa.nome == nome:
                del self.__lista_player[i]
                break
        os.system('cls' if os.name == 'nt' else 'clear') or None
        self.voltar_menu_central()

    def voltar_menu_central(self):
        self.__controlador_central.inicia_programa()



    def abre_tela_player(self):
        while True:
            opcao_escolhida = self.__tela_player.mostrar_opcoes_iniciais()
            if opcao_escolhida == 1: #adicionar player
                os.system('cls' if os.name == 'nt' else 'clear') or None
                self.adiciona_player()
                break
            elif opcao_escolhida == 2: #excluir player
                os.system('cls' if os.name == 'nt' else 'clear') or None
                self.exclui_player()
                break
            elif opcao_escolhida == 3: #listar jogadores cadastrados
                os.system('cls' if os.name == 'nt' else 'clear') or None
                self.__tela_player.listar_jogadores(self.__lista_player)
                self.abre_tela_player()
                break
            elif opcao_escolhida == 4: #voltar ao menu anterior
                os.system('cls' if os.name == 'nt' else 'clear') or None
                self.voltar_menu_central()
            else:
                print("Opção escolhida invalida")
                os.system('cls' if os.name == 'nt' else 'clear') or None
