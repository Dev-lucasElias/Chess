from abc import ABC, abstractmethod
import os

class Tela(ABC):

    @abstractmethod
    def mostrar_opcoes(self, opcoes, tipo_menu) -> int:
        print(f"""
        ****  MENU {tipo_menu} ****
                                            
            Escolha uma opcao:
                """)
        for i in range(len(opcoes)):
            print(f"{i+1} - {opcoes[i]}")

                                            
        opcao_escolhida = int(input("""
            opção ecolhida:"""))
        self.limpar_tela()
        return opcao_escolhida

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear') or None
