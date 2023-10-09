class TelaJogo:
    def mostrar_opcoes(self) -> int:
        opcao_escolhida = int(input("""
****  MENU JOGO ****
                                    
    Escolha uma opção:
                                    
        1- Iniciar uma partida
        2- voltar
                                    
    opção ecolhida:"""))
        return opcao_escolhida