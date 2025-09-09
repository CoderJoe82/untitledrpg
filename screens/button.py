import pygame
from settings import *
from engine.utils import draw_formatted_text

class Button:
    def __init__(self, x, y, width, height, text_to_format, text_color, font, base_color, hover_color, key_text = "default"):
        self.button_rect = pygame.Rect(x, y, width, height)
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_to_format = text_to_format
        self.key_text = key_text
        self.font = font
        self.text_color = text_color
        self.display_text = self._check_text_complexity()
        self.current_color = self.base_color

    def _check_text_complexity(self):
        if isinstance(self.text_to_format, str):
            return [[(self.text_to_format, self.text_color)]]
        else:
            return self.text_to_format

    def update(self, mouse_pos):
        if self.button_rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.base_color

    def draw(self, screen): 
        pygame.draw.rect(screen, self.current_color, self.button_rect)
        draw_formatted_text(screen, self.display_text, self.button_rect, self.font, alignment = "center", vert_alignment = "center")

    def is_clicked(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(mouse_pos):
                return True
        return False