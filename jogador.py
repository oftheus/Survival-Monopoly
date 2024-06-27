import pygame
from utilitario import *
from tela_qtd_jogadores import *
from peca import *
from stateJogador import *
from stateSobrevivente import *
from stateZumbi import *

class Jogador:
    def __init__(self, controlador, id_jogador, pos_inicial, jogadorSprite, tabuleiro):
        self.id = id_jogador
        self.controlador = controlador
        self.controlador.jogador = self
        self.pos_inicial = pos_inicial
        self.suprimentos = 1500  # Quantidade inicial de "dinheiro" para cada jogador
        self.imagem = pygame.image.load(
            # Carrega a imagem do jogador
            f"assets/peao{id_jogador + 1}.png").convert_alpha()
        self.imagem = pygame.transform.scale(
            self.imagem, (28, 30))  # Redimensiona a imagem
        self.peca = Peca(self.pos_inicial, jogadorSprite, tabuleiro)
        self.estado = SobreviventeState()
        self.titulos = []
        self.preso = False
        self.rodadasPreso = 0
        self.cartasEscape = 0

    def modificarSuprimentos(self,qtd):
        #comportamento pode ser, por polimorfismo, alterado no zumbi
        return self.estado.atualizarSuprimentos(self,qtd)

    def encurrala(self):
        self.estado.encurralar(self)

    def libera(self):
        self.preso = False
        self.rodadasPreso = 0
        
    def podeMover(self):
        if self.preso:
            return self.estado.tentarFugir(self)
        else:
            return True
        
    def renderizar_suprimento(self, font, screen, colorVector):
        # Renderiza o formato de fundo
        suprimento_bg_rect = pygame.Rect(200 + self.id * 150, 200, 80, 30)
        pygame.draw.rect(screen, (((184, 219, 211))), suprimento_bg_rect,
                         border_radius=15)  # Retângulo arredondado

        # Ajusta a posição com base no id do jogador
        screen.blit(self.imagem, (200 + self.id * 148, 200))
        if not self.isZombie() and not self.preso:
            texto_suprimento = font.render(
                f"{self.suprimentos}", True, (colorVector))
        elif self.isZombie():
            if colorVector == (0,0,0):
                texto_suprimento = font.render("Morto", True, (	22, 68, 47))
            else:
                texto_suprimento = font.render("Morto", True, colorVector)
        else:
            texto_suprimento = font.render("Preso", True, colorVector)
        # Ajusta a posição com base no id do jogador
        screen.blit(texto_suprimento, (230 + self.id * 150, 202))

    def transforma_zumbi(self):
        self.peca.jogadorSprite.atualizaImage("assets/zumbi.png")
        #= JogadorSprite(
        #    "assets/zumbi.png", (55, 80),  (50, 700))
        #self.peca.casa = self.pos_inicial
        self.estado = ZumbiState()
        # print(self.peca.jogadorSprite.image)
        # algo com state ou outro modo de implementar

    def isZombie(self):
        return self.estado.isZombie()
    
    def ganharTitulo(self, titulo):
        self.titulos.append(titulo)

    def usarCartaDistracao(self):
        self.estado.tentarFugir(self)

    def ganharCartaEscape(self):
        self.cartasEscape += 1

class JogadorSprite(pygame.sprite.Sprite):
    def __init__(self, imagePath, size, posicao_inicial):
        super().__init__()
        # Carrega a imagem do peão do jogador
        self.imagem = pygame.image.load(imagePath).convert_alpha()
        self.size = size
        self.imagem = pygame.transform.scale(
            self.imagem, size)  # Redimensiona a imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = posicao_inicial  # Define a posição inicial

    def atualizaImage(self, newImagePath):
        pos = self.rect.topleft
        self.imagem = pygame.image.load(newImagePath).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (40,70))  # Redimensiona a imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = pos