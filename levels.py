import pygame
from random import randint
from entities import *

WIDTH = 1024
LENGHT = 768

def mega_blit(window, background, characters, enemies):
    window.blit(background, ((WIDTH - background.get_width()) / 2,0))

    for character in characters:
        character.draw(window)
        character.health_info(window)

    for enemy in enemies:
        enemy.draw(window)
        enemy.health_info(window)

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

            if(len(enemies_list) == 0):
                return 1
            if(len(characters_list) == 0):
                return 0

            if turn[entity_turn - 1].get_team():

                if event.type == pygame.KEYDOWN:

                    mega_blit(window, background_level, characters, enemies)
                    enemies_list[selected_enemy - 1].attack_info(window)

                    if event.key == pygame.K_DOWN:
                        selected_enemy = selected_enemy%len(enemies_list) + 1
                        print(selected_enemy)
                        mega_blit(window, background_level, characters, enemies)
                        enemies_list[selected_enemy - 1].attack_info(window)

                    if event.key == pygame.K_UP:
                        selected_enemy = selected_enemy%len(enemies_list) - 1
                        print(selected_enemy)
                        if(selected_enemy < 0):
                            selected_enemy = 1

                        mega_blit(window, background_level, characters, enemies)
                        enemies_list[selected_enemy - 1].attack_info(window)

                    if event.key == pygame.K_z:
                        if event.key == pygame.K_x:
                            continue

                        turn[entity_turn - 1].attack(enemies_list[selected_enemy - 1])
                        entity_turn = entity_turn%len(turn) + 1
                        selected_enemy = 1

                        if not(enemies_list[selected_enemy - 1].alive()):

                            enemies_list.pop(selected_enemy - 1)
                            print("An enemy was removed from the list!")
                            print(len(enemies_list))
                            
            else:
                if(turn[entity_turn - 1].alive):
                    if turn[entity_turn - 1].active_special():
                        turn[entity_turn - 1].special(enemies_list)
                        turn[entity_turn - 1].reset_cooldown()
                    else:
                        turn[entity_turn - 1].decrease_cooldown()
                    num = randint(0, 2)
                    while num:
                        if characters_list[num].alive:
                            turn[entity_turn - 1].attack(characters_list[num])
                            break
                        else:
                            num = randint(0, 2)
                    entity_turn = entity_turn%len(turn) + 1

            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()