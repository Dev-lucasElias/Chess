from classes.telas.tela import Tela

class TelaPlayer(Tela):
    def mostrar_opcoes(self, opcoes, tipo_menu, limpar) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu, limpar)
        
    
    def listar_jogadores(self,lista):
        if len(lista) > 1:
            print("""
        LISTA DE JOGADORES
                            
    -------------------------
                        """)
            for pessoa in lista:
                print("       "+pessoa.nome)# montar uma lista
            #chama função da tela
            print("""
                  
   --------------------------
                        """)
        else:
            print("Não há jogadores cadastrados.")
        
        return

    def pergunta_dados(self):
        nome_novo_jogador = input("digite o nome do novo jogador: ")
        cpf_novo_jogador = input("Digite o cpf do novo jogador: ")

        return nome_novo_jogador, cpf_novo_jogador

    def pergunta_dados_excluir(self) -> str:
        nome = input("                Digite o nome do jogador que gostaria de remover:")
        return nome