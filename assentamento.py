from casa import *
from tituloAssentamento import *

class Assentamento(Casa):
    def __init__(self, id, distanceToNext, name, titulo):
        # Inicializa a classe base Casa
        super().__init__(id, distanceToNext, name)
        self.titulo = titulo  # Atribui um título à propriedade
        self.titulo.casa = self  # Define a propriedade do título como esta casa
        self.fortalezas = 0  # Inicializa o número de fortalezas na propriedade

    def ativarEvento(self, jogador):
        # Método chamado quando um jogador cai nesta casa
        if not self.titulo.comprado:
            # Se o título não foi comprado, pergunta ao jogador se ele quer comprar
            if jogador.controlador.controlar("Comprar Casa"):
                self.comprar(jogador)
        else:
            if jogador != self.titulo.jogador:
                # Se a casa pertence a outro jogador, cobra aluguel
                valorDim = jogador.modificarSuprimentos(-self.titulo.custo)
                self.titulo.jogador.modificarSuprimentos(-valorDim)
            else:
                if self.titulo.grupo.verificarPosseGrupo(jogador):
                    # Se o jogador possui todo o grupo de propriedades, permite construir fortaleza
                    self.construirFortaleza(jogador)
    
    def comprar(self, jogador):
        # Método para comprar a propriedade
        jogador.modificarSuprimentos(-self.titulo.custo)  # Deduz o custo do jogador
        self.titulo.atribuirAJogador(jogador)  # Atribui o título ao jogador
        jogador.ganharTitulo(self.titulo)  # Adiciona o título ao jogador

    def construirFortaleza(self, jogador):
        # Método para construir uma fortaleza na propriedade
        jogador.modificarSuprimentos(-self.titulo.custo)  # Deduz o custo do jogador
        self.fortalezas += 1  # Incrementa o número de fortalezas
        self.titulo.custo *= 2  # Dobra o custo do título

    def drawCasa(self, coord, fonte, fonteFortaleza, screen):
        # Método para desenhar a propriedade na tela
        # Ajusta o texto para ficar bem posicionado dependendo da casa
        if self.distanceToNext[1] < -70:
            coord[0] -= 10
            coord[1] -= 10
        if self.distanceToNext[1] > 70:
            coord[0] += 36
            coord[1] -= 20
        if self.distanceToNext[0] > 70:
            coord[1] -= 6
        if self.distanceToNext[0] < -70:
            coord[1] += 3
        if self.id > 10 and self.id < 16:
            coord[0] += 3 + (self.id - 12) / 1
        coord[1] -= 10

        # Dependendo do estado da casa, mostra as informações
        if self.titulo.jogador is None:
            textoCasa = fonte.render('    Sem dono  ', True, (255, 255, 255))
        else:
            if not self.titulo.jogador.isZombie():
                textoCasa = fonte.render(
                    f'  Do jogador {self.titulo.jogador.id + 1} ', True, (255, 255, 255))
            else:
                textoCasa = fonte.render(' Horda zumbi  ', True, (255, 255, 255))
        
        # Se há fortalezas, desenha o número de fortalezas
        if self.fortalezas > 0:
            textoFortaleza = fonteFortaleza.render(
                f'  Fortalezas: {self.fortalezas} ', True, (255, 255, 255))
        
        # Desenha as informações na tela
        screen.blit(textoCasa, coord)
