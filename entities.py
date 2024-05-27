#entities.py

import pygame

class Entity(pygame.sprite.Sprite):
    """ 
    Properties:
    hp_max : Maximum points of health
    hp_current: Current points of health
    atk : Points of damage
    dfn : Defense points
    spd : Speed points
    special: Special hability

    x : x position
    y : y position
    image: Visual representation
    """

    def __init__(self, hp, atk, dfn, spd):
        super().__init__
        self.hp_max = hp
        self.hp_current = hp
        self.atk = atk
        self.dfn = dfn
        self.spd = spd

    #Getters

    def get_hp_max(self):
        return self.hp_max
    
    def get_hp_current(self):
        return self.hp_current
    
    def get_atk(self):
        return self.atk
    
    def get_dfn(self):
        return self.dfn
    
    def get_spd(self):
        return self.spd

    #Setters

    def restore_all_hp(self):
        self.hp_current = self.hp_max

    #Others

    def restore_hp(self, restore):
        self.hp_current += restore

    def receive_atk(self, attack):
        self.hp_current -= attack

    def attack(self, enemie):
        enemie.receive_atk(self.get_atk())



class Paladin(Entity):
    """
    Properties:
    """

    def __init__(self):
        super().__init__(150, 20, 50, 25)
        self.counter = 0

    def special(self, enemie):
        # if(enemie.get_hp_current() < (enemie.get_hp_max() / 4)): ... Deixar isso pra outra hora
        enemie

           
class Rogue(Entity):
    """
    """

    def __init__(self):
        super().__init__(125, 25, 25, 50)


class Cleric(Entity):
    """
    """

    def __init__(self):
        super().__init__(125, 10, 35, 25)

    def special(self, ally):
        ally.restore_hp(30)

class Wizard(Entity):
    """
    """

    def __init__(self):
        super().__init__(100, 15, 25, 35)

    def special(self, enemies):
        for i in len(enemies):
            enemies[i].receive_atk(self.get_atk())

class Hunter(Entity):
    """
    """

    def __init__(self):
        super().__init__(115, 20, 15, 50)