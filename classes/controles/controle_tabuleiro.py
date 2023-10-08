from modelos.pecas.bispo import Bispo
from modelos.pecas.cavalo import Cavalo
from modelos.pecas.peao import Peao
from modelos.pecas.rainha import Rainha
from modelos.pecas.rei import Rei
from modelos.pecas.torre import Torre
from classes.telas.tela_jogo import TelaJogo
from classes.controles.controle_central import ControleCentral

class ControleTabuleiro():
    def __init__(self, controlador_central : ControleCentral) -> None:
        self.__tabuleiro = self.gerar_tabuleiro()
        self.__tela_jogo = TelaJogo()
        self.__controlador_central = controlador_central

    @property
    def tabuleiro(self):
        return self.__tabuleiro

    def abre_tela_jogo(self):
        while True:
            opcao_escolhida = self.__tela_jogo.mostrar_opcoes()
            if opcao_escolhida == 1:
                self.gerar_tabuleiro()
                break
            elif opcao_escolhida == 2:
                self.__controlador_central.inicia_programa()
                break
            else:
                print("digite uma opcao valida! ")

    def gerar_tabuleiro(self):
        tabuleiro = [[None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None],
                    [None, None, None, None, None, None, None, None]]

        #posiciona as pecas brancas
        tabuleiro[7][0] = Torre('branco', [7, 0])
        tabuleiro[7][1] = Cavalo('branco', [7, 1])
        tabuleiro[7][2] = Bispo('branco', [7, 2])
        tabuleiro[7][3] = Rainha('branco', [7, 3])
        tabuleiro[7][4] = Rei('branco', [7, 4])
        tabuleiro[7][5] = Bispo('branco', [7, 5])
        tabuleiro[7][6] = Cavalo('branco', [7, 6])
        tabuleiro[7][7] = Torre('branco', [7, 7])
        for i in range(8):
            tabuleiro[6][i] = Peao('branco', [6, i])
    
        #posiciona as pecas pretas
        tabuleiro[0][0] = Torre('preto', [0, 0])
        tabuleiro[0][1] = Cavalo('preto', [0, 1])
        tabuleiro[0][2] = Bispo('preto', [0, 2])
        tabuleiro[0][3] = Rainha('preto', [0, 3])
        tabuleiro[0][4] = Rei('preto', [0, 4])
        tabuleiro[0][5] = Bispo('preto', [0, 5])
        tabuleiro[0][6] = Cavalo('preto', [0, 6])
        tabuleiro[0][7] = Torre('preto', [0, 7])
        for i in range(8):
            tabuleiro[1][i] = Peao('preto', [1, i])

        return tabuleiro

    def display_tabuleiro(self):
        for row in self.__tabuleiro:
            for peca in row:
                if peca is None:
                    print('  .  ', end=' ')
                else:
                    print(f'{peca.cor[0]}{peca.tipo} ', end=' ')
            print('\n')