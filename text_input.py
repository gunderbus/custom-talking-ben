import pygame


class textInput:
    width: int
    height: int
    font: str
    bckcolor: str
    textcolor: str

    def __init__(
        self,
        iwidth: int,
        iheight: int,
        ifont: str,
        ibckcolor: str,
        itextcolor: str,
        screen,
        x,
        y,
    ):
        self.width = iwidth
        self.height = iheight
        self.font = ifont
        self.bckcolor = ibckcolor
        self.textcolor = itextcolor

        self.rect = pygame.Rect()
        self.rect.topleft = (x, y)
        self.rect.width = self.width
        self.rect.height = self.height
