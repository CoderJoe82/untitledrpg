import pygame
from settings import *
from data.races.all_races import ALL_RACES
from engine.utils import draw_formatted_text, measure_formatted_text_height

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
        self.data_display_details_font = pygame.font.Font(FONT_PATH, CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_DESCRIPTION_FONT_SIZE)

    def _get_race_info(self):
        self.race_info = {
            'header' : self.current_race['display_name'],
            'description' : self.current_race['description'],
            'stat_modifiers' : self.current_race['stats'],
            'resistances' : self.current_race['resistances'],
            'abilities' : self.current_race['abilities'],
            'font_color' : self.current_race['font_color']
        }

    def _get_text_measurements(text, rect, font):
        measure_formatted_text_height(text, rect, font)

    def _create_temp_rect(self, height):
        x = self.rect.x + self.panel_padding
        y = self.current_y
        width = self.rect.width - (self.panel_padding * 2)
        height = height
        return pygame.Rect(x, y, width, height)

    def _create_all_ui(self):
        self.display_rect = self._create_temp_rect(
            (self.navigation_starting_y - self.rect.y) - (self.panel_padding * 2)
        )
        self.header_rect = self._create_temp_rect(
            measure_formatted_text_height([[(self.race_info['header'], self.race_info['font_color'])]], self._create_temp_rect(self.current_y, 100), self.data_display_details_font)
        )
        self.header_rect.width = self.data_display_details_font.size(self.race_info['header'])[0]
        self._create_header_underline_dimensions()
        self.current_y += self.header_rect.height + (CHARACTER_CREATION_SCREEN_HEADER_UNDERLINE_HEIGHT * 2)
        self.description_rect = self._create_temp_rect(
            measure_formatted_text_height([[(self.race_info['description'], self.race_info['font_color'])]], self._create_temp_rect(self.current_y, 100), self.data_display_details_font)
        )
        self.current_y += self.description_rect.height + self.panel_padding

        ######## THIS IS WHERE WE LEFT OFF #############



    def _create_display_rect(self):
        self.display_rect = pygame.Rect(
            self.rect.x + self.panel_padding,
            self.rect.y + self.panel_padding,
            self.rect.width - (self.panel_padding * 2),
            (self.navigation_starting_y - self.rect.y) - (self.panel_padding * 2),
        )

    def _create_text_rect(self):
        self.text_rect_x = self.rect.x + self.panel_padding
        self.text_rect_y = self.rect.y + self.panel_padding
        self.text_rect_width = self.rect.width - (self.panel_padding * 2)
        self.text_rect_height = (self.navigation_starting_y - self.rect.y) - (self.panel_padding * 2)
        self.text_rect = pygame.Rect(self.text_rect_x, self.text_rect_y, self.text_rect_width, self.text_rect_height)

    def _create_header_text_rect(self):
        self.header_text_width, self.header_text_height = self.rect_font.size(self.current_race['display_name'])
        self.header_text_rect_x = self.text_rect_x
        self.header_text_rect_y = self.text_rect_y
        self.header_text_rect_width = self.header_text_width
        self.header_text_rect_height = self.header_text_height
        self.header_text_rect_font = self.rect_font
        self.race_header_rect = pygame.Rect(self.header_text_rect_x, self.header_text_rect_y, self.header_text_rect_width, self.header_text_rect_height)

    def _create_header_underline_dimensions(self):
        self.header_underline_starting_x = self.text_rect_x
        self.header_underline_starting_y = self.current_y
        self.header_underline_ending_x = self.race_header_rect.width
    
    def _create_race_display_description_rect(self):
        self.race_display_description_rect_x = self.text_rect_x
        self.race_display_description_rect_y = (self.header_underline_starting_y + CHARACTER_CREATION_SCREEN_HEADER_UNDERLINE_HEIGHT) + self._get_object_buffer(self.text_rect.height, CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_TEXT_PADDING)
        self.race_display_description_rect_width = self.text_rect.width
        self.race_display_description_rect_font = self.data_display_details_font
        self.race_display_description_rect_height = self._get_text_rect_height([[(f"Description:\n{self.current_race['description']}", self.current_race['font_color'])]], pygame.Rect(self.race_display_description_rect_x, self.race_display_description_rect_y, self.race_display_description_rect_width, 100), self.race_display_description_rect_font)
        self.race_data_display_description_rect = pygame.Rect(self.race_display_description_rect_x, self.race_display_description_rect_y, self.text_rect.width, self.race_display_description_rect_height)
        self.description_text_segment = f"Description:\n{self.current_race['description']}"

    def _prepare_race_starting_stat_modifiers(self):        
        modifiers = self.current_race['stats']
        self.modifier_string = "Stat Modifiers: \n"
        for key, value in modifiers.items():
            stat_name = key
            stat_value = value
            self.modifier_string += f"{stat_name}: {stat_value} "

    def _create_race_display_stat_modifier_rect(self):
        self.race_display_stat_modifier_rect_x = self.text_rect_x
        self.race_display_stat_modifier_rect_y = self.race_data_display_description_rect.bottom + self._get_object_buffer(self.text_rect.height, CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_TEXT_PADDING)
        self.race_display_stat_modifier_rect_width = self.text_rect_width
        self.race_display_stat_modifier_rect_font = self.data_display_details_font
        self.race_display_stat_modifier_rect_height = self._get_text_rect_height([[(self.modifier_string, self.current_race['font_color'])]], pygame.Rect(self.text_rect_x, self.race_display_stat_modifier_rect_y, self.text_rect_width, 1000), self.race_display_stat_modifier_rect_font)
        self.race_display_stat_modifier_rect = pygame.Rect(self.race_display_stat_modifier_rect_x, self.race_display_stat_modifier_rect_y, self.race_display_stat_modifier_rect_width, self.race_display_stat_modifier_rect_height)

        # def measure_formatted_text_height(surface, text_segments, rect)

    def _get_text_rect_height(self, text_segments, rect, font):
        text = text_segments
        text_rect = rect
        text_font = font
        return measure_formatted_text_height(text, text_rect, text_font)
    
    def _get_object_buffer(self, y, buffer_percent):
        return y * buffer_percent

    def _setup_character_display_ui_section(self):
        self._create_text_rect()
        self._get_race_info()
        self.current_y = self.rect.y
        self._create_header_text_rect()            
        self._create_header_underline_dimensions()
        self._create_race_display_description_rect()
        self._prepare_race_starting_stat_modifiers()
        self._create_race_display_stat_modifier_rect()

    def set_current_race(self, race_id):
        for race in self.race_data:
            if race_id == race['id']:
                self.current_race = race
                print(self.current_race)
                self._setup_character_display_ui_section()

    def draw(self, surface):
        if self.current_race is not None:
            pygame.draw.rect(surface, CHARCOAL_SLATE, self.rect)
            pygame.draw.rect(surface, CHARCOAL_SLATE, self.text_rect)
            self.race_header_text_height = draw_formatted_text(surface, [[(self.current_race['display_name'], self.current_race['font_color'])]], self.race_header_rect, self.header_text_rect_font)
            self.header_text_underline = pygame.draw.line(surface, self.current_race['font_color'], (self.header_underline_starting_x, self.header_underline_starting_y), (self.header_underline_ending_x, self.header_underline_starting_y), 2)
            self.race_description_text = draw_formatted_text(surface, [[(self.description_text_segment, self.current_race['font_color'])]], self.race_data_display_description_rect, self.race_display_description_rect_font)
            self.race_display_stat_modifier_rect_text = draw_formatted_text(surface, [[(self.modifier_string, self.current_race['font_color'])]], self.race_display_stat_modifier_rect, self.data_display_details_font)