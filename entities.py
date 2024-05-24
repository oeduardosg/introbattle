#entities.py

import pygame

class Entity(pygame.sprite.Sprite):
    """ 
    Properties:
    hp_max : Maximum points of health
    hp_current: Current points of health
    atk : Points of damage
    dfn : Defense points
    """

    def __init__(self, hp, atk, dfn):
        self.hp_max = hp
        self.hp_current = hp
        self.atk = atk
        self.dfn = dfn

    def restore_all_hp(self):
        self.hp_current = self.hp_max

    def restore_hp(self, restore):
        self.hp_current += restore

    def receive_atk(self, attack):
        self.hp_current -= attack

    #Getters and setters
