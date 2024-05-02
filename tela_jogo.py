import pygame, sys
from utilitario import get_fonte

def jogar(screen):
    while True:

        screen.fill("black")

        TEXTO = get_fonte(45).render("IMPLEMENTAR JOGO AQUI se leu mamou", True, "White")
        TEXTO_RECT = TEXTO.get_rect(center=(640, 260))
        screen.blit(TEXTO, TEXTO_RECT)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()


