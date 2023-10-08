from classes.controles.controle_jogo import ControleJogo

jogo = ControleJogo()
jogo.tabuleiro[0][0].posicao = [1,2]
jogo.sincronizar_posicoes_tabuleiro()
print(jogo.tabuleiro[0][0].posicao)
