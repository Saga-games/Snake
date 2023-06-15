import pygame
from pygame.locals import *

pygame.init()

ESQUERDA = K_LEFT
DIREITA = K_RIGHT
CIMA = K_UP
BAIXO = K_DOWN

# TELA
tamanho_tela = (600,600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Jogo da Cobrinha")

# COBRINHA
cobrinha_pos = [(300,300)]
cobrinha_sup = pygame.Surface((10,10))
cobrinha_sup.fill((255, 255, 255))
cobrinha_dir = ESQUERDA

# MACA

while True:

    tela.fill((0,0,0))

    # VERIFICAR EVENTOS
    for event in pygame.event.get():

        # SE CLICAR EM FECHAR, FECHAR
        if event.type == QUIT:
            pygame.quit()
            quit()
      
    # DESENHANDO A COBRINHA
    for posicao in cobrinha_pos: 
        tela.blit(cobrinha_sup, posicao)

    pygame.display.update()
