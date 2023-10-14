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
import random
import time
#from classes.controles.controle_central import ControleCentral

class ControleJogo():
    def __init__(self,controlador_central) -> None:
        self.__tabuleiro = self.gerar_tabuleiro()
        self.__tela_jogo = TelaJogo()
        self.__controlador_central = controlador_central
        self.__jogador_1 = Player(None,None)
        self.__jogador_2 = Player(None,None)
        self.__jogo_atual = Player(None,None)
        self.__bot_preto = Player("BOT_preto", "000000000")
        self.__historico_partidas = []
        self.__bot_branco = Player("BOT_Branco", "999999999")

    @property
    def tabuleiro(self):
        return self.__tabuleiro
    
    
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
        posicao_rei = None
        #verifica se as brancas estão em cheque
        if self.__jogo_atual.turno_atual % 2 == 0:
            for i in range(8):
                for j in range(8):
                    if self.__tabuleiro[i][j] != None:
                        if self.__tabuleiro[i][j].tipo == 'rei':
                            if self.__tabuleiro[i][j].cor == 'branco':
                                posicao_rei = self.__tabuleiro[i][j].posicao
                        else:
                            if self.__tabuleiro[i][j].cor == 'preto':
                                ameacas_rei.extend(self.__tabuleiro[i][j].possiveis_movimentos(self.__tabuleiro))
            if posicao_rei == None:
                return True, "Brancas", True
            for possivel_ameaca in ameacas_rei:
                if possivel_ameaca == posicao_rei:
                    return True, "Brancas", False
            return False, "Brancas", False
        #verifica se as pretas estão em cheque
        if self.__jogo_atual.turno_atual % 2 == 1:
            for i in range(8):
                for j in range(8):
                    if self.__tabuleiro[i][j] != None:
                        if self.__tabuleiro[i][j].tipo == 'rei':
                            if self.__tabuleiro[i][j].cor == 'preto':
                                posicao_rei = self.__tabuleiro[i][j].posicao
                        else:
                            if self.__tabuleiro[i][j].cor == 'branco':
                                ameacas_rei.extend(self.__tabuleiro[i][j].possiveis_movimentos(self.__tabuleiro))

            if posicao_rei == None:
                return True, "Brancas", True
            for possivel_ameaca in ameacas_rei:
                if possivel_ameaca == posicao_rei:
                    return True, "Pretas", False
            return False, "Pretas", False
        #se o codigo não funcionar
        return None

    #deve ser executado somente se verifixar_cheque retornar true
    def verifica_cheque_mate(self) -> bool:
        ameacas_rei = list()
        movimentos_rei = None
        #verifica se as brancas tomaram cheque-mate
        if self.__jogo_atual.turno_atual % 2 == 0:
            for i in range(8):
                for j in range(8):
                    if self.__tabuleiro[i][j] != None:
                        if self.__tabuleiro[i][j].tipo == 'rei':
                            if self.__tabuleiro[i][j].cor == 'branco':
                                movimentos_rei = self.__tabuleiro[i][j].possiveis_movimentos(self.__tabuleiro)
                        else:
                            if self.__tabuleiro[i][j].cor == 'preto':
                                ameacas_rei.extend(self.__tabuleiro[i][j].possiveis_movimentos(self.__tabuleiro))
            if movimentos_rei == None:
               return True, "Brancas", True

            for possivel_fuga in movimentos_rei:
                if possivel_fuga not in ameacas_rei:
                    return False, "Brancas", False
            return True, "Brancas", False
        #verifica se as pretas tomaram cheque-mate
        if self.__jogo_atual.turno_atual % 2 == 1:
            for i in range(8):
                for j in range(8):
                    if self.__tabuleiro[i][j] != None:
                        if self.__tabuleiro[i][j].tipo == 'rei':
                            if self.__tabuleiro[i][j].cor == 'preto':
                                movimentos_rei = self.__tabuleiro[i][j].possiveis_movimentos(self.__tabuleiro)
                        else:
                            if self.__tabuleiro[i][j].cor == 'branco':
                                ameacas_rei.extend(self.__tabuleiro[i][j].possiveis_movimentos(self.__tabuleiro))
            if movimentos_rei == None:
               return True, "Brancas", True

            for possivel_fuga in movimentos_rei:
                if possivel_fuga not in ameacas_rei:
                    return False, "Pretas", False
            return True, "Pretas", False

    def abre_tela_jogo(self):
        possiveis_escolhas = [" Iniciar Partida contra BOT"," Iniciar simulacao entre dois BOT's"," Iniciar Player vs Player"," voltar"]
        tipo_menu = "JOGADOR"
        while True:
            opcao_escolhida = self.__tela_jogo.mostrar_opcoes(possiveis_escolhas,tipo_menu, True)
            if opcao_escolhida == 1:# contra BOT
                nome_jogador = self.__tela_jogo.solicitar_jogador(1)
                jogador = self.__controlador_central.buscar_jogador(nome_jogador)
                tabuleiro = self.__tabuleiro
                if jogador != None and isinstance(jogador,Player):
                    self.__jogo_atual = Jogo(jogador, self.__bot_preto,tabuleiro)
                    self.__jogador_1 = jogador
                    self.__tela_jogo.mostrar_tabuleiro(self.gerar_foto_tabuleiro(tabuleiro))
                    self.menu_jogadas_player_bot()
                    break
                else:
                    msg = "Jogador não encontrado! "
                    self.__tela_jogo.notifica_usuario(msg,2.0)
            elif opcao_escolhida == 2: #Simulacao
                tabuleiro = self.__tabuleiro
                self.__jogador_1 = self.__bot_branco
                self.__jogo_atual = Jogo(self.__bot_branco, self.__bot_preto,tabuleiro)
                self.__tela_jogo.mostrar_tabuleiro(self.gerar_foto_tabuleiro(tabuleiro))
                self.Simulacao()
                break
            elif opcao_escolhida == 3: #Player Vs Player
                nome_jogador_1 = self.__tela_jogo.solicitar_jogador(1)
                nome_jogador_2 = self.__tela_jogo.solicitar_jogador(2)
                jogador_1 = self.__controlador_central.buscar_jogador(nome_jogador_1)
                jogador_2 = self.__controlador_central.buscar_jogador(nome_jogador_2)
                tabuleiro = self.__tabuleiro
                if jogador_1 != None and isinstance(jogador_1,Player) and jogador_2 != None and isinstance(jogador_2,Player):
                    self.__jogo_atual = Jogo(jogador_1, jogador_2,tabuleiro)
                    self.__jogador_1 = jogador_1
                    self.__jogador_2 = jogador_2
                    self.__tela_jogo.mostrar_tabuleiro(self.gerar_foto_tabuleiro(tabuleiro))
                    self.menu_jogadas_player_player()
                    break
                else:
                    msg = "Jogador não encontrado! "
                    self.__tela_jogo.notifica_usuario(msg,2.0)
            elif opcao_escolhida == 4:
                self.__controlador_central.inicia_programa()
                break
            else:
                msg = "digite uma opcao valida! "
                self.__tela_jogo.notifica_usuario(msg,1.5)

    def menu_jogadas_player_bot(self):
        possiveis_escolhas = [" Jogar"," Desistir da partida"]
        tipo_menu = "JOGADAS"
        while True:
            opcao_escolhida = self.__tela_jogo.mostrar_opcoes(possiveis_escolhas,tipo_menu, False)
            if opcao_escolhida == 1: 
                jogada_valida = False
                while jogada_valida ==  False:
                    jogada_valida, msg, finalizou_ou_nao = self.mover_peca_jogador()
                    self.__tela_jogo.notifica_usuario(msg,1.5)
                    if finalizou_ou_nao:
                        self.finalizar_partida(self.__jogador_1.nome,"Xeque_mate")       
                time.sleep(random.uniform(0.5,1.5))
                jogada_valida_bot, msg_bot, finalizou_ou_nao_bot = self.mover_peca_bot("preto")
                if finalizou_ou_nao_bot:
                    self.finalizar_partida(self.__bot_preto.nome,"Xeque_Mate")
                self.__tela_jogo.notifica_usuario(msg_bot,1.5)
                foto_tabuleiro = self.gerar_foto_tabuleiro(self.__tabuleiro)
                self.__tela_jogo.mostrar_tabuleiro(foto_tabuleiro)
            elif opcao_escolhida == 2:
                self.finalizar_partida(self.__bot_preto.nome, "Desistencia")
                break
            else:
                msg = "digite uma opcao valida! "
                self.__tela_jogo.notifica_usuario(msg,1.5)

    def menu_jogadas_player_player(self):
        possiveis_escolhas = [" Jogar"," Desistir da partida"]
        tipo_menu_branco = "JOGADA - BRANCAS"
        tipo_menu_preto = "JOGADA - PRETAS"
        while True:
            #********************* vez das Brancas *****************************
            opcao_escolhida = self.__tela_jogo.mostrar_opcoes(possiveis_escolhas,tipo_menu_branco, False)
            if opcao_escolhida == 1: 
                jogada_valida = False
                while jogada_valida ==  False:
                    jogada_valida, msg, finalizou_ou_nao = self.mover_peca_jogador("branco")
                    self.__tela_jogo.notifica_usuario(msg,1.5)
                    if finalizou_ou_nao:
                        self.finalizar_partida(self.__jogador_1.nome,"Xeque_mate")       
            elif opcao_escolhida == 2:
                self.finalizar_partida(self.__jogador_2.nome, "Desistencia")
                break
            else:
                msg = "digite uma opcao valida! "
                self.__tela_jogo.notifica_usuario(msg,1.5)
                #********************* mostra tabuleiro *****************************
            self.__tela_jogo.notifica_usuario(msg,1.5)
            foto_tabuleiro = self.gerar_foto_tabuleiro(self.__tabuleiro)  
            self.__tela_jogo.mostrar_tabuleiro(foto_tabuleiro)
                #********************* vez das pretas *****************************
            opcao_escolhida = self.__tela_jogo.mostrar_opcoes(possiveis_escolhas,tipo_menu_preto, False)
            if opcao_escolhida == 1: 
                jogada_valida = False
                while jogada_valida ==  False:
                    jogada_valida, msg, finalizou_ou_nao = self.mover_peca_jogador("preto")
                    self.__tela_jogo.notifica_usuario(msg,1.5)
                    if finalizou_ou_nao:
                        self.finalizar_partida(self.__jogador_2.nome,"Xeque_mate")       
            elif opcao_escolhida == 2:
                self.finalizar_partida(self.__jogador_2.nome, "Desistencia")
                break
            else:
                msg = "digite uma opcao valida! "
                self.__tela_jogo.notifica_usuario(msg,1.5)
                 #********************* mostra tabuleiro *****************************
            self.__tela_jogo.notifica_usuario(msg,1.5)
            foto_tabuleiro = self.gerar_foto_tabuleiro(self.__tabuleiro)  
            self.__tela_jogo.mostrar_tabuleiro(foto_tabuleiro)


    def Simulacao(self):
        contador = 0
        while contador < 200:
            #***************************** vez das Brancas ***************************************
            time.sleep(random.uniform(0.05,0.06))
            msg_bot, finalizou_ou_nao_bot_branco = self.mover_peca_bot(self.__bot_branco, "branco")
            if finalizou_ou_nao_bot_branco:
                self.finalizar_partida(self.__bot_branco.nome,"Xeque_Mate")
            self.__tela_jogo.notifica_usuario(msg_bot,0.02)
            foto_tabuleiro = self.gerar_foto_tabuleiro(self.__tabuleiro)
            self.__tela_jogo.mostrar_tabuleiro(foto_tabuleiro)
            #***************************** vez das Pretas ***************************************
            time.sleep(random.uniform(0.05,0.06))
            msg_bot, finalizou_ou_nao_bot_preto = self.mover_peca_bot(self.__bot_preto,"preto")
            if finalizou_ou_nao_bot_preto:
                self.finalizar_partida(self.__bot_preto.nome,"Xeque_Mate")
            self.__tela_jogo.notifica_usuario(msg_bot,0.02)
            foto_tabuleiro = self.gerar_foto_tabuleiro(self.__tabuleiro)
            self.__tela_jogo.mostrar_tabuleiro(foto_tabuleiro)
            contador +=1

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
            linha.append(f" {i}")
            mesa.append(linha)
        return  mesa
    
    def descobre_peca_manipulada(self, posicao_peca):
        coluna = posicao_peca[0]
        linha = posicao_peca[1]
        return self.__tabuleiro[coluna][linha]
    
    def finalizar_partida(self,quem_ganhou, motivo):
        self.__historico_partidas.append(self.__jogo_atual)
        self.__jogo_atual.fechar_jogo(quem_ganhou, motivo)
        self.__tela_jogo.gerar_relatorio(self.__jogador_1.nome,quem_ganhou, motivo, self.__jogo_atual.historico_jogadas, self.__jogo_atual.turno_atual)
        self.abre_tela_jogo()

    def mover_peca_bot(self, Bot_cor , cor: str):
        rei_morto = False
        while True:
            lista_de_pecas = []
            for linha in range(8):
                for coluna in range(8):
                    if self.__tabuleiro[linha][coluna] != None and self.__tabuleiro[linha][coluna].cor == cor:
                        peca = self.__tabuleiro[linha][coluna]
                        lista_de_pecas.append(peca)
            peca_selecionada = random.choice(lista_de_pecas)
            possiveis_movimentos = peca_selecionada.possiveis_movimentos(self.__tabuleiro)
            if len(possiveis_movimentos) != 0:
                break
        movimento_selecionado = random.choice(possiveis_movimentos)
        x_inicial = peca_selecionada.posicao[0]
        y_inicial = peca_selecionada.posicao[1]
        x_final = movimento_selecionado[0]
        y_final = movimento_selecionado[1]
        self.__tabuleiro[x_final][y_final] = self.__tabuleiro[x_inicial][y_inicial]
        self.__tabuleiro[x_inicial][y_inicial] = None
        self.sincronizar_posicoes_tabuleiro()       
        self.__jogo_atual.registra_jogada(Bot_cor,peca,peca.posicao,movimento_selecionado,self.__tabuleiro)
        xeque,cor_em_xeque, rei_morto = self.verifica_cheque()
        xeque_mate, cor_em_xeque_mate, rei_morto = self.verifica_cheque_mate()
        if rei_morto == True: 
            return  f"Xeque-Mate, as {cor_em_xeque_mate} Perderam", True
        if xeque:
            if xeque_mate:
                return  f"Xeque-Mate, as {cor_em_xeque_mate} Perderam", True
            return f"Xeque nas {cor_em_xeque} !", False
        return "Jogada efetuada. ", False
    

    def mover_peca_jogador(self, cor):
        posicao_inicial = self.__tela_jogo.solicitar_posicao('inicial')
        posicao_final = self.__tela_jogo.solicitar_posicao('final')
        x_inicial = posicao_inicial[0]
        y_inicial = posicao_inicial[1]
        x_final = posicao_final[0]
        y_final = posicao_final[1]
        if self.__tabuleiro[x_inicial][y_inicial] == None:
            return False,'A posição está vazia, selecione uma peça', False
        if self.__tabuleiro[x_inicial][y_inicial].cor != cor:
            return False,f'A peça escolhida pertence ao jogador adversário, escolha uma peça {cor}', False
        movimentos_peca = self.__tabuleiro[x_inicial][y_inicial].possiveis_movimentos(self.__tabuleiro)
        if posicao_final not in movimentos_peca:
            return False,'A peça não pode se mover para essa posição, selecione uma posição válida', False
        if self.__tabuleiro[x_final][y_final] != None:
            if self.__tabuleiro[x_final][y_final].cor == cor:
                return False,'Já existe uma peça aliada nesta posição, seleciona uma posição válida', False
        self.__tabuleiro[x_final][y_final] = self.__tabuleiro[x_inicial][y_inicial]
        self.__tabuleiro[x_inicial][y_inicial] = None
        self.sincronizar_posicoes_tabuleiro()       
        self.__jogo_atual.registra_jogada(self.__jogador_1,self.__tabuleiro[x_final][y_final],posicao_inicial,posicao_final,self.__tabuleiro)
        xeque,cor_em_xeque, rei_morto = self.verifica_cheque()
        xeque_mate, cor_em_xeque_mate, rei_morto = self.verifica_cheque_mate()
        if rei_morto == True: 
            return True, f"Xeque-Mate, as {cor_em_xeque_mate} Perderam", True
        if xeque:
            if xeque_mate:
                return True, f"Xeque-Mate, as {cor_em_xeque_mate} Perderam", True
            return True, f"Xeque nas {cor_em_xeque} !", False
        return True, "Jogada efetuada. ", False