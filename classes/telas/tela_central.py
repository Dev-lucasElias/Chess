from classes.telas.tela import Tela

class TelaCentral(Tela):
    def mostrar_opcoes(self, opcoes, tipo_menu) -> int:
        return super().mostrar_opcoes(opcoes, tipo_menu)
    
    def mostrar_opcoes_iniciais(self) -> int:
        self.limpar_tela()
        opcao_escolhida = self.mostrar_opcoes(["Jogador","Partida"],"CENTRAL")
        self.limpar_tela()
        return opcao_escolhida


    

        
