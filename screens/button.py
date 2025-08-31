import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, display_text, text_color, font, base_color, hover_color, key_text = "default"):
        self.button_rect = pygame.Rect(x, y, width, height)
        self.base_color = base_color
        self.hover_color = hover_color
        self.display_text = display_text
        self.key_text = key_text
        self.font = font
        self.text_surface = self.font.render(self.display_text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center = self.button_rect.center)
        self.current_color = self.base_color

    def update(self, mouse_pos):
        if self.button_rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.base_color

    def draw(self, screen): 
        pygame.draw.rect(screen, self.current_color, self.button_rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(mouse_pos):
                return True
        return False