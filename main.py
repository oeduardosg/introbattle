import pygame
from entities import *

pygame.init()

#Creating the window
WIDTH = 1024
LENGHT = 768

window = pygame.display.set_mode((WIDTH, LENGHT))
pygame.display.set_caption("Don't Starve by Them")

#Adjusting the background size
menu = pygame.image.load("images/menu_backgrounds/background_1.webp")
h = menu.get_width()
menu = pygame.transform.scale_by(menu, WIDTH/h)

#Creating the main groups
characters = pygame.sprite.Group()

enemies = pygame.sprite.Group()
enemies.add(Necromancer())
enemies.add(Spider())

#Setting the game tick
fps = 60
clock = pygame.time.Clock()

run = True

while run:
    window.blit(menu, (0,0))
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

    pygame.display.flip()

pygame.quit()