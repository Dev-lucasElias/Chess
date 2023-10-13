from classes.modelos.jogada import Jogada

class Jogo:

    def __init__(self, jogador_partida, tabuleiro) -> None:
        self.__jogador_partida = jogador_partida
        self.__turno_atual = 0
        self.__historico_jogadas = []
        self.__resultado_tabuleiro = tabuleiro
        self.__status_partida = None
        self.__quem_ganhou = None
        self.__motivo = None

    @property
    def resultado_tabuleiro(self) -> list:
        return self.__resultado_tabuleiro
	
    @resultado_tabuleiro.setter
    def resultado_tabuleiro(self, resultado_tabuleiro) -> None:
        if isinstance(resultado_tabuleiro, list):
            self.__resultado_tabuleiro = resultado_tabuleiro
    
    #turno par = vez das brancas, turno impar = vez das pretas
    @property
    def turno_atual(self) -> int:
        return self.__turno_atual
    
    @turno_atual.setter
    def turno_atual(self, turno_atual) -> None:
        if isinstance(turno_atual, int):
            self.__turno_atual = turno_atual

    @property
    def historico_jogadas(self):
        return self.__historico_jogadas
    
    @property
    def quem_ganhou(self):
        return self.__quem_ganhou
    
    @quem_ganhou.setter
    def quem_ganhou(self, quem_ganhou):
        if isinstance(quem_ganhou, object):
            self.__quem_ganhou = quem_ganhou
    @property
    def motivo(self):
        return self.__motivo
    
    @motivo.setter
    def motivo(self, motivo):
        if isinstance(motivo, str):
            self.__motivo = motivo
    
    @property
    def status_partida(self):
        return self.__status_partida
    
    @status_partida.setter
    def status_partida(self, status):
        if isinstance(status, str):
            self.__status_partida = status

        
    def fechar_jogo(self, quem_ganhou, motivo):
        self.quem_ganhou = quem_ganhou
        self.motivo = motivo
        self.status_partida = "Finalizado"
        

    def registra_jogada(self, jogador,peca, posicao_inical, posicao_final, resultado_tabuleiro):
        jogada = Jogada(jogador, peca, posicao_inical, posicao_final, resultado_tabuleiro, self.__turno_atual)
        self.__historico_jogadas.append(jogada)
        self.__turno_atual += 1
        self.resultado_tabuleiro = resultado_tabuleiro
