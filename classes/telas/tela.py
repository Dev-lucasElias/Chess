from abc import ABC, abstractmethod
import os
from classes.excepitions.relatorioError import relatorioError

class Tela(ABC):

    @abstractmethod
    def mostrar_opcoes(self, opcoes, tipo_menu, limpar) -> int:
        try:
            print(f"""
            ****  MENU {tipo_menu} ****
                                                
                Escolha uma opcao:
                    """)
            for i in range(len(opcoes)):
                print(f"{i+1} - {opcoes[i]}")

            opcao_escolhida = self.verifica_numero_inteiro(input("""
                opção ecolhida:"""),[range(1,len(opcoes))])                                    
            if limpar :
                self.limpar_tela()
            return opcao_escolhida
        
        except:Exception


    def verifica_numero_inteiro(self,mensagem, inteiros_validos):
        input_manual = mensagem
        while True:
            try:
                input_manual_em_int = int(input_manual)
                return input_manual_em_int
            except ValueError:
                print("voce digitou valores incorretos, por favor, insira novamente.")
                print(f"valore inteiros validos : {inteiros_validos}")

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear') or None
