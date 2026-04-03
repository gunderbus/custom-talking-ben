import pygame


class drawRectObj:
    x: float
    y: float
    width: float
    height: float
    color: pygame.Color

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def drawThisRect(self, xdil: float, ydil: float, width1, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x + xdil, self.y + ydil, self.width, self.height, width1),
        )
        