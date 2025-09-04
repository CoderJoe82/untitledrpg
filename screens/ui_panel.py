import pygame

class UI_Panel:
    def __init__(self, x, y, width, height, background_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background_color = background_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.background_color, self.rect)