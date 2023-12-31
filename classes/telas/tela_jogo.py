from classes.telas.tela import Tela
from classes.modelos.jogada import Jogada
from classes.excepitions.relatorioError import relatorioError
import sys
import PySimpleGUI as sg


class TelaJogo(Tela):

    def mostrar_tabuleiro(self, tabuleiro):
        janela = sg.Window('Chess', tabuleiro)
        posicao_inicial = None
        posicao_final = None
        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED:
                sys.exit()
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

    def gerar_foto_tabuleiro(self, tabuleiro):
        tabuleiro_gui = list()
        i = -1
        for linha in tabuleiro:
            i += 1
            j = -1
            linha_tabuleiro = list()
            peca = None
            for posicao in linha:
                j += 1
                try:
                    if posicao.cor == 'branco':
                        if posicao.tipo == 'BISPO':
                            peca = 'images/wB.png'
                        if posicao.tipo == 'CAVALO':
                            peca = 'images/wN.png'
                        if posicao.tipo == 'PEAO':
                            peca = 'images/wp.png'
                        if posicao.tipo == 'RAINHA':
                            peca = 'images/wQ.png'
                        if posicao.tipo == 'REI':
                            peca = 'images/wK.png'
                        if posicao.tipo == 'TORRE':
                            peca = 'images/wR.png'
                    if posicao.cor == 'preto':
                        if posicao.tipo == 'BISPO':
                            peca = 'images/bB.png'
                        if posicao.tipo == 'CAVALO':
                            peca = 'images/bN.png'
                        if posicao.tipo == 'PEAO':
                            peca = 'images/bp.png'
                        if posicao.tipo == 'RAINHA':
                            peca = 'images/bQ.png'
                        if posicao.tipo == 'REI':
                            peca = 'images/bK.png'
                        if posicao.tipo == 'TORRE':
                            peca = 'images/bR.png'
                except:
                    peca = 'images/blank.png'
                cor = 'firebrick4' if (i + j) % 2 == 0 else 'wheat'
                if peca != None:
                    botao_peca = sg.Button(size=(1, 1), image_filename=peca, button_color=('tomato', cor), key=(j, i))
                else:
                    botao_peca = sg.Button(size=(1, 1), button_color=('tomato', cor), key=(j, i))
                linha_tabuleiro.append(botao_peca)
            tabuleiro_gui.append(linha_tabuleiro)
        return tabuleiro_gui

    def mostrar_opcoes(self, opcoes, tipo_menu, limpar) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu, limpar)
    
    def solicitar_jogador(self, numero) ->str:
        layout = [
        [sg.Text(f"Por favor, digite o nome do jogador {numero} para começar a partida:")],
        [sg.InputText(key='nome')],
        [sg.Button('OK'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Solicitar Jogador', layout)

        while True:
            event, values = window.read()

            if event == 'Cancelar':
                window.close()
                return None

            if event == sg.WINDOW_CLOSED:
                sys.exit()

            if event == 'OK':
                nome_jogador = values['nome']
                window.close()
                return nome_jogador

    def notifica_usuario(self, mensagem, tempo):
        sg.popup_quick_message(mensagem, title="Notificação", auto_close_duration=0.5)
    
    def gerar_relatorio(self, jogador1, jogador2, quem_ganhou, motivo, historico_jogadas, quantos_turnos):
        layout = [
            [sg.Text("***************  RELATORIO DE JOGO ***************")],
            [sg.Text(f"Jogadores: {jogador1} e {jogador2}")],
            [sg.Text(f"Vencedor: {quem_ganhou}")],
            [sg.Text(f"Motivo: {motivo}")],
            [sg.Text(f"Quantos turnos: {quantos_turnos}")],
            [sg.Text("------ Histórico de Jogadas ------")],
            [sg.Multiline("", size=(50, 10), key='historico', disabled=True)],
            [sg.Button('OK')]
        ]

        window = sg.Window('Relatório de Jogo', layout)
        window.finalize()

        historico_texto = ""

        for i in historico_jogadas:
            historico_texto += f"T: {i.turno_jogada} - Jogador: {i.jogador.nome}, Peça selecionada: {i.peca.tipo}, Movimento: [{i.posicao_inicial},{i.posicao_final}]\n"

        window['historico'].update(historico_texto)

        while True:
            event, values = window.read()

            if event == 'OK':
                window.close()
                break

            if event == sg.WINDOW_CLOSED:
                sys.exit()
        
    def gerar_historico_partidas(self,historico_partidas):
        historico_text = ""
        try:
            for i in historico_partidas:
                historico_text += (
                    f"***** RELATORIO DE JOGO *****\n\n"
                    f"Jogadores: {i.jogador_1.nome} vs {i.jogador_2.nome}\n"
                    f"Vencedor: {i.quem_ganhou}\n"
                    f"motivo: {i.motivo}\n"
                    f"Quantos turnos: {i.turno_atual}\n\n"
                    "-- historico de jogadas --\n\n"
                )
        except Exception as e:
            raise relatorioError from e

        layout = [[sg.Text("Histórico de Partidas")],
                  [sg.Multiline(historico_text, size=(50, 10), disabled=True)],
                  [sg.Button("Fechar")]]

        window = sg.Window("Histórico de Partidas", layout)

        while True:
            event, values = window.read()

            if event == 'Fechar':
                break
            if event == sg.WINDOW_CLOSED:
                sys.exit()

        window.close()
        
    
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
        
        
