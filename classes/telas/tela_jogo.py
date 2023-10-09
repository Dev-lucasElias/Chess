class TelaJogo:
    def mostrar_opcoes(self) -> int:
        opcao_escolhida = int(input("""
****  MENU JOGO ****
                                    
    Escolha uma opção:
                                    
        1- Iniciar uma partida
        2- voltar
                                    
    opção ecolhida:"""))
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