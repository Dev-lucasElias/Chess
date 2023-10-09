from classes.modelos.pecas.bispo import Bispo
from classes.modelos.pecas.cavalo import Cavalo
from classes.modelos.pecas.peao import Peao
from classes.modelos.pecas.rainha import Rainha
from classes.modelos.pecas.rei import Rei
from classes.modelos.pecas.torre import Torre
from classes.telas.tela_jogo import TelaJogo
import os
#from classes.controles.controle_central import ControleCentral

class ControleJogo():
    def __init__(self,controlador_central) -> None:
        self.__tabuleiro = self.gerar_tabuleiro()
        self.__tela_jogo = TelaJogo()
        self.__turno = 0
        self.__controlador_central = controlador_central

    @property
    def tabuleiro(self):
        return self.__tabuleiro
    
    #turno par = vez das brancas, turno impar = vez das pretas
    @property
    def turno(self):
        return self.__turno
    
    #seta o atributo posicao de cada peca no tabuleiro para sua posicao [i][j] na matriz
    #sincronizando o atributo posicao com sua posicao real no tabuleiro
    def sincronizar_posicoes_tabuleiro(self) -> None:
        for i in range(8):
            for j in range(8):
                if self.__tabuleiro[i][j] == None:
                    pass
                else:
                    self.__tabuleiro[i][j].posicao = [i,j]

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
    
    def verifica_cheque(self) -> bool:
        ameacas_rei = list()
        #verifica se as brancas estão em cheque
        if self.__turno % 2 == 0:
            for i in range(8):
                for j in range(8):
                    if self.__tabuleiro[i][j] != None:
                        if self.__tabuleiro[i][j].tipo == 'rei':
                            if self.__tabuleiro[i][j].cor == 'branco':
                                posicao_rei = self.__tabuleiro[i][j].posicao
                        else:
                            if self.__tabuleiro[i][j].cor == 'preto':
                                ameacas_rei.extend(self.__tabuleiro[i][j].possiveis_movimentos(self.tabuleiro))
            for possivel_ameaca in ameacas_rei:
                if possivel_ameaca == posicao_rei:
                    return True
            return False
        #verifica se as pretas estão em cheque
        if self.__turno % 2 != 0:
            for i in range(8):
                for j in range(8):
                    if self.__tabuleiro[i][j] != None:
                        if self.__tabuleiro[i][j].tipo == 'rei':
                            if self.__tabuleiro[i][j].cor == 'preto':
                                posicao_rei = self.__tabuleiro[i][j].posicao
                        else:
                            if self.__tabuleiro[i][j].cor == 'branco':
                                ameacas_rei.extend(self.__tabuleiro[i][j].possiveis_movimentos(self.tabuleiro))
            for possivel_ameaca in ameacas_rei:
                if possivel_ameaca == posicao_rei:
                    return True
            return False
        #if the code didnt work
        return None

    def abre_tela_jogo(self):
        while True:
            opcao_escolhida = self.__tela_jogo.mostrar_opcoes()
            if opcao_escolhida == 1:
                os.system('cls' if os.name == 'nt' else 'clear') or None
                tabuleiro = self.gerar_tabuleiro()
                self.__tela_jogo.mostrar_tabuleiro(tabuleiro)
                self.abre_tela_jogo()
                break
            elif opcao_escolhida == 2:
                os.system('cls' if os.name == 'nt' else 'clear') or None
                self.__controlador_central.inicia_programa()
                break
            else:
                print("digite uma opcao valida! ")
                os.system('cls' if os.name == 'nt' else 'clear') or None

    #metodo temporario para testar tabuleiro, o método real ficara na tela tabuleiro
    def display_tabuleiro(self):
        for row in self.__tabuleiro:
            for peca in row:
                if peca is None:
                    print('  .  ', end=' ')
                else:
                    print(f'{peca.cor[0]}{peca.tipo} ', end=' ')
            print('\n')