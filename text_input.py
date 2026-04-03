import pygame


class textInput:
    width: int
    height: int
    font: str
    bckcolor: pygame.Color
    textcolor: pygame.Color
    isClicked: bool = False

    def __init__(
        self,
        iwidth: int,
        iheight: int,
        ifont: str,
        ibckcolor: pygame.Color,
        itextcolor: pygame.Color,
        screen,
        x,
        y,
    ):
        self.width = iwidth
        self.height = iheight
        self.font = ifont
        self.bckcolor = ibckcolor
        self.textcolor = itextcolor
        self.isClicked = False

        # self.drawrect = {
        #     "topleft": (x, y),
        #     "color": self.bckcolor,
        #     "textcolor": self.textcolor,
        #     "width": self.width,
        #     "height": self.height,
        # }

        self.rect = pygame.Rect()
        self.rect.width = self.width
        self.rect.height = self.height
        self.rect.topleft = (x, y)

    def getIsClicked(self):
        return self.isClicked

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos):
            if mouse_click[0]:  # 0 is left click
                if self.isClicked == False:
                    self.isClicked = True
                else:
                    self.isClicked = False
