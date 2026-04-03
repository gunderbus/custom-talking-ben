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
    ):
        self.width = iwidth
        self.height = iheight
        self.font = ifont
        self.bckcolor = ibckcolor
        self.textcolor = itextcolor

        # self.rect = pygame.draw.rect(screen, self.bckcolor, pygame.Rect(0, 0, 0, ))
