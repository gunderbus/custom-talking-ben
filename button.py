import pygame


class Button:
    def __init__(self, x, y, auto_img, hover_img, click_img):
        # Use self. to save these to the specific button object
        self.auto_img = auto_img
        self.hover_img = hover_img
        self.click_img = click_img
        self.current_img = self.auto_img

        # Create a rect so we know WHERE the button is for clicking/hovering
        self.rect = self.current_img.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        # Logic to check for hover/click
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Reset to default each frame
        self.current_img = self.auto_img

        # Check if mouse is over the button
        if self.rect.collidepoint(mouse_pos):
            self.current_img = self.hover_img
            if mouse_click[0]:  # 0 is left click
                self.current_img = self.click_img

        # Draw the current state to the screen
        screen.blit(self.current_img, (self.rect.x, self.rect.y))

    def getIsHover(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos):
            return True
            # if mouse_click[0]: # 0 is left click
            #     self.current_img = self.click_img
