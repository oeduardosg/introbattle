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

    special_cooldown: Cooldown to reuse a special hability
    x : x position
    y : y position
    image: Visual representation
    """

    def __init__(self, hp, atk, dfn, spd):
        super().__init__()
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

    def die(self):
        self.hp_current = 0

    #Others

    def restore_hp(self, restore):
        self.hp_current += restore

    def receive_atk(self, attack):
        self.hp_current -= attack

    def attack(self, enemy):
        enemy.receive_atk(self.get_atk())


#Wigfrid
class Paladin(Entity):
    """
    Wigfrid can instantly kill her enemies if their current hp is under 20% of the max hp.
    """

    def __init__(self):
        super().__init__(150, 20, 50, 25)
        self.counter = 0

    def attack(self, enemy):
        if(enemy.get_hp_current() < (enemy.get_hp_max() / 5)):
            enemy.die()
        else:
            enemy.receive_atk(self.get_atk())

#WX-78
class Rogue(Entity):
    """
    Wortox special hability steals an enemy hp based on his attack
    """

    def __init__(self):
        super().__init__(125, 25, 25, 50)

    def special(self, enemy):
        if(enemy.get_current_hp() < self.get_atk()):
            self.restore_hp(enemy.get_current_hp())
            enemy.die()
        else:
            self.restore_hp(self.get_atk())
            self.attack(enemy)

#Wormwood
class Cleric(Entity):
    """
    Wormood loves all of his friends and cures them
    """

    def __init__(self):
        super().__init__(125, 10, 35, 25)

    def special(self, ally):
        ally.restore_hp(30)

#Wickerbottom
class Wizard(Entity):
    """
    Wickerbottom is a powerful librarian who can summon lightning bolts!
    """

    def __init__(self):
        super().__init__(100, 15, 25, 35)

    def special(self, enemies):
        for enemy in enemies:
            enemy.receive_atk(self.get_atk())

#Willow
class Hunter(Entity):
    """
    Willow just sets fire to everything and *everyone*
    """

    def __init__(self):
        super().__init__(115, 20, 15, 50)

    def special(self, enemie):
        enemie #on fire

#Spider
class Spider(Entity):
    """
    """

    def __init__(self):
        super().__init__(50, 15, 10, 30)

    def special(self, enemy):
        enemy
        #Não consegue jogar por um turno

#Maxwell
class Necromancer(Entity):
    """
    """

    def __init__(self):
        super().__init__(250, 20, 20, 30)

    def special(self, allies):
        if(len(allies.sprites()) == 1):
           allies.add(Spider())
        else:
            return 0