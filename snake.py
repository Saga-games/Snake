import pygame

pygame.init()

# TELA
tamanho_tela = (600,600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Jogo da Cobrinha")

# COBRINHA
cobrinha_pos = [(300,300)]
cobrinha_sup = pygame.Surface((10,10))
cobrinha_sup.fill = ((255, 255, 255))

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
          tela.blit(cobrinha_sup, cobrinha_pos)

      pygame.display.update()
