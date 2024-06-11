import pygame
from entities import *

WIDTH = 1024
LENGHT = 768

def level_1(characters, enemies, window, background_level, clock, fps):

    window.blit(background_level, ((WIDTH - background_level.get_width()) / 2,0))

    characters_list = characters.sprites()
    characters_list[0].x_y(120, 120)
    characters_list[1].x_y(220, 260)
    characters_list[2].x_y(120, 400)

    enemies_list = enemies.sprites()
    enemies_list[0].x_y(650, 160)
    enemies_list[1].x_y(670, 460)

    turn = []

    for character in characters_list:
        turn.append(character)

    for enemy in enemies_list:
        turn.append(enemy)

    for character in characters:
        character.draw(window)

    for enemy in enemies:
        enemy.draw(window)

    clock.tick(fps)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if pygame.K_a:
                    return 1
        pygame.display.flip()