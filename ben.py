import pygame

class ben:
    state: int

    def __init__(
        self,
        defaultImgPath: str
        imgNoPath: str,
        imgYesPath: str,
        imgHahaPath: str,
        imgBlehPath: str,
        stateSet: int,
    ):

        self.defImg = pygame.image.load(defaultImgPath).convert_alpha()
        self.imgNo = pygame.image.load(imgNoPath).convert_alpha()
        self.imgYes = pygame.image.load(imgYesPath).convert_alpha()
        self.imgHaha = pygame.image.load(imgHahaPath).convert_alpha()
        self.imgBleh = pygame.image.load(imgBlehPath).convert_alpha()

        self.rect = self.defImg.get_rect()
        self.rect.topleft = (x,y)

        self.stateSet = -1

    def setState(
        state: int
    ):
        self.stateSet = state

    def draw():

        # damn bruh this shit is genuene ass
        if(stateSet == -1):
            self.rect = self.defImg.get_rect()
        elif stateSet == 0:
            self.rect = self.imgHaha.get_rect()
        elif stateSet == 1:
            self.rect = self.imgBleh.get_rect()
        elif stateSet == 2:
            self.rect = self.imgYes.get_rect()
        elif stateSet == 3:
            self.rect == self.imgNo.get_rect()
        else:
            self.rect = self.defImg.get_rect()
