import pygame as pg

pg.init()

monitor = [pg.display.Info().current_w, pg.display.Info().current_h]
sirina = monitor[0] / 2
visina = monitor[1] / 2
prozor = pg.display.set_mode((sirina, visina), pg.RESIZABLE)