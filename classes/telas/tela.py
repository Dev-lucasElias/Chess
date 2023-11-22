from abc import ABC, abstractmethod
import os
from classes.excepitions.relatorioError import relatorioError
import PySimpleGUI as sg

class Tela(ABC):

    @abstractmethod
    def mostrar_opcoes(self, opcoes, tipo_menu, limpar) -> int:
        try:
            layout = [
                [sg.Text(f"****  MENU {tipo_menu} ****", font=("Helvetica", 25))],
            ]

            for i in range(len(opcoes)):
                layout.append([sg.Button(f"{i+1}  -  {opcoes[i]}")])

            window = sg.Window('Chess', layout, font=("Helvetica", 12))

            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED or ' - ' in event:
                    break

        except:Exception
        try:
            opcao_escolhida = int(event[0])
            if 1 <= opcao_escolhida <= len(opcoes):
                window.close()
                return opcao_escolhida
            
        except:Exception


    def verifica_numero_inteiro(self,mensagem, inteiros_validos):
        while True:
            try:
                input_manual = input(mensagem)
                input_manual_em_int = int(input_manual)
                return input_manual_em_int
            except ValueError:
                print("                voce digitou valores incorretos, por favor, insira novamente.")
                print(f"                valore inteiros validos : {inteiros_validos}")

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear') or None
