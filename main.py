# import dspy
import this

import pygame

import drawrect

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
cole = drawrect.drawRectObj(10, 10, 100, 100, pygame.Color(255, 255, 255))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    cole.drawThisRect(0, 0, 10, screen)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60


pygame.quit()
