#entities.py

import pygame

CHARACTER_SCALE = 0.6
SPIDER_SCALE = 0.45

class Entity(pygame.sprite.Sprite):
    """ 
    Properties:
    hp_max : Maximum points of health
    hp_current: Current points of health
    atk : Points of damage
    dfn : Defense points
    spd : Speed points
    x : x position
    y : y position
    image: Visual representation

    special_cooldown: Cooldown to reuse a special hability
    """

    def __init__(self, hp, atk, dfn, spd, image, team):
        super().__init__()
        self.hp_max = hp
        self.hp_current = hp
        self.atk = atk
        self.dfn = dfn
        self.spd = spd
        self.x = 0
        self.y = 0
        self.image = image
        self.team = team

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
    
    def get_team(self):
        return self.team
    
    def get_class_name(self):
        return self.__class__.__name__
    
    def alive(self):
        return self.hp_current > 0

    #Setters

    def restore_all_hp(self):
        self.hp_current = self.hp_max

    def die(self):
        self.hp_current = 0

    def x(self, x):
        self.x = x

    def y(self, y):
        self.y = y

    def x_y(self, x, y):
        self.x = x
        self.y = y

    def image(self, image):
        self.image = image

    def team(self, team):
        self.team = team

    #Others

    def restore_hp(self, restore):
        self.hp_current += restore

    def receive_atk(self, attack):
        if self.hp_current - attack <= 0:
            self.die()
        else: self.hp_current -= attack

    def attack(self, enemy):
        enemy.receive_atk(self.get_atk())

    def draw(self, window):
        window.blit(self.image, [self.x, self.y])

    def attack_info(self, window):
        font = pygame.font.Font(None, 50)
        text = font.render(f"You are selecting {self.get_class_name()}", True, (255, 255, 255))
        window.blit(text, [100, 650])

        font = pygame.font.Font(None, 25)
        text = font.render(f"Press Z to attack!", True, (255, 255, 255))
        window.blit(text, [100, 700])

    def health_info(self, window):
        font = pygame.font.Font(None, 25)
        text = font.render(f"{self.get_hp_current()}/{self.get_hp_max()}", True, (255, 255, 255))
        window.blit(text, [self.x, self.y])

#Wigfrid
class Wigfrid(Entity):
    """
    Wigfrid can instantly kill her enemies if their current hp is under 20% of the max hp.
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/wigfrid/wigfrid_base.png")
        image = pygame.transform.scale_by(image, CHARACTER_SCALE)
        super().__init__(150, 20, 50, 25, image, 1)
        self.counter = 0

    def attack(self, enemy):
        if(enemy.get_hp_current() < (enemy.get_hp_max() / 5)):
            enemy.die()
        else:
            enemy.receive_atk(self.get_atk())

#WX-78
class WX78(Entity):
    """
    WX-78 has a special hability to eat gears dropped by its enemies and become restore health
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/wx78/wx78_base.png")
        image = pygame.transform.scale_by(image, CHARACTER_SCALE)
        super().__init__(125, 25, 25, 50, image, 1)

    def special(self, enemy):
        if(enemy.get_current_hp() < self.get_atk()):
            self.restore_hp(enemy.get_current_hp())
            enemy.die()
        else:
            self.restore_hp(self.get_atk())
            self.attack(enemy)

#Wormwood
class Wormwood(Entity):
    """
    Wormood loves all of his friends and cures them
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/wormwood/wormwood_base.webp")
        image = pygame.transform.scale_by(image, CHARACTER_SCALE + 0.1)
        super().__init__(125, 10, 35, 25, image, 1)

    def special(self, ally):
        ally.restore_hp(30)

#Wickerbottom
class Wickerbottom(Entity):
    """
    Wickerbottom is a powerful librarian who can summon lightning bolts!
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/wickerbottom/wickerbottom_base.webp")
        image = pygame.transform.scale_by(image, CHARACTER_SCALE)
        super().__init__(100, 15, 25, 35, image, 1)

    def special(self, enemies):
        for enemy in enemies:
            enemy.receive_atk(self.get_atk())

#Willow
class Willow(Entity):
    """
    Willow just sets fire to everything and *everyone*
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/willow/willow_base.png")
        image = pygame.transform.scale_by(image, CHARACTER_SCALE)
        super().__init__(115, 20, 15, 50, image, 1)

    def special(self, enemie):
        enemie #on fire

#Spider
class Spider(Entity):
    """
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/spider/spider_base.webp")
        image = pygame.transform.scale_by(image, SPIDER_SCALE)
        super().__init__(50, 15, 10, 30, image, 0)

    def special(self, enemy):
        enemy
        #Não consegue jogar por um turno

#Maxwell
class Maxwell(Entity):
    """
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/maxwell/maxwell_base.webp")
        image = pygame.transform.scale_by(image, CHARACTER_SCALE)
        super().__init__(250, 20, 20, 30, image, 0)

    def special(self, allies):
        if(len(allies.sprites()) == 1):
            allies.add(Spider())
            return 1
        else:
            return 0