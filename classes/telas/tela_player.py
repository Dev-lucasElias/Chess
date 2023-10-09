class TelaPlayer:
    
    def mostrar_opcoes(self) -> int:
        opcao_escolhida = int(input("""
****  MENU PLAYER ****
                                    
    Escolha uma opcao:
                                    
        1- Adicionar jogador
        2- excluir jogador
        3- Voltar
                                    
    opção ecolhida: """))
        return opcao_escolhida
    
    def pergunta_dados(self):
        nome_novo_jogador = input("digite o nome do novo jogador: ")
        cpf_novo_jogador = input("Digite o cpf do novo jogador: ")

        return nome_novo_jogador, cpf_novo_jogador

    def pergunta_dados_excluir(self) -> str:
        nome = input("Digite o nome do jogador que gostaria de remover:")
        return nome