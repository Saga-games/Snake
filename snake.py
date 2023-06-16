import pygame
from pygame.locals import *
import random

pygame.init()

ESQUERDA = pygame.locals.K_LEFT
DIREITA = pygame.locals.K_RIGHT
CIMA = pygame.locals.K_UP
BAIXO = pygame.locals.K_DOWN

passo = 10

# TELA
tamanho_tela = (600, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Jogo da Cobrinha")

# COBRINHA
cobrinha_pos = [(300, 300)]
cobrinha_sup = pygame.Surface((10, 10))
cobrinha_sup.fill((255, 255, 255))
cobrinha_dir = ESQUERDA

# MACA


def gerar_posicao_aleatoria():
    x = random.randint(0, tamanho_tela[0])
    y = random.randint(0, tamanho_tela[1])
    x = x // passo * passo
    y = y // passo * passo
    return x, y


maca_pos = gerar_posicao_aleatoria()
maca_sup = pygame.Surface((10, 10))
maca_sup.fill((255, 0, 0))

while True:

    pygame.time.Clock().tick(15)

    # LIMPAR O DISPLAY
    tela.fill((0, 0, 0))

    # VERIFICAR EVENTOS
    for event in pygame.event.get():

        # SE CLICAR EM FECHAR, FECHAR
        if event.type == QUIT:
            pygame.quit()
            quit()

    # VERIFICAR O BOTAO CLICADO PARA MOVIMENTAR
    if event.type == KEYDOWN:
        if event.key in [ESQUERDA, DIREITA, CIMA, BAIXO]:
            cobrinha_dir = event.key

    # DESENHANDO A COBRINHA
    for posicao in cobrinha_pos:
        tela.blit(cobrinha_sup, posicao)

    # DESENHANDO A MACA
    tela.blit(maca_sup, maca_pos)

    if cobrinha_dir == DIREITA:
        cobrinha_pos[0] = cobrinha_pos[0][0] + passo, cobrinha_pos[0][1]
    if cobrinha_dir == ESQUERDA:
        cobrinha_pos[0] = cobrinha_pos[0][0] - passo, cobrinha_pos[0][1]
    if cobrinha_dir == CIMA:
        cobrinha_pos[0] = cobrinha_pos[0][0], cobrinha_pos[0][1] - passo
    if cobrinha_dir == BAIXO:
        cobrinha_pos[0] = cobrinha_pos[0][0], cobrinha_pos[0][1] + passo

    pygame.display.update()