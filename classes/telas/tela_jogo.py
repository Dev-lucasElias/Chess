from classes.telas.tela import Tela


class TelaJogo(Tela):

    def mostrar_opcoes(self, opcoes, tipo_menu) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu)
    
    def mostrar_opcoes_iniciais(self) -> int:
        opcao_escolhida = self.mostrar_opcoes([" Fazer uma jogada"," Desistir"],"PARTIDA")
        self.limpar_tela()
        return opcao_escolhida
    
    def mostrar_tabuleiro(self, tabuleiro):
        for row in tabuleiro:
            for peca in row:
                if peca is None:
                    print('   .   ', end=' ')
                else:
                    if peca.tipo == "peao":
                        print(f' {peca.cor[0]}{peca.tipo} ', end=' ')
                    else:
                        print(f'{peca.cor[0]}{peca.tipo} ', end=' ')
            print('\n')
        #---- não trazer a entidade peca para a tela, apenas dados!.----

    def mostrar_opcoes_Djogadas(self) -> int:
        opcao_escolhida = int(input("""
    ****  MENU JOGO ****
                                        
        Escolha uma opção:
                                        
            1- Movimentar uma peça
            2- Desistir da partida
                                        
        opção ecolhida:"""))
        return opcao_escolhida