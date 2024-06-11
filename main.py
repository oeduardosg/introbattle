import pygame
from entities import *
from menu import *
from levels import *

pygame.init()

#Creating the window
WIDTH = 1024
LENGHT = 768

window = pygame.display.set_mode((WIDTH, LENGHT))
pygame.display.set_caption("Don't Starve by Them")

#Adjusting the menu background size
background_menu = pygame.image.load("images/backgrounds/background_1.webp")
h = background_menu.get_width()
background_menu = pygame.transform.scale_by(background_menu, WIDTH/h)

#Adjusting the selection background
background_selection = pygame.image.load("images/backgrounds/selection_1.png")
h = background_selection.get_height()
background_selection = pygame.transform.scale_by(background_selection, LENGHT/h)

#Adjusting the level 1 background
background_level = pygame.image.load("images/backgrounds/level_1.jpg")
h = background_level.get_width()
background_level = pygame.transform.scale_by(background_level, WIDTH/h)

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
        if run:
            run = level_1(characters, enemies, window, background_level, clock, fps)

pygame.quit()