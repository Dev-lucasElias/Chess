from classes.telas.tela_player import TelaPlayer
from classes.modelos.player import Player

class ControlePlayer:

    def __init__(self, controlador_central):
        self.__tela_player = TelaPlayer()
        self.__lista_player = []
        self.__controlador_central = controlador_central

    def adiciona_player(self):
        nome, cpf = self.__tela_player.pergunta_dados()
        self.__lista_player.append(Player(nome,cpf))
        self.voltar_menu_central()

    def exclui_player(self):
        nome = self.__tela_player.pergunta_dados_excluir()
        for i, pessoa in enumerate(self.__lista_player):
            if pessoa.nome == nome:
                del self.__lista_player[i]
                break
        self.voltar_menu_central()

    def voltar_menu_central(self):
        self.__controlador_central.inicia_programa()



    def abre_tela_player(self):
        possiveis_escolhas = [" Adicionar jogador"," Remover jogador", " Listar jogador", " Voltara ao menu anterior"]
        tipo_menu =  "JOGADOR"
        while True:
            opcao_escolhida = self.__tela_player.mostrar_opcoes(possiveis_escolhas,tipo_menu)
            if opcao_escolhida == 1: #adicionar player
                self.adiciona_player()
                break
            elif opcao_escolhida == 2: #excluir player
                self.exclui_player()
                break
            elif opcao_escolhida == 3: #listar jogadores cadastrados
                self.__tela_player.listar_jogadores(self.__lista_player)
                self.abre_tela_player()
                break
            elif opcao_escolhida == 4: #voltar ao menu anterior
                self.voltar_menu_central()
            else:
                print("Opção escolhida invalida")
