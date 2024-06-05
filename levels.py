import pygame
from entities import *

WIDTH = 1024
LENGHT = 768

def level_1(characters, enemies, window, background_level, clock, fps):
    characters_list = characters.sprites()
    characters_list[0].x_y(50, 50)
    characters_list[1].x_y(100, 100)
    characters_list[2].x_y(50, 150)

    enemies_list = enemies.sprites()
    enemies_list[0].x_y(500, 75)
    enemies_list[1].x_y(500, 125)

    for character in characters:
        character.draw(window)

    for enemy in enemies:
        enemy.draw(window)

    clock.tick(fps)
    pygame.display.flip()

    while True:
        pygame.display.flip()