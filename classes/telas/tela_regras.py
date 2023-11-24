from classes.telas.tela import Tela
import time
import PySimpleGUI as sg

class TelaRegras(Tela):
    def __init__(self, controlador_central) -> None:
        self.__controlador_central = controlador_central

    def mostrar_opcoes(self, opcoes, tipo_menu, limpar) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu, limpar)
    
    def voltar_menu_central(self):
        self.__controlador_central.inicia_programa()

    def diferencas(self):
        layout = [
            [sg.Text('Diferente do xadrez tradicional, nosso xadrez simplificado')],
            [sg.Text('não possui regras especiais, como: rock, em peasant, transformação do peão')],
            [sg.Text('e peão movendo duas casas na primeira jogada.')],
            [sg.Text('Além dessas mudanças, a principal diferença é que o nosso jogo')],
            [sg.Text('permite o sacrifício do Rei, criando oportunidades de jogadas novas')],
            [sg.Text('e armadilhas criativas. Se divirta!')],
            [sg.Button('Voltar')]
        ]

        window = sg.Window('Diferenças do Jogo', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Voltar':
                window.close()
                self.limpar_tela()
                self.mostrar_regras()
                break

        window.close()
    
    def tutorial(self):
        layout = [
            [sg.Text('Para jogar, primeiro cadastre seu jogador dentro do "Menu Jogador"')],
            [sg.Text('Em seguida, volte para a tela inicial e abra o "Menu Partida".')],
            [sg.Text('Dentro desse menu, você terá diversos estilos de jogo, basta escolher')],
            [sg.Text('o seu favorito para dar início à partida.')],
            [sg.Text('Dentro da partida, a cada turno, haverá a opção de fazer uma jogada ou')],
            [sg.Text('desistir no meio. Selecione jogar e então digite a posição da peça')],
            [sg.Text('que quer mover e então a posição em que ela deve ir. As posições')],
            [sg.Text('são compostas por uma letra entre "A" e "H" e um número entre "0" e "7",')],
            [sg.Text('por exemplo: "b1" ou "c6".')],
            [sg.Text('Após cada jogada, será o turno do adversário e então o seu novamente,')],
            [sg.Text('continue jogando até ganhar. Boa sorte! :)')],
            [sg.Button('Voltar')]
        ]

        window = sg.Window('Tutorial', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Voltar':
                window.close()
                self.limpar_tela()
                self.mostrar_regras()
                break

        window.close()

    
    def mostrar_regras(self):
        possiveis_escolhas = [" Diferenças para o xadrez tradicional"," Como jogar", " Voltar"]
        tipo_menu =  "REGRAS"
        while True:
            self.limpar_tela()
            opcao_escolhida = self.mostrar_opcoes(possiveis_escolhas,tipo_menu, True)
            if opcao_escolhida == 1:
                self.diferencas()
                break
            elif opcao_escolhida == 2:
                self.tutorial()
                break
            elif opcao_escolhida == 3:
                self.voltar_menu_central()
            else:
                print("Opção invalida")
                time.sleep(1.5)