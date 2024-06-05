import pygame
from entities import *

WIDTH = 1024
LENGHT = 768

def menu(window, background_menu, clock, fps):

    run = True
    while run:

        window.blit(background_menu, (0,0))

        font = pygame.font.Font(None, 76)
        text = font.render("Start", True, (255, 255, 255))
        window.blit(text, (850, 680))

        clock.tick(fps)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if pygame.K_a:
                    return 1
                

def selection(characters, window, background_selection, clock, fps):

    frame_image = pygame.image.load("images/selection_frame.png")
    h = frame_image.get_width()
    frame_image = pygame.transform.scale_by(frame_image, 290/h)

    x = 108
    y = 25
    
    main_x_up = 150
    main_x_down = 275
    main_x_variation = 250

    mid_pixel = LENGHT/2
    shift = 150
    upper_shift = mid_pixel - 2 * shift
    lower_shift = mid_pixel + LENGHT / 25

    delta_x = main_x_up - x
    delta_y = upper_shift - y


    while len(characters.sprites()) < 3:

        window.blit(background_selection, ((WIDTH - background_selection.get_width()) / 2,0))
        window.blit(frame_image, (x, y))

        characters_position = {"Wigfrid": [main_x_up, upper_shift],
                               "WX78": [main_x_up + main_x_variation, upper_shift],
                               "Wormwood": [main_x_up + main_x_variation * 2, upper_shift],
                               "Wickerbottom": [main_x_down, lower_shift],
                               "Willow": [main_x_down + main_x_variation, lower_shift] ,}
        
        for name, position in characters_position.items():
            image = pygame.image.load(f"images/entities/{name.lower()}/{name.lower()}_selection.webp")
            h = image.get_height()
            image = pygame.transform.scale_by(image, 250/h)
            window.blit(image, position)

        clock.tick(fps)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x = main_x_up - delta_x
                    y = upper_shift - delta_y
                if event.key == pygame.K_DOWN:
                    x = main_x_down - delta_x
                    y = lower_shift - delta_y
                if event.key == pygame.K_RIGHT:
                    if(x < 615):
                        x += 250
                if event.key == pygame.K_LEFT:
                    if(x > 115):
                        x -= 250
                if event.key == pygame.K_z:
                    characters.add(Rogue())

    return True