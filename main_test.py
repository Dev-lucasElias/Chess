
from classes.controles.controle_jogo import ControleJogo
from classes.controles.controle_central import ControleCentral
controle = ControleCentral()
jogo = ControleJogo(controle)
jogo.abre_tela_jogo()
