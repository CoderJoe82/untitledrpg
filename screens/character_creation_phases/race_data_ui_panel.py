import pygame
from settings import *
from data.races.all_races import ALL_RACES

class RaceDataPanel:
    def __init__(self, panel_x, panel_y, panel_width, panel_height):
        self.panel_x = panel_x
        self.panel_y = panel_y
        self.panel_width = panel_width
        self.panel_height = panel_height
        self.background_color = WHITE
        self.rect = pygame.Rect(self.panel_x, self.panel_y, self.panel_width, self.panel_height)
        print(f"Race Info Panel Rect: {self.rect}")

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)