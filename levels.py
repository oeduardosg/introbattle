import pygame
from random import randint
from entities import *

WIDTH = 1024
LENGHT = 768

def order_turns(turns_list):
    for i in range(0, len(turns_list)):
        for j in range(0, len(turns_list)):
            if(turns_list[i].get_spd() > turns_list[j].get_spd()):
                aux = turns_list[i]
                turns_list[i] = turns_list[j]
                turns_list[j] = aux

def level_1(characters, enemies, window, background_level, clock, fps):

    characters_list = characters.sprites()
    characters_list[0].x_y(120, 60)
    characters_list[1].x_y(220, 200)
    characters_list[2].x_y(120, 340)

    enemies_list = enemies.sprites()
    enemies_list[0].x_y(650, 100)
    enemies_list[1].x_y(670, 400)

    turn = []

    for character in characters_list:
        turn.append(character)

    for enemy in enemies_list:
        turn.append(enemy)

    order_turns(turn)
    mega_blit(window, background_level, characters, enemies)

    clock.tick(fps)
    pygame.display.flip()

    entity_turn = 1

    while True:
        for event in pygame.event.get():

            characters_win = 1
            enemies_win = 1

            for entity in turn:
                if entity.alive():
                    if entity.get_team():
                        enemies_win = 0
                    else:
                        characters_win = 0

            if characters_win: return 1
            if enemies_win: return 0

            if turn[entity_turn - 1].alive():
                turn[entity_turn - 1].action(window, background_level, characters_list, enemies_list)
            entity_turn += 1
            if entity_turn > len(turn):
                entity_turn = 1
                
            for entity in turn:
                entity.decrease_cooldown()
                if entity.is_on_fire():
                    entity.receive_atk(3)

            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()