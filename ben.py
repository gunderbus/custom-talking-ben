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
        x,
        y
    ):
        self.x = x
        self.y = y

        self.defImg = pygame.image.load(defaultImgPath).convert_alpha()
        self.imgNo = pygame.image.load(imgNoPath).convert_alpha()
        self.imgYes = pygame.image.load(imgYesPath).convert_alpha()
        self.imgHaha = pygame.image.load(imgHahaPath).convert_alpha()
        self.imgBleh = pygame.image.load(imgBlehPath).convert_alpha()

        self.image = self.degImg

        self.stateSet = -1

    def setState(
        state: int
    ):
        self.stateSet = state

    def draw(self, screen):

        # damn bruh this shit is genuene ass
        if(self.stateSet == -1):
            self.image = self.defImg
        elif self.stateSet == 0:
            self.image = self.imgHaha
        elif self.stateSet == 1:
            self.image = self.imgBleh
        elif self.stateSet == 2:
            self.image = self.imgYes
        elif self.stateSet == 3:
            self.image == self.imgNo
        else:
            self.image = self.defImg

        try:
            screen.blit(self.rect, (self.x, self.y))
        except:
            raise ValueError("ts is not working bruh")
