## Xadrez Simplificado
Para iniciar o game, execute o arquivo main.py.


### Descrição do sistema:

O objetivo/problema do projeto é replicar um jogo de xadrez sem regras especiais, se diferenciando do xadrez normal por não ter em peasant, rock, casa dupla do peão, transformação do peão e permitir o suicídio do rei. Essas decisões surgiram como uma maneira de simplificar o desenvolvimento do jogo, mais tarde percebemos que não seria difícil de implementar, mas decidimos manter as mudanças para diferenciar o jogo do xadrez convencional.

O escopo do projeto era criar um jogo funcional, onde o jogador humano pudesse cadastrar seu usuario, jogar contra um bot ou contra outro jogador através de uma tela que simulasse o tabuleiro e no fim de cada partida receber seu histórico de jogadas.

As regras de negócio são muito semelhantes as do xadrez convencional. A cada turno, um único jogador/bot pode realizar uma única jogada, alternando entre si e o adversário. O jogador principal sempre jogará com as brancas. Os elementos principais do jogo são o tabuleiro e as peças. As peças são objetos instanciados, o tabuleiro uma matriz 8x8 composta por peças e casas vazias. Cada peça tem sua própria lógica de movimento incluindo direção e número de casas. Uma peça só pode se mover para determinada posição se esta posição estiver dentro de sua lógica de movimentação e estiver vazia ou ocupada por uma peça inimiga, nunca por uma peça aliada. Diferente do xadrez tradicional, aqui o jogo acaba com a morte do Rei, pois o Rei pode se mover para casas onde está sendo ameaçado, cabendo ao jogador adversário capturar ou não o Rei, o jogo também pode acabar por desistencia caso assim o jogador decida. 


### Requisitos:

Cadastro: Jogador, jogadas e pecas.

Registro: Histórico de jogadas

Relatorio: Histórico de jogadas, jogador vencedor e turnos

Herança: Peças e telas

Composição: jogada é uma composicao de Jogo

Agregação: Player é uma agregaçao de Jogo e Jogoda.

### O que cada um fez:
Guilherme: Fez os modelos das peças, trabalhou com o controlador jogo na criação do tabuleiro, na verificação de cheque e cheque mate, na movimentação das peças player e na criação da tela de regras.

Lucas: Trabalhou nos modelos jogada, jogo e player. Fez o controle central, a maior parte das telas e dos controladores que interagem com elas. Dentro do controle jogo trabalhou na criação do bot e da movimentaçao da peça pelo bot, da simulação e dos menus.
