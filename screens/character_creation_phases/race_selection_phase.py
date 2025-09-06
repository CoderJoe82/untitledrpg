import pygame
from settings import *
from screens.button import Button
from data.races.all_races import ALL_RACES
from screens.character_creation_phases.character_creation_phase import CharacterCreationPhase

class RaceSelectionPhase(CharacterCreationPhase):
    def __init__(self, screen_manager):
        super().__init__(screen_manager)
        self.manager = screen_manager
        self._create_race_selection_buttons()

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
                    'display_text' : race_data['display_name']
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
                    button_names['display_text'],
                    WHITE,
                    pygame.font.Font(FONT_PATH, CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_FONT_SIZE),
                    SLATE_GRAY,
                    MOSSY_STONE,
                    button_names['key_text']
                )
            )
            current_y += self.manager.button_panel_button_height + self.manager.button_panel_button_padding

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        for key, value in enumerate(self.race_selection_buttons):
            button = value
            button.update(mouse_position)

    def draw(self, surface):
        for index, value in enumerate(self.race_selection_buttons):
            button = value
            button.draw(surface)

    def handle_events(self, events):
        mouse_position = pygame.mouse.get_pos()
        for event in events:
            for button in self.race_selection_buttons:
                if button.is_clicked(event, mouse_position):
                    pass
