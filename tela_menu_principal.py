import pygame, sys
from botao import Botao
from utilitario import get_fonte, get_bg, get_fonte_titulo
from tela_opcoes import opcoes
from tela_qtd_jogadores import selecionar_qtd_jogadores

BG = get_bg()

def menu_principal(screen):
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_fonte_titulo(115).render("THE LAST OF MONOPOLY", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        BOTAO_JOGAR = Botao(image=pygame.image.load("assets/retangulo.png"), pos=(640, 250), 
                    text_input="JOGAR", font=get_fonte(65), base_color="#FFFFFF", hovering_color="White", y_offset=5)
        BOTAO_OPCOES = Botao(image=pygame.image.load("assets/retangulo.png"), pos=(640, 400), 
                        text_input="OPÇÕES", font=get_fonte(65), base_color="#FFFFFF", hovering_color="White", y_offset=0)
        BOTAO_SAIR = Botao(image=pygame.image.load("assets/retangulo.png"), pos=(640, 550), 
                    text_input="SAIR", font=get_fonte(65), base_color="#FFFFFF", hovering_color="White", y_offset=5)

        screen.blit(MENU_TEXT, MENU_RECT)

        for botao in [BOTAO_JOGAR, BOTAO_OPCOES, BOTAO_SAIR]:
            botao.changeColor(MENU_MOUSE_POS)
            botao.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTAO_JOGAR.checkForInput(MENU_MOUSE_POS):
                    selecionar_qtd_jogadores(screen)

                if BOTAO_OPCOES.checkForInput(MENU_MOUSE_POS):
                    opcoes(screen)

                if BOTAO_SAIR.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
