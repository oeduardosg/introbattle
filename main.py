import pygame
from entities import *
from menu import *

pygame.init()

#Creating the window
WIDTH = 1024
LENGHT = 768

window = pygame.display.set_mode((WIDTH, LENGHT))
pygame.display.set_caption("Don't Starve by Them")

#Adjusting the menu background size
background_menu = pygame.image.load("images/backgrounds/background_1.webp").convert()
h = background_menu.get_width()
background_menu = pygame.transform.scale_by(background_menu, WIDTH/h)

#Adjusting the selection background
background_selection = pygame.image.load("images/backgrounds/background_1.webp")    #ADICIONAR!!!!!!!!!!!!!!!!!!!!!

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

    run = menu(window, background_menu, clock, fps)
    if run == 1:
        run = selection(characters, window, background_selection, clock, fps)
        #if run:
            #run = level(characters, enemies, window, background_level, clock, fps)

pygame.quit()