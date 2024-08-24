#entities.py

import pygame
from random import *

CHARACTER_SCALE = 0.6
SPIDER_SCALE = 0.45

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

    pygame.draw.rect(window, (128, 128, 128), pygame.Rect(0, 575, 1024, 768))
                     
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
        self.cooldown = 15
        self.x = 0
        self.y = 0
        self.image = image
        self.team = team
        self.webbed = 0
        self.onfire = 0
        self.resist = 0

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
    
    def resisting(self):
        return self.resist

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

    def reset_cooldown(self):
        self.cooldown = 15

    def web(self):
        self.webbed = 5

    def defend(self):
        self.resist = 1

    def remove_resist(self):
        self.resist = 0

    #Others

    def restore_hp(self, restore):
        self.hp_current += restore

    def receive_atk(self, attack):
        if self.resisting():
            self.hp_current -= int(attack * (50 / (100 + self.dfn)))
            self.remove_resist()
        else:
            self.hp_current -= int(attack * (50 / (50 + self.dfn)))
        if self.hp_current < 0: self.hp_current = 0

    def attack(self, enemy):
        enemy.receive_atk(self.get_atk())

    def draw(self, window):
        window.blit(self.image, [self.x, self.y])
        if self.webbed:
            image = pygame.image.load(f"images/entities/effects/webbed.webp")
            image = pygame.transform.scale_by(image, 0.3)
            window.blit(image, [self.x, self.y + 65])

        if self.onfire:
            image = pygame.image.load(f"images/entities/effects/fire.webp")
            image = pygame.transform.scale_by(image, 0.3)
            window.blit(image, [self.x + 30, self.y + 90])

    def attack_info(self, window):
        font = pygame.font.Font(None, 50)
        text = font.render(f"You are selecting {self.get_class_name()}", True, (0, 0, 0))
        window.blit(text, [100, 650])

        font = pygame.font.Font(None, 25)
        text = font.render(f"Press Z to attack!", True, (0, 0, 0))
        window.blit(text, [100, 700])

    def health_info(self, window):
        font = pygame.font.Font(None, 25)
        text = font.render(f"{self.get_hp_current()}/{self.get_hp_max()}", True, (255, 255, 255))
        window.blit(text, [self.x + 60, self.y + 210])

    def decrease_cooldown(self):
        if(self.cooldown != 0):
            self.cooldown -= 1

        if(self.webbed != 0):
            self.webbed -= 1

        if(self.onfire != 0):
            self.onfire -= 1

    def active_special(self):
        return self.cooldown == 0
    
    def turn_info(self, window):
        font = pygame.font.Font(None, 50)
        text = font.render(f"{self.get_class_name()}'s turn:", True, (0, 0, 0))
        window.blit(text, [100, 600])
    
    def action(self, window, background, characters, enemies):

        selected_option = 0
        selected_enemy = 0
        screen = 0

        if self.webbed:
            return

        while True:

            if screen == 0:
                mega_blit(window, background, characters, enemies)
                self.turn_info(window)
                font = pygame.font.Font(None, 50)
                text = font.render("Attack", True, (0, 0, 0))
                window.blit(text, [550, 600])
                text = font.render("Defend", True, (0, 0, 0))
                window.blit(text, [750, 600])
                text = font.render("Special", True, (0, 0, 0))
                window.blit(text, [550, 650])

                if selected_option == 0:
                    font = pygame.font.Font(None, 50)
                    text = font.render("Attack", True, (255, 0, 0))
                    window.blit(text, [550, 600])

                if selected_option == 1:
                    font = pygame.font.Font(None, 50)
                    text = font.render("Defend", True, (255, 0, 0))
                    window.blit(text, [750, 600])

                if selected_option == 2:
                    font = pygame.font.Font(None, 50)
                    text = font.render("Special", True, (255, 0, 0))
                    window.blit(text, [550, 650])

            elif screen == 1:
                mega_blit(window, background, characters, enemies)
                enemies[selected_enemy].attack_info(window)
                self.turn_info(window)

            else:
                self.special(characters, enemies, window=window)
                return


            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:

                    if screen == 0:
                        mega_blit(window, background, characters, enemies)
                        self.turn_info(window)
                        font = pygame.font.Font(None, 50)
                        text = font.render("Attack", True, (0, 0, 0))
                        window.blit(text, [550, 600])
                        text = font.render("Defend", True, (0, 0, 0))
                        window.blit(text, [750, 600])
                        text = font.render("Special", True, (0, 0, 0))
                        window.blit(text, [550, 650])

                        if event.key == pygame.K_DOWN:
                            selected_option += 1
                            if selected_option > 2: selected_option = 0

                        if event.key == pygame.K_UP:
                            selected_option -= 1
                            if selected_option < 0: selected_option = 2

                        if selected_option == 0:
                            if event.key == pygame.K_z:
                                screen = 1

                        if selected_option == 1:
                            if event.key == pygame.K_z:
                                self.defend()
                                return

                        if selected_option == 2:
                            if event.key == pygame.K_z:
                                screen = 2

                    elif screen == 1:
                        mega_blit(window, background, characters, enemies)
                        enemies[selected_enemy].attack_info(window)
                        self.turn_info(window)

                        if event.key == pygame.K_DOWN:
                            selected_enemy += 1
                            if(selected_enemy > 1): selected_enemy = 0
                            mega_blit(window, background, characters, enemies)
                            enemies[selected_enemy].attack_info(window)
                            self.turn_info(window)

                        if event.key == pygame.K_UP:
                            selected_enemy -= 1
                            if(selected_enemy < 0): selected_enemy = 1
                            mega_blit(window, background, characters, enemies)
                            enemies[selected_enemy].attack_info(window)
                            self.turn_info(window)

                        if event.key == pygame.K_z:
                            self.attack(enemies[selected_enemy])
                            return
                        
                        if event.key == pygame.K_x:
                            screen = 0
            
                if event.type == pygame.QUIT:
                        pygame.quit()

            pygame.display.flip()


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

    def special(self, allies = None, enemies = None, ally = None, enemy = None, window = None):
        rand = randint(0, 1)
        while not(enemies[rand].alive()):
            rand = randint(0, 1)

        if(enemies[rand].get_hp_current() < self.get_atk()):
            self.restore_hp(enemies[rand].get_hp_current())
            enemies[rand].die()
        else:
            self.restore_hp(self.get_atk())
            self.attack(enemies[rand])

