import pygame, sys

pygame.init()

monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
sirina = monitor[0]
visina = monitor[1]

prozor = pygame.display.set_mode((sirina, visina), pygame.FULLSCREEN)
pygame.display.set_caption("Test")
sat = pygame.time.Clock()

def gameloop():
    while True:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        tasteri = pygame.key.get_pressed()
        if tasteri[pygame.K_q]:
            pygame.quit()
            exit()

        pygame.display.update()
        sat.tick(60)

gameloop()