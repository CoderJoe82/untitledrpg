from screens.character_creation_phases.character_creation_phase import CharacterCreationPhase
from settings import *
import pygame
from screens.button import Button
from engine.utils import draw_formatted_text

class NameSelectionPhase(CharacterCreationPhase):
    def __init__(self, screen_manager):
        super().__init__(screen_manager)
        self.manager = screen_manager
        self.player_name = ""
        self.input_active = False
        self._create_input_text_rect_dimensions()
        self.input_text_rect = pygame.Rect(
            self.input_text_rect_x,
            self.input_text_rect_y,
            self.input_text_rect_width,
            self.input_text_rect_height
        )
        self._create_header_text()
        self._create_input_text_navigation_buttons()

    def _create_input_text_rect_dimensions(self):
        self.input_text_rect_width = self.manager.data_display_data_panel_width * CHARACTER_CREATION_SCREEN_INPUT_TEXT_RECT_WIDTH
        self.input_text_rect_x = self.manager.data_display_data_panel_x + ((self.manager.data_display_data_panel_width / 2) - (self.input_text_rect_width / 2))
        self.input_text_rect_y = self.manager.data_display_data_panel_y + ((self.manager.data_display_data_panel_height / 2) - (CHARACTER_CREATION_SCREEN_INPUT_TEXT_RECT_HEIGHT / 2))
        self.input_text_rect_height = CHARACTER_CREATION_SCREEN_INPUT_TEXT_RECT_HEIGHT

    def _create_input_text_navigation_buttons(self):
        self.navigation_buttons = []
        self.navigation_button_texts = {
            'confirm' : "Confirm",
            'go_back' : "Go Back"
        }
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
                        FONT_PATH,
                        CHARACTER_CREATION_SCREEN_NAVIGATION_BUTTON_FONT_SIZE
                    ),
                    SLATE_GRAY,
                    MOSSY_STONE,
                    key_text
                )
            )
            current_x += (
                self.manager.navigation_button_width + self.manager.navigation_button_padding
            )

    def _create_header_text(self):
        self.header_rect = pygame.Rect(
            self.manager.phase_title_panel_x,
            self.manager.phase_title_panel_y,
            self.manager.phase_title_panel_width,
            self.manager.phase_title_panel_height
        )
        self.header_rect_display_text = "Enter Your Name"
        self.header_rect_font = pygame.font.Font(FONT_PATH, LARGE_FONT_SIZE)
        self.header_rect_display_text_alignment = 'center'
        self.header_rect_display_text_vert_alignment = 'center'

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self, surface):
        draw_formatted_text(surface, [[(self.header_rect_display_text, WHITE)]], self.header_rect, self.header_rect_font, self.header_rect_display_text_alignment, self.header_rect_display_text_vert_alignment)
        pygame.draw.rect(surface, SLATE_GRAY, self.input_text_rect)
        for button in self.navigation_buttons:
            button.draw(surface)

