from classes.modelos.pecas.bispo import Bispo
from classes.modelos.pecas.cavalo import Cavalo
from classes.modelos.pecas.peao import Peao
from classes.modelos.pecas.rainha import Rainha
from classes.modelos.pecas.rei import Rei
from classes.modelos.pecas.torre import Torre
from classes.telas.tela_jogo import TelaJogo
from classes.modelos.jogo import Jogo
from classes.modelos.player import Player
#from classes.controles.controle_player import Player
import os
#from classes.controles.controle_central import ControleCentral

class ControleJogo():
    def __init__(self,controlador_central) -> None:
        self.__tabuleiro = self.gerar_tabuleiro()
        self.__tela_jogo = TelaJogo()
        self.__turno = 0
        self.__controlador_central = controlador_central
        self.__jogador_atual = None
        self.__jogo_atual = None

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

    #deve ser executado somente se verifixar_cheque retornar true
    def verifica_cheque_mate(self) -> bool:
        ameacas_rei = list()
        #verifica se as brancas tomaram cheque-mate
        if self.__turno % 2 == 0:
            for i in range(8):
                for j in range(8):
                    if self.__tabuleiro[i][j] != None:
                        if self.__tabuleiro[i][j].tipo == 'rei':
                            if self.__tabuleiro[i][j].cor == 'branco':
                                movimentos_rei = self.__tabuleiro[i][j].possiveis_movimentos(self.tabuleiro)
                        else:
                            if self.__tabuleiro[i][j].cor == 'preto':
                                ameacas_rei.extend(self.__tabuleiro[i][j].possiveis_movimentos(self.tabuleiro))
            for possivel_fuga in movimentos_rei:
                if possivel_fuga not in ameacas_rei:
                    return False
            return True
        #verifica se as pretas tomaram cheque-mate
        if self.__turno % 2 != 0:
            for i in range(8):
                for j in range(8):
                    if self.__tabuleiro[i][j] != None:
                        if self.__tabuleiro[i][j].tipo == 'rei':
                            if self.__tabuleiro[i][j].cor == 'preto':
                                movimentos_rei = self.__tabuleiro[i][j].possiveis_movimentos(self.tabuleiro)
                        else:
                            if self.__tabuleiro[i][j].cor == 'branco':
                                ameacas_rei.extend(self.__tabuleiro[i][j].possiveis_movimentos(self.tabuleiro))
            for possivel_fuga in movimentos_rei:
                if possivel_fuga not in ameacas_rei:
                    return False
            return True

    def abre_tela_jogo(self):
        possiveis_escolhas = [" Iniciar Partida"," voltar"]
        tipo_menu = "JOGADOR"
        while True:
            opcao_escolhida = self.__tela_jogo.mostrar_opcoes(possiveis_escolhas,tipo_menu)
            if opcao_escolhida == 1:
                nome_jogador = self.__tela_jogo.solicitar_jogador()
                jogador = self.__controlador_central.buscar_jogador(nome_jogador)
                tabuleiro = self.gerar_tabuleiro()
                self.__jogo_atual = Jogo(jogador,tabuleiro)
                self.__tela_jogo.mostrar_tabuleiro(self.gerar_foto_tabuleiro(tabuleiro))#---AQUIIIIII

                self.menu_jogadas()
                break
            elif opcao_escolhida == 2:
                self.__controlador_central.inicia_programa()
                break
            else:
                print("digite uma opcao valida! ")

    def gerar_foto_tabuleiro(self, tabuleiro):
        mesa = []
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        linha_superior = [f"   {letras[i]}   " for i in range(8)]
        mesa.append(linha_superior)
        for i,row in enumerate(tabuleiro):
            linha = []  
            for peca in row:
                if peca is None:
                    linha.append("   .   ")
                else:
                    if peca.tipo == "peao":
                        linha.append(str(f' {peca.cor[0]}{peca.tipo} '))
                    else:
                        linha.append(str(f'{peca.cor[0]}{peca.tipo} '))
            linha.append(f" {i+1}")
            mesa.append(linha)
        return  mesa

    def menu_jogadas(self):
        possiveis_escolhas = [" Jogar"," Desistir da partida"]
        tipo_menu = "JOGADAS"
        while True:
            opcao_escolhida = self.__tela_jogo.mostrar_opcoes(possiveis_escolhas,tipo_menu)
            if opcao_escolhida == 1: 
                posicao_escolhida = self.__tela_jogo.solicitar_posicao_inicial()
                #continuar depois. AJUSTAR PRIMEIRO A CLASSE PARTIDA
                break
            elif opcao_escolhida == 2:
                #Desistir da partida partida
                break
            else:
                print("digite uma opcao valida! ")