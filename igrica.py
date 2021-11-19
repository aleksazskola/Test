import pygame as pg

pygame.init()

monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
sirina = monitor[0] * 50%
visina = monitor[1] * 50%
prozor = pygame.display.set_mode((sirina, visina))