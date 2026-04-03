import pygame


class textInput:
    def __init__(
        self,
        iwidth: int,
        iheight: int,
        ifont: pygame.font.Font,  # Ensure this is a Font object
        ibckcolor: pygame.Color,
        itextcolor: pygame.Color,
        screen,
        x,
        y,
    ):
        self.rect = pygame.Rect(x, y, iwidth, iheight)
        self.font = ifont
        self.bckcolor = ibckcolor
        self.textcolor = itextcolor
        self.isClicked = False
        self.wasClicked = False
        self.givenText = []

    def onClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        left_click = mouse_buttons[0]

        if self.rect.collidepoint(mouse_pos):
            if left_click and not self.wasClicked:
                self.isClicked = not self.isClicked

        # This update happens regardless of hover to track mouse state correctly
        self.wasClicked = left_click

    def getIsClicked(self):
        return self.isClicked

    def draw(self, screen, events):  # Added 'events' as a parameter
        self.onClicked()

        # Handle Text Appending
        if self.isClicked:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(self.givenText) > 0:
                            self.givenText.pop()
                    elif event.key == pygame.K_RETURN:  # Fixed indentation
                        self.isClicked = False
                    else:
                        # Append the typed character
                        if event.unicode:
                            self.givenText.append(event.unicode)

        # Visuals: Draw the Box
        border_color = (255, 255, 255) if self.isClicked else (100, 100, 100)
        pygame.draw.rect(screen, self.bckcolor, self.rect)
        pygame.draw.rect(screen, border_color, self.rect, 2)

        # Visuals: Render the Text
        # Joining the list into a string
        display_text = "".join(self.givenText)
        text_surface = self.font.render(display_text, True, self.textcolor)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
