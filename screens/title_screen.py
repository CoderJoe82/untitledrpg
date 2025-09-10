import pygame
from settings import *
from engine.state import State
from screens.button import Button
from engine.utils import draw_formatted_text

class TitleScreen(State):
    def __init__(self, game):
        super().__init__(game)
        self.title_screen_size = self.game.screen.get_size()
        self.surface = pygame.Surface(self.title_screen_size)
        self._create_title_rect()
        self._create_title_screen_button_dimensions()
        self._create_title_screen_buttons()

    def _create_title_screen_button_dimensions(self):
        game_window_width, game_window_height = self.title_screen_size
        self.button_height = TITLE_SCREEN_BUTTON_HEIGHT
        self.button_width = TITLE_SCREEN_BUTTON_WIDTH
        self.button_x_location = (self.surface.get_width() / 2) - (self.button_width / 2)
        self.button_y_location = game_window_height * TITLE_SCREEN_BUTTON_Y_POSITION
        self.button_padding = TITLE_SCREEN_BUTTON_PADDING

    def _create_title_screen_buttons(self):
        self.title_screen_button_names = {
            'new_game' : 'New Game',
            'load_game' : 'Load Game',
            'quit' : 'Quit'
        }
        self.title_screen_buttons = []
        self.current_y = self.button_y_location
        for key, value in self.title_screen_button_names.items():
            key_text = key
            display_text = value
            self.title_screen_buttons.append(
                Button(
                    self.button_x_location,
                    self.current_y,
                    self.button_width,
                    self.button_height,
                    display_text,
                    WHITE,  
                    pygame.font.Font(FONT_PATH, 30),
                    SLATE_GRAY,
                    MOSSY_STONE,
                    key_text
                )
            )
            self.current_y += self.button_height + self.button_padding

    # def _create_title(self):
    def _create_title_rect(self):
        game_window_width, game_window_height = self.title_screen_size
        self.title_rect = pygame.Rect(game_window_width * TITLE_SCREEN_TITLE_RECT_X, game_window_height * TITLE_SCREEN_TITLE_RECT_Y, game_window_width * TITLE_SCREEN_TITLE_RECT_WIDTH, game_window_height * TITLE_SCREEN_TITLE_RECT_HEIGHT)
        self.title_rect_text = "Untitled RPG"
        self.title_font = pygame.font.Font(FONT_PATH, LARGE_FONT_SIZE)
        self.title_rect_alignment = "center"
        self.title_rect_vert_alignment = "center"

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        for key, value in enumerate(self.title_screen_buttons):
            button = value
            button.update(mouse_position)

    def draw(self, screen):
        self.surface.fill(CHARCOAL_SLATE)
        draw_formatted_text(self.surface, [[(self.title_rect_text, WHITE)]], self.title_rect, self.title_font, self.title_rect_alignment, self.title_rect_vert_alignment)
        for index, value in enumerate(self.title_screen_buttons):
            button = value
            button.draw(self.surface)
        self.game.screen.blit(self.surface, (0, 0))

    def handle_events(self, events):
        mouse_position = pygame.mouse.get_pos()
        for event in events:
            for index, value in enumerate(self.title_screen_buttons):
                button = value
                if button.is_clicked(event, mouse_position):
                    if button.key_text == "quit":
                        self.game.running = False
                    elif button.key_text == "new_game":
                        self.game.change_game_state('welcome')