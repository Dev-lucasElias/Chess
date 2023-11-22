from classes.telas.tela import Tela
import PySimpleGUI as sg

class TelaPlayer(Tela):
    def mostrar_opcoes(self, opcoes, tipo_menu, limpar) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu, limpar)
        
    
    def listar_jogadores(self,lista):
        if len(lista) >= 1:
            nomes_jogadores = [pessoa.nome for pessoa in lista]

            layout = [
                [sg.Text("LISTA DE JOGADORES")],
                [sg.Listbox(values=nomes_jogadores, size=(30, 10))],
                [sg.Button('Fechar')]
            ]

            janela = sg.Window('Lista de Jogadores', layout)

            while True:
                event, values = janela.read()

                if event == sg.WIN_CLOSED or event == 'Fechar':
                    break
            janela.close()

        else:
            sg.popup_ok("Não há jogadores cadastrados.")

    def pergunta_dados(self):
        layout=[
            [sg.Text("digite o nome do novo jogador: "), sg.Input("fulano", key='nome')],
            [sg.Text("Digite o cpf do novo jogador: "), sg.Input("123456789", key='cpf')],
            [sg.Button("Enviar"), sg.Button("cancelar")]
        ]

        janela = sg.Window('chess',layout)
        while True:
            event, values = janela.read()

            if event == sg.WIN_CLOSED or event == 'cancelar':
                janela.close()
                return None, None
            elif event == 'Enviar':
                nome_novo_jogador = values['nome']
                cpf_novo_jogador = values['cpf']
                janela.close()
                break

        return nome_novo_jogador, cpf_novo_jogador

    def pergunta_dados_excluir(self) -> str:
        layout = [
            [sg.Text("Digite o nome do jogador que gostaria de remover:")],
            [sg.InputText(key='nome')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Excluir Jogador', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return None  # Retorna None se o usuário cancelar a entrada de dados

            if event == 'OK':
                nome_jogador = values['nome']
                window.close()
                return nome_jogador