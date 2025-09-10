import pygame
from settings import *
from screens.button import Button
from data.races.all_races import ALL_RACES
from screens.character_creation_phases.character_creation_phase import CharacterCreationPhase
from engine.utils import draw_formatted_text

class RaceSelectionPhase(CharacterCreationPhase):
    def __init__(self, screen_manager):
        super().__init__(screen_manager)
        self.manager = screen_manager
        self._create_race_selection_buttons()
        self._create_race_navigation_buttons()

    def _create_race_selection_buttons(self):
        self.race_selection_buttons = []
        self.race_selection_names = []
        race_data = list(ALL_RACES.values())
        self.number_of_race_buttons = len(race_data)
        self.full_height_of_race_buttons = (self.manager.button_panel_button_height * self.number_of_race_buttons) + (self.manager.button_panel_button_padding * (self.number_of_race_buttons - 1))
        current_y = self.manager.button_panel_button_y - (self.full_height_of_race_buttons / 2)
        for index, value in enumerate(race_data):
            race_data = value
            self.race_selection_names.append(
                {
                    'key_text' : race_data['id'],
                    'display_text' : race_data['display_name'],
                    'font_color' : race_data['font_color']
                }
            )
        for index, value in enumerate(self.race_selection_names):
            button_names = value
            self.race_selection_buttons.append(
                Button(
                    self.manager.button_panel_button_x,
                    current_y,
                    self.manager.button_panel_button_width,
                    self.manager.button_panel_button_height,
                    [[(button_names['display_text'][0], button_names['font_color']), (button_names['display_text'][1:], WHITE)]],
                    WHITE,
                    pygame.font.Font(FONT_PATH, CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_FONT_SIZE),
                    SLATE_GRAY,
                    MOSSY_STONE,
                    button_names['key_text']
                )
            )
            current_y += self.manager.button_panel_button_height + self.manager.button_panel_button_padding

    def _create_race_navigation_buttons(self):
        self.navigation_buttons = []
        self.navigation_button_texts = {
            'confirm' : "Confirm",
            'go_back' : "Go Back"
        }
        self.number_of_navigation_buttons = len(self.navigation_button_texts)
        self.full_width_of_navigation_buttons = (self.manager.navigation_button_width * self.number_of_navigation_buttons) +  self.manager.navigation_button_padding
        current_x = self.manager.navigation_starting_x - (self.full_width_of_navigation_buttons / 2)
        for key, value in self.navigation_button_texts.items():
            key_text = key
            button_text = value
            self.navigation_buttons.append(
                Button(
                    current_x,
                    self.manager.navigation_starting_y,
                    self.manager.navigation_button_width,
                    self.manager.navigation_button_height,
                    button_text,
                    WHITE,
                    pygame.font.Font(FONT_PATH, CHARACTER_CREATION_SCREEN_NAVIGATION_BUTTON_FONT_SIZE),
                    SLATE_GRAY,
                    MOSSY_STONE,
                    key_text
                )
            )
            current_x += self.manager.navigation_button_width + self.manager.navigation_button_padding

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        for button in self.race_selection_buttons:
            button.update(mouse_position)
        for button in self.navigation_buttons:
            button.update(mouse_position)
        

    def draw(self, surface):
        for button in self.race_selection_buttons:
            button.draw(surface)
        for button in self.navigation_buttons:
            button.draw(surface)

    def handle_events(self, events):
        mouse_position = pygame.mouse.get_pos()
        for event in events:
            for button in self.navigation_buttons:
                if button.is_clicked(event, mouse_position):
                    if button.key_text == 'go_back':
                        self.manager.game.change_game_state('welcome')