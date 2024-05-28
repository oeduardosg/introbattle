import pygame

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
                run = False

    return False