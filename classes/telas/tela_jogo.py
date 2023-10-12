from classes.telas.tela import Tela


class TelaJogo(Tela):

    def mostrar_opcoes(self, opcoes, tipo_menu) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu)
    
    def mostrar_tabuleiro(self, foto_matriz):
        for linha in foto_matriz:
            for posicao in linha:
                    print(posicao, end=' ')
            print('\n')

    def mostrar_opcoes(self, opcoes, tipo_menu) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu)
    
    def solicitar_jogador(self) ->str:
        nome_jogador = input("por favor digite o nome do jogador para começar a partida: ")
        return nome_jogador
    
    def solicitar_posicao(self, tipo) -> str:
        while True:
            in_posicao_escolhida = input(f"Posiçao {tipo}: ").lower().strip()
            if len(in_posicao_escolhida) <= 2:
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
                print("posição não faz parte do tabuleiro! tente denovo.")
        posicao_escolhida = (int(in_posicao_escolhida[0]), int(in_posicao_escolhida[1]))
        return posicao_escolhida
        
        
        
