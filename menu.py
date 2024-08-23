import pygame
from entities import *

WIDTH = 1024
LENGHT = 768

class Selection():

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.selectable = 1

    def selectable(self):
        self.selectable = 1

    def unselectable(self):
        self.selectable = 0

    def is_position(self, x, y):
        if(self.position[0] == x and self.position[1] == y): return 1
        return 0

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position
    
    def get_selectable(self):
        return self.selectable

def menu(window, background_menu, clock, fps):

    run = True
    while run:

        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(0, 0, 1024, 768))
        window.blit(background_menu, (0,0))

        font = pygame.font.Font(None, 76)
        text = font.render("Start", True, (255, 255, 255))
        window.blit(text, (850, 680))

        clock.tick(fps)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.K_a:
                    return 1
                

def selection(characters, window, background_selection, clock, fps):

    frame_image = pygame.image.load("images/selection_frame.png")
    h = frame_image.get_width()
    frame_image = pygame.transform.scale_by(frame_image, 290/h)

    x = 108
    y = 25
    count = 0
    
    main_x_up = 150
    main_x_down = 275
    main_x_variation = 250

    mid_pixel = LENGHT/2
    shift = 150
    upper_shift = mid_pixel - 2 * shift
    lower_shift = mid_pixel + LENGHT / 25

    delta_x = main_x_up - x
    delta_y = upper_shift - y


    characters_selection = []
    characters_selection.append(Selection("Wigfrid", [main_x_up, upper_shift]))
    characters_selection.append(Selection("WX78", [main_x_up + main_x_variation, upper_shift]))
    characters_selection.append(Selection("Wormwood", [main_x_up + main_x_variation * 2, upper_shift]))
    characters_selection.append(Selection("Wickerbottom", [main_x_down, lower_shift]))
    characters_selection.append(Selection("Willow", [main_x_down + main_x_variation, lower_shift]))

    while len(characters.sprites()) < 3:

        window.blit(background_selection, ((WIDTH - background_selection.get_width()) / 2,0))
        window.blit(frame_image, (x, y))

        for character in characters_selection:
            name = character.get_name()
            if(character.get_selectable()):
                image = pygame.image.load(f"images/entities/{name.lower()}/{name.lower()}_selection.webp")
            else:
                image = pygame.image.load(f"images/entities/{name.lower()}/{name.lower()}_selected.webp")
            h = image.get_height()
            image = pygame.transform.scale_by(image, 250/h)
            window.blit(image, character.get_position())

        clock.tick(fps)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x = main_x_up - delta_x
                    y = upper_shift - delta_y
                if event.key == pygame.K_DOWN:
                    x = main_x_down - delta_x
                    y = lower_shift - delta_y
                if event.key == pygame.K_RIGHT:
                    if(x < 608 and y == 25) or (x < 483 and y == 355.72):
                        x += 250
                if event.key == pygame.K_LEFT:
                    if(x > 115 and y == 25) or (x > 233 and y == 355.72):
                        x -= 250
                if event.key == pygame.K_z:
                    for character in characters_selection:
                        if(character.is_position(x + delta_x, y + delta_y) and character.get_selectable()):
                            characters.add(globals()[character.get_name()]())
                            character.unselectable()



    return True

def win(window, background_menu, clock, fps):

    run = True
    while run:

        window.blit(background_menu, (-175,0))

        font = pygame.font.Font(None, 60)
        text = font.render("You win!", True, (255, 255, 255))
        window.blit(text, (550, 660))

        font = pygame.font.Font(None, 42)
        text = font.render("Press A to return to the menu", True, (255, 255, 255))
        window.blit(text, (550, 710))

        clock.tick(fps)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.K_a:
                    return 1
                
def lose(window, background_menu, clock, fps):

    run = True
    while run:

        window.blit(background_menu, (-175,0))

        font = pygame.font.Font(None, 60)
        text = font.render("You lose...", True, (255, 255, 255))
        window.blit(text, (550, 660))

        font = pygame.font.Font(None, 42)
        text = font.render("Press A to return to the menu", True, (255, 255, 255))
        window.blit(text, (550, 710))

        clock.tick(fps)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.K_a:
                    return 1