from classes.controles.controle_jogo import ControleJogo

jogo = ControleJogo()
jogo.tabuleiro[0][3].posicao = [6,4]
print(jogo.verifica_cheque())
