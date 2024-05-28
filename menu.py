import pygame
from entities import *

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

    frame_image = pygame.image.load("images/selection_frame.png").convert()
    #h = frame_image.get_width()
    #frame_image = pygame.transform.scale_by(frame_image, WIDTH/h)
    x = 50
    y = 50

    while len(characters.sprites()) < 3:

        window.blit(background_selection, (0,0))
        window.blit(frame_image, (x, y))

        clock.tick(fps)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_UP:
                    y -= 10
                if event.type == pygame.K_DOWN:
                    y += 10
                if event.type == pygame.K_RIGHT:
                    x += 10
                if event.type == pygame.K_LEFT:
                    x -= 10

    return False