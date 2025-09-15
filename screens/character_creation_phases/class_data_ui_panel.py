import pygame
from settings import *
from data.classes.all_classes import ALL_CLASSES
from engine.utils import draw_formatted_text, measure_formatted_text_height

class ClassDataPanel:
    def __init__(self, panel_x, panel_y, panel_width, panel_height, navigation_starting_y, screen_size):
        self.character_class_data = list(ALL_CLASSES.values())
        self.current_character_class = None
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
        self.data_display_details_font = pygame.font.Font(FONT_PATH, CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_DESCRIPTION_FONT_SIZE)
        self.display_rect = pygame.Rect(self.rect.x + self.panel_padding, self.rect.y + self.panel_padding, self.rect.width - (self.panel_padding * 2), (self.navigation_starting_y - self.rect.y) - (self.panel_padding * 2))
        self.current_y = self.display_rect.y
    
    def _get_character_class_info(self):
        self.character_class_info = {
            'header' : self.current_character_class['display_name'],
            'description' : self.current_character_class['description'],
            'stat_modifiers' : self.current_character_class['stats'],
            'resistances' : self.current_character_class['resistances'],
            'abilities' : self.current_character_class['abilities'],
            'font_color' : self.current_character_class['font_color']
        }

    def _create_display_strings(self):
        self.header_string = self.character_class_info['header']
        self.description_string = f"Description:\n{self.character_class_info['description']}"
        self.stat_modifier_string = f"Stat Modifiers:\n"
        for key, value in self.character_class_info['stat_modifiers'].items():
            stat_name = key
            stat_value = value
            self.stat_modifier_string += f"{stat_name}: {stat_value} "
        self.resistances_string = f"Resistances:\n"
        for key, value in self.character_class_info['resistances'].items():
            resistance_type = key
            resistance_value = value
            self.resistances_string += f"{resistance_type}: {resistance_value}"
        self.abilities_string = f"Abilities:\n"
        for ability_dict in self.character_class_info['abilities']:
            ability_name = ability_dict['name']
            ability_description = ability_dict['description']
            self.abilities_string += f"{ability_name}: {ability_description}"

    def _get_display_string_heights(self):
        self.header_string_height = measure_formatted_text_height([[(self.header_string, self.character_class_info['font_color'])]], pygame.Rect(self.display_rect.x, self.display_rect.y, self.display_rect.width, 100), self.data_display_details_font)
        self.description_string_height = measure_formatted_text_height([[(self.description_string, self.character_class_info['font_color'])]], pygame.Rect(self.display_rect.x, self.display_rect.y, self.display_rect.width, 100), self.data_display_details_font)
        self.stat_modifier_string_height = measure_formatted_text_height([[(self.stat_modifier_string, self.character_class_info['font_color'])]], pygame.Rect(self.display_rect.x, self.display_rect.y, self.display_rect.width, 100), self.data_display_details_font)
        self.resistances_string_height = measure_formatted_text_height([[(self.resistances_string, self.character_class_info['font_color'])]], pygame.Rect(self.display_rect.x, self.display_rect.y, self.display_rect.width, 100), self.data_display_details_font)
        self.abilities_string_height = measure_formatted_text_height([[(self.abilities_string, self.character_class_info['font_color'])]], pygame.Rect(self.display_rect.x, self.display_rect.y, self.display_rect.width, 100), self.data_display_details_font)

    def _create_temp_rect(self, height):
        return pygame.Rect(self.display_rect.x, self.current_y, self.display_rect.width, height)
    
    def _create_header_underline_dimensions(self):
        header_string_width, _ = self.data_display_details_font.size(self.header_string)
        self.header_underline_starting_x = self.display_rect.x
        self.header_underline_starting_y = self.display_rect.y + self.header_string_height
        self.header_underline_ending_x = self.header_underline_starting_x + header_string_width

    def _create_display_rects(self):
        self._get_display_string_heights()
        self.header_rect = self._create_temp_rect(self.header_string_height)
        self._create_header_underline_dimensions()
        self.current_y += self.header_string_height + self.panel_padding + CHARACTER_CREATION_SCREEN_HEADER_UNDERLINE_HEIGHT
        self.description_rect = self._create_temp_rect(self.description_string_height)
        self.current_y += self.description_string_height + self.panel_padding
        self.stat_modifier_rect = self._create_temp_rect(self.stat_modifier_string_height)
        self.current_y += self.stat_modifier_string_height + self.panel_padding
        self.resistances_rect = self._create_temp_rect(self.resistances_string_height)
        self.current_y += self.resistances_string_height + self.panel_padding
        self.abilities_rect = self._create_temp_rect(self.abilities_string_height)

    def _setup_character_class_display_ui(self):
        self._get_character_class_info()
        self._create_display_strings()
        self._create_display_rects()
        self.current_y = self.display_rect.y

    def set_current_character_class(self, character_class_id):
        for character_class in self.character_class_data:
            if character_class_id == character_class['id']:
                self.current_character_class = character_class
                self._setup_character_class_display_ui()

    def draw(self, surface):
        if self.current_character_class is not None:
            pygame.draw.rect(surface, CHARCOAL_SLATE, self.rect)
            pygame.draw.rect(surface, CHARCOAL_SLATE, self.display_rect)
            draw_formatted_text(surface, [[(self.header_string, self.character_class_info['font_color'])]], self.header_rect, self.data_display_details_font)
            pygame.draw.line(surface, self.character_class_info['font_color'], (self.header_underline_starting_x, self.header_underline_starting_y), (self.header_underline_ending_x, self.header_underline_starting_y), CHARACTER_CREATION_SCREEN_HEADER_UNDERLINE_HEIGHT)
            draw_formatted_text(surface, [[(self.description_string, self.character_class_info['font_color'])]], self.description_rect, self.data_display_details_font)
            draw_formatted_text(surface, [[(self.stat_modifier_string, self.character_class_info['font_color'])]], self.stat_modifier_rect, self.data_display_details_font)
            draw_formatted_text(surface, [[(self.resistances_string, self.character_class_info['font_color'])]], self.resistances_rect, self.data_display_details_font)
            draw_formatted_text(surface, [[(self.abilities_string, self.character_class_info['font_color'])]], self.abilities_rect, self.data_display_details_font)