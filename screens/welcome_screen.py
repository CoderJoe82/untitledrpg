import pygame
from settings import *
from engine.state import State
from engine.utils import draw_formatted_text
from game_text.welcome_screen_text import game_welcome_message_text
from screens.button import Button

class WelcomeScreen(State):
    def __init__(self, game):
        super().__init__(game)
        self.welcome_screen_size = self.game.screen.get_size()
        self.surface = pygame.Surface(self.welcome_screen_size)
        self._create_welcome_text_rect_dimensions()
        self._create_welcome_screen_button_dimensions()
        self._create_welcome_screen_buttons()
        

    def _create_welcome_text_rect_dimensions(self):
        self.welcome_text_font = pygame.font.Font(FONT_PATH, WELCOME_SCREEN_WELCOME_MESSAGE_FONT_SIZE)
        self.surface_width, self.surface_height = self.welcome_screen_size
        self.welcome_text_rect = pygame.Rect(self.surface_width * WELCOME_SCREEN_TEXT_RECT_X, self.surface_height * WELCOME_SCREEN_TEXT_RECT_Y, self.surface_width - ((self.surface_width *  WELCOME_SCREEN_TEXT_RECT_Y_PADDING) * 2), 10)

    def _create_welcome_screen_button_dimensions(self):
        self.button_height = WELCOME_SCREEN_BUTTON_HEIGHT
        self.button_width = WELCOME_SCREEN_BUTTON_WIDTH
        self.button_padding = WELCOME_SCREEN_BUTTON_PADDING
        self.button_y_location = (self.surface.get_height() * WELCOME_SCREEN_BUTTON_Y_POSITION) - (self.button_height / 2)

    def _create_welcome_screen_buttons(self):
        game_window_width, game_window_height = self.welcome_screen_size
        self.welcome_screen_button_names = {
            'create_character' : "Create Character",
            'go_back' : "Go Back"
        }
        self.welcome_screen_buttons = []
        self.total_number_of_buttons = len(self.welcome_screen_button_names)
        self.total_width_of_buttons_and_padding = (self.button_width * self.total_number_of_buttons) + (self.button_padding * (self.total_number_of_buttons - 1))
        current_x = (game_window_width * WELCOME_SCREEN_BUTTON_X_POSITION) - (self.total_width_of_buttons_and_padding / 2)
        for key, value in self.welcome_screen_button_names.items():
            key_text = key
            display_text = value
            self.welcome_screen_buttons.append(
                Button(
                    current_x,
                    self.button_y_location,
                    self.button_width,
                    self.button_height,
                    display_text,
                    WHITE,
                    pygame.font.Font(FONT_PATH, WELCOME_SCREEN_BUTTON_FONT_SIZE),
                    SLATE_GRAY,
                    MOSSY_STONE,
                    key_text
                    # self, x, y, width, height, text_to_format, text_color, font, base_color, hover_color, key_text = "default"
                )
            )
            current_x += self.button_width + (game_window_width * self.button_padding)

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        for key, value in enumerate(self.welcome_screen_buttons):
            button = value
            button.update(mouse_position)

    def draw(self, screen):
        self.surface.fill(CHARCOAL_SLATE)
        draw_formatted_text(self.surface, game_welcome_message_text, self.welcome_text_rect, self.welcome_text_font)
        for index, value in enumerate(self.welcome_screen_buttons):
            button = value
            button.draw(self.surface)
        self.game.screen.blit(self.surface, (0, 0))

    def handle_events(self, events):
        mouse_position = pygame.mouse.get_pos()
        for event in events:
            for index, value in enumerate(self.welcome_screen_buttons):
                button = value
                if button.is_clicked(event, mouse_position):
                    if button.key_text == 'go_back':
                        self.game.change_game_state('title')
                    elif button.key_text == "create_character":
                        self.game.change_game_state('character_creation')             