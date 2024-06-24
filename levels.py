import pygame
from entities import *

WIDTH = 1024
LENGHT = 768

def mega_blit(window, background, characters, enemies):
    window.blit(background, ((WIDTH - background.get_width()) / 2,0))

    for character in characters:
        character.draw(window)

    for enemy in enemies:
        enemy.draw(window)

def order_turns(turns_list):
    for i in range(0, len(turns_list)):
        for j in range(0, len(turns_list)):
            if(turns_list[i].get_spd() > turns_list[j].get_spd()):
                aux = turns_list[i]
                turns_list[i] = turns_list[j]
                turns_list[j] = aux

def level_1(characters, enemies, window, background_level, clock, fps):

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

    order_turns(turn)
    mega_blit(window, background_level, characters, enemies)

    clock.tick(fps)
    pygame.display.flip()

    entity_turn = 1
    selected_enemy = 1

    while True:
        for event in pygame.event.get():
            if turn[entity_turn - 1].get_team():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        selected_enemy = selected_enemy%2 + 1
                        mega_blit(window, background_level, characters, enemies)
                        enemies_list[selected_enemy - 1].info(window)

                    if event.key == pygame.K_UP:
                        selected_enemy = selected_enemy%2 - 1
                        mega_blit(window, background_level, characters, enemies)
                        enemies_list[selected_enemy - 1].info(window)
                        
                    if event.key == pygame.K_z:
                        #if event.key == pygame.K_x:
                            #go back
                        turn[entity_turn - 1].attack(enemies_list[selected_enemy - 1])
                        entity_turn = entity_turn%5 + 1
                        selected_enemy = 1
            
            else:
                entity_turn = entity_turn%5 + 1

            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    return 1
        
        pygame.display.flip()