from classes.telas.tela import Tela
from classes.modelos.jogada import Jogada
from classes.excepitions.relatorioError import relatorioError
import time
import PySimpleGUI as sg


class TelaJogo(Tela):

    def mostrar_tabuleiro(self, tabuleiro):
        janela = sg.Window('Chess', tabuleiro)
        posicao_inicial = None
        posicao_final = None
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            elif type(evento) == tuple:  # Checking if the event is a tuple, indicating a button click
                if posicao_inicial is None:
                    posicao_inicial = evento  # Store the first click

                elif posicao_final is None:
                    posicao_final = evento  # Store the second click

                    break
        
        posicao_inicial = list(posicao_inicial[::-1])
        posicao_final = list(posicao_final[::-1])
        janela.close()
        return posicao_inicial, posicao_final


    def mostrar_opcoes(self, opcoes, tipo_menu, limpar) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu, limpar)
    
    def solicitar_jogador(self, numero) ->str:
        nome_jogador = input(f"                por favor digite o nome do jogador {numero} para começar a partida: ")
        self.limpar_tela()
        return nome_jogador
    
    def notifica_usuario(self, menssagem, tempo):
        print(f"{menssagem}")
        time.sleep(tempo)
    
    def gerar_relatorio(self,jogador1,jogador2, quem_ganhou, motivo, historico_jogadas, quantos_turnos):
        try:
            print(f"""
              ***************  RELATORIO DE JOGO ***************
            
            Jogadores: {jogador1} e {jogador2}
            Vencedor: {quem_ganhou}
            motivo: {motivo}
            Quantos turnos: {quantos_turnos}
            
                        ------ Historico de jogadas ------
            
            """)

            for i in historico_jogadas:
                print(f"""                 T: {i.turno_jogada} - Jogador: {i.jogador.nome}, Peça selecionada: {i.peca.tipo}, Movimento: [{i.posicao_inicial},{i.posicao_final}]
                    """)
                
            print("                 -------------------------------------------------------------------")

        except Exception as e:
            raise relatorioError from e
        
    def gerar_historico_partidas(self,historico_partidas):
        try:
            for i in historico_partidas:
                print(f"""
                *****  RELATORIO DE JOGO ****
                
                Jogadores: {i.jogador_1.nome} vs {i.jogador_2.nome}
                Vencedor: {i.quem_ganhou}
                motivo: {i.motivo}
                Quantos turnos: {i.turno_atual}
                
                -- historico de jogadas --
                
                """)
        except Exception as e:
            raise relatorioError from e    
        
    
    def solicitar_posicao(self, tipo) -> list:
        nao_faz_parte = "posição não faz parte do tabuleiro! tente denovo."
        while True:
            in_posicao_escolhida = input(f"Posiçao {tipo}: ").lower().strip()
            if len(in_posicao_escolhida) == 2 and in_posicao_escolhida[0].isalpha() and in_posicao_escolhida[1].isnumeric():
                if int(in_posicao_escolhida[1]) > 7:
                    in_posicao_escolhida = in_posicao_escolhida.replace(in_posicao_escolhida[1],'7')
                if int(in_posicao_escolhida[1]) < 0:
                    in_posicao_escolhida = in_posicao_escolhida.replace(in_posicao_escolhida[1],'0')
                if in_posicao_escolhida[0] == "a":
                    in_posicao_escolhida = in_posicao_escolhida.replace( "a","0")
                    break
                elif in_posicao_escolhida[0] == "b":
                    in_posicao_escolhida = in_posicao_escolhida.replace( "b","1")
                    break
                elif in_posicao_escolhida[0] == "c":
                    in_posicao_escolhida = in_posicao_escolhida.replace( "c","2")
                    break
                elif in_posicao_escolhida[0] == "d":
                    in_posicao_escolhida = in_posicao_escolhida.replace( "d","3")
                    break
                elif in_posicao_escolhida[0] == "e":
                    in_posicao_escolhida = in_posicao_escolhida.replace( "e","4")
                    break
                elif in_posicao_escolhida[0] == "f":
                    in_posicao_escolhida = in_posicao_escolhida.replace( "f","5")
                    break
                elif in_posicao_escolhida[0] == "g":
                    in_posicao_escolhida = in_posicao_escolhida.replace( "g","6")
                    break
                elif in_posicao_escolhida[0] == "h":
                    in_posicao_escolhida = in_posicao_escolhida.replace( "h","7")
                    break
                else:
                    print(nao_faz_parte)
            else:
                print(nao_faz_parte)
        posicao_escolhida = [int(in_posicao_escolhida[1]), int(in_posicao_escolhida[0])]
        return posicao_escolhida
        
        
