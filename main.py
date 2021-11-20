import pygame, sys

pygame.init()

monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
sirina = monitor[0] / 2
visina = monitor[1] / 2
prozor = pygame.display.set_mode((sirina, visina))

pygame.display.set_caption("Test")

while True:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()