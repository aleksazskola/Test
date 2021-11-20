import pygame

pygame.init()

monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
sirina = monitor[0] / 2
visina = monitor[1] / 2
prozor = pygame.display.set_mode((sirina, visina), pygame.RESIZABLE)