#Wormwood
class Wormwood(Entity):
    """
    Wormood loves all of his friends and cures them
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/wormwood/wormwood_base.webp")
        image = pygame.transform.scale_by(image, CHARACTER_SCALE + 0.1)
        super().__init__(125, 10, 35, 25, image, 1)

    def special(self, allies = None, enemies = None, ally = None, enemy = None, window = None):
        print(allies)
        rand = randint(0, 2)
        while not(allies[rand].alive()):
            rand = randint(0, 2)
        allies[rand].restore_hp(30)

    def health_info(self, window):
        font = pygame.font.Font(None, 25)
        text = font.render(f"{self.get_hp_current()}/{self.get_hp_max()}", True, (255, 255, 255))
        window.blit(text, [self.x + 60, self.y + 190])

#Wickerbottom
class Wickerbottom(Entity):
    """
    Wickerbottom is a powerful librarian who can summon lightning bolts!
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/wickerbottom/wickerbottom_base.webp")
        image = pygame.transform.scale_by(image, CHARACTER_SCALE)
        super().__init__(100, 15, 25, 35, image, 1)

    def special(self, allies = None, enemies = None, ally = None, enemy = None, window = None):
        for enemy in enemies:
            image = pygame.image.load(f"images/entities/effects/lightning_bolt.webp")
            image = pygame.transform.scale_by(image, 1)
            window.blit(image, [enemy.x - 20, enemy.y - 200])
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

    def special(self, allies = None, enemies = None, ally = None, enemy = None, window = None):
        rand = randint(0, 1)
        while not(enemies[rand].alive):
            rand = randint(0, 1)
        enemies[rand].onfire = 5

#Spider
class Spider(Entity):
    """
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/spider/spider_base.webp")
        image = pygame.transform.scale_by(image, SPIDER_SCALE)
        super().__init__(50, 15, 10, 30, image, 0)

    def special(self, allies = None, enemies = None, ally = None, enemy = None, window = None):
        enemy.web()
        print(enemy)
        print("Should have been webbed")
        self.reset_cooldown()

    def action(self, window, background, characters, enemies):
        print(f"Spider cooldown {self.cooldown}")
        if self.active_special():
            rand = randint(0, 2)
            while not(characters[rand].alive):
                rand = randint(0, 2)
            self.special(enemy=characters[rand])
        else:
            rand = randint(0, 2)
            while not(characters[rand].alive):
                rand = randint(0, 2)
            self.attack(characters[rand])

    def health_info(self, window):
        font = pygame.font.Font(None, 25)
        text = font.render(f"{self.get_hp_current()}/{self.get_hp_max()}", True, (255, 255, 255))
        window.blit(text, [self.x + 50, self.y + 75])

#Maxwell
class Maxwell(Entity):
    """
    """

    def __init__(self):
        image = pygame.image.load(f"images/entities/maxwell/maxwell_base.webp")
        image = pygame.transform.scale_by(image, CHARACTER_SCALE)
        super().__init__(250, 20, 20, 30, image, 0)

    def special(self, allies = None, enemies = None, ally = None, enemy = None, window = None):
        if not(ally.alive()):
            image = pygame.image.load(f"images/entities/effects/nightmare_fuel.webp")
            image = pygame.transform.scale_by(image, 0.8)
            window.blit(image, [ally.x + 50, ally.y + 40])
            ally.restore_all_hp()
            self.reset_cooldown()
        
    def action(self, window, background, characters, enemies):
        if self.active_special():
            self.special(ally=enemies[1], window=window)
        else:
            rand = randint(0, 2)
            while not(characters[rand].alive):
                rand = randint(0, 2)
            self.attack(characters[rand])