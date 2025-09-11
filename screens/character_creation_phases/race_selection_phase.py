import pygame
from settings import *
from screens.button import Button
from data.races.all_races import ALL_RACES
from screens.character_creation_phases.character_creation_phase import CharacterCreationPhase
from screens.character_creation_phases.race_data_ui_panel import RaceDataPanel
from engine.utils import draw_formatted_text


class RaceSelectionPhase(CharacterCreationPhase):
    def __init__(self, screen_manager):
        super().__init__(screen_manager)
        self.manager = screen_manager
        self.info_panel_data = RaceDataPanel(
            self.manager.data_display_data_panel_x,
            self.manager.data_display_data_panel_y,
            self.manager.data_display_data_panel_width,
            self.manager.data_display_data_panel_height,
            self.manager.navigation_starting_y,
            self.manager.character_creation_screen_size
        )
        self.race_data = list(ALL_RACES.values())
        self._create_race_selection_buttons()
        self._create_race_navigation_buttons()
        self._create_header_text()

    def _create_race_data_display_text_dimensions(self):
        pass

    def _create_race_selection_buttons(self):
        self.race_selection_buttons = []
        self.race_selection_names = []
        self.number_of_race_buttons = len(self.race_data)
        self.full_height_of_race_buttons = (
            self.manager.button_panel_button_height * self.number_of_race_buttons
        ) + (
            self.manager.button_panel_button_padding * (self.number_of_race_buttons - 1)
        )
        current_y = self.manager.button_panel_button_y - (
            self.full_height_of_race_buttons / 2
        )
        for index, value in enumerate(self.race_data):
            data = value
            self.race_selection_names.append(
                {
                    "key_text": data["id"],
                    "display_text": data["display_name"],
                    "font_color": data["font_color"],
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
                    [
                        [
                            (
                                button_names["display_text"][0],
                                button_names["font_color"],
                            ),
                            (button_names["display_text"][1:], WHITE),
                        ]
                    ],
                    WHITE,
                    pygame.font.Font(
                        FONT_PATH,
                        CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_FONT_SIZE,
                    ),
                    SLATE_GRAY,
                    MOSSY_STONE,
                    button_names["key_text"],
                )
            )
            current_y += (
                self.manager.button_panel_button_height
                + self.manager.button_panel_button_padding
            )

    def _create_race_navigation_buttons(self):
        self.navigation_buttons = []
        self.navigation_button_texts = {"confirm": "Confirm", "go_back": "Go Back"}
        self.number_of_navigation_buttons = len(self.navigation_button_texts)
        self.full_width_of_navigation_buttons = (
            self.manager.navigation_button_width * self.number_of_navigation_buttons
        ) + self.manager.navigation_button_padding
        current_x = self.manager.navigation_starting_x - (
            self.full_width_of_navigation_buttons / 2
        )
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
                    pygame.font.Font(
                        FONT_PATH, CHARACTER_CREATION_SCREEN_NAVIGATION_BUTTON_FONT_SIZE
                    ),
                    SLATE_GRAY,
                    MOSSY_STONE,
                    key_text,
                )
            )
            current_x += (
                self.manager.navigation_button_width
                + self.manager.navigation_button_padding
            )

    def _create_header_text(self):
        self.header_rect = pygame.Rect(
            self.manager.phase_title_panel_x,
            self.manager.phase_title_panel_y,
            self.manager.phase_title_panel_width,
            self.manager.phase_title_panel_height,
        )
        self.header_rect_display_text = "Choose Your Race"
        self.header_rect_font = pygame.font.Font(FONT_PATH, LARGE_FONT_SIZE)
        self.header_rect_display_text_alignment = "center"
        self.header_rect_display_text_vert_alignment = "center"

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        for button in self.race_selection_buttons:
            button.update(mouse_position)
        for button in self.navigation_buttons:
            button.update(mouse_position)

    def draw(self, surface):
        draw_formatted_text(
            surface,
            [[(self.header_rect_display_text, WHITE)]],
            self.header_rect,
            self.header_rect_font,
            self.header_rect_display_text_alignment,
            self.header_rect_display_text_vert_alignment,
        )
        self.info_panel_data.draw(surface)
        for button in self.race_selection_buttons:
            button.draw(surface)
        for button in self.navigation_buttons:
            button.draw(surface)

    def handle_events(self, events):
        mouse_position = pygame.mouse.get_pos()
        for event in events:
            for button in self.navigation_buttons:
                if button.is_clicked(event, mouse_position):
                    if button.key_text == "go_back":
                        self.manager.game.change_game_state("welcome")
            for button in self.race_selection_buttons:
                if button.is_clicked(event, mouse_position):
                    self.info_panel_data.set_current_race(button.key_text)