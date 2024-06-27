import pygame
import random
from utilitario import *

# Carregando imagens das faces dos dados
IMAGEMDOSDADOS = get_imagem_dados()

class Dado(pygame.sprite.Sprite):
    def __init__(self, images):
        super().__init__()
        self.images = images # Lista de imagens do dado
        self.image = self.images[0]  # Começa mostrando sendo a face 1 do dado 
        self.rect = self.image.get_rect() # Obtém o retângulo da imagem do dado, pra gente limitar quando clicar nele

    def rolar(self):
        resultado = random.randint(1, 6) # Gerar um número aleatório entre 1 e 6
        self.image = self.images[resultado - 1]  #Atualizar a imagem pra mostrar o resultado
        return resultado
    def draw(self, screen):
        screen.blit(self.image, self.rect) # Desenha a imagem do dado na tela usando o retângulo delimitador

# Criando sprite do dado
sprite_dado = Dado(IMAGEMDOSDADOS)
sprite_dado.rect.center = (990, 590) #posição do dado na tela

sprite_dado2 = Dado(IMAGEMDOSDADOS)
sprite_dado2.rect.center = (990, 505)
