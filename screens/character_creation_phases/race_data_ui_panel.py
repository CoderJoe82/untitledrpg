import pygame
from settings import *
from data.races.all_races import ALL_RACES
from engine.utils import draw_formatted_text

class RaceDataPanel:
    def __init__(self, panel_x, panel_y, panel_width, panel_height, navigation_starting_y, screen_size):
        self.race_data = list(ALL_RACES.values())
        self.current_race = None
        self.panel_x = panel_x
        self.panel_y = panel_y
        self.panel_width = panel_width
        self.panel_height = panel_height
        self.screen_size = screen_size
        self.navigation_starting_y = navigation_starting_y
        self.game_window_width, self.game_window_height = self.screen_size
        self.panel_padding = self.game_window_height * CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_TEXT_PADDING
        self.rect = pygame.Rect(self.panel_x, self.panel_y, self.panel_width, self.panel_height)
        self.rect_font = pygame.font.Font(FONT_PATH, CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_FONT_SIZE)
        print(f"Race Info Panel Rect: {self.rect}")
        self._create_text_rect()
        self.text_rect = pygame.Rect(self.text_rect_x, self.text_rect_y, self.text_rect_width, self.text_rect_height)

    def _create_text_rect(self):
        self.text_rect_x = self.rect.x + self.panel_padding
        self.text_rect_y = self.rect.y + self.panel_padding
        self.text_rect_width = self.rect.width - (self.panel_padding * 2)
        self.text_rect_height = (self.navigation_starting_y - self.rect.y) - (self.panel_padding * 2)
        self.text_rect = pygame.Rect(self.text_rect_x, self.text_rect_y, self.text_rect_width, self.text_rect_height)
        print(self.rect.height - self.text_rect.height)

    def set_current_race(self, race_id):
        for race in self.race_data:
            if race_id == race['id']:
                self.current_race = race

    def draw(self, surface):
        pygame.draw.rect(surface, CHARCOAL_SLATE, self.rect)
        pygame.draw.rect(surface, WHITE, self.text_rect)
        if self.current_race is not None:
            draw_formatted_text(surface, [[(self.current_race['display_name'], self.current_race['font_color'])]], self.text_rect, self.rect_font)