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
    
   