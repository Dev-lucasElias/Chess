from classes.telas.tela import Tela
import time

class TelaRegras(Tela):
    def __init__(self, controlador_central) -> None:
        self.__controlador_central = controlador_central

    def mostrar_opcoes(self, opcoes, tipo_menu, limpar) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu, limpar)
    
    def voltar_menu_central(self):
        self.__controlador_central.inicia_programa()

    def diferencas(self):
        while True:
            self.limpar_tela()
            print('Diferente do xadrez tradicional, nosso xadrez simplificado \n'
                  'não possui regras especiais, como: rock, em peasant, transformação do peão \n'
                  'e peão movendo duas casas na primeira jogada. \n'
                  'Além dessas mudanças, a principal diferença é que o nosso jogo \n'
                  'permite o sácrificio do Rei, criando oportunidades de jogadas novas \n'
                  'e armadilhas criativas. Se divirta!')
            for _ in range(3):
                print()
            voltar = input('Aperte a tecla "ENTER" para voltar:')
            if voltar == '':
                self.limpar_tela()
                self.mostrar_regras()
                break
            else:
                self.limpar_tela()
                print('tente novamente')
                time.sleep(1.5)
    
    def tutorial(self):
        while True:
            self.limpar_tela()
            print('Para jogar, primeiro cadastre seu jogador dentro do "Menu Jogador", \n'
                  'em seguida volte para a tela inicial e abra o "Menu Partida", \n'
                  'dentro desse menu você terá diversos estilos de jogo, basta escolher \n'
                  'escolher o seu favorito para dar início a partida. \n'
                  'Dentro da partida, a cada turno haverá a opção de fazer uma jogada ou \n'
                  'desistir no meio. Selecione jogar, e então digite a posição da peça \n'
                  'que quer mover, e então a posição em que ela deve ir. As posições \n'
                  'são compostas por uma letra entre "A" e "H" e um número entre "0" e "7", \n'
                  'por exemplo: "b1" ou "c6". \n'
                  'Após cada jogada será o turno do adversário e então o seu novamente, \n'
                  'continue jogando até ganhar, boa sorte! :)')
            for _ in range(3):
                print()
            voltar = input('Aperte a tecla "ENTER" para voltar:')
            if voltar == '':
                self.limpar_tela()
                self.mostrar_regras()
                break
            else:
                self.limpar_tela()
                print('tente novamente')
                time.sleep(1.5)

    
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