import pygame
from settings import *
from engine.state import State
from screens.button import Button
from screens.ui_panel import UI_Panel
from data.races.all_races import ALL_RACES

class CharacterCreationScreen(State):
    def __init__(self, game):
        super().__init__(game)
        self.character_creation_screen_size = self.game.screen.get_size()
        self.surface = pygame.Surface(self.character_creation_screen_size)
        self.phases = {
            'race_selection' : {
                'title' : "Choose Your Race",
                'buttons' : []
            },
            'class_selection' : {
                'title' : "Choose your Class",
                'buttons' : []
            },
            'character_confirmation' : {
                'title' : 'Your Curreent Character',
                'buttons' : []
            }
        }
        self.current_phase = 'race_selection'
        self._create_divider_line_dimensions()
        self._create_character_creation_panel_dimensions()
        self._create_character_creation_panels()
        self._create_button_panel_button_dimensions()
        self._create_race_selection_buttons()

    def _create_character_creation_panel_dimensions(self):
        game_window_width, game_window_height = self.character_creation_screen_size
        self.button_ui_panel_x = CHARACTER_CREATION_SCREEN_BUTTON_PANEL_STARTING_X
        self.button_ui_panel_y = CHARACTER_CREATION_SCREEN_BUTTON_PANEL_STARTING_Y
        self.button_ui_panel_width = game_window_width * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_WIDTH
        self.button_ui_panel_height = game_window_height
        self.phase_title_panel_x = game_window_width * CHARACTER_CREATION_SCREEN_PHASE_TITLE_PANEL_STARTING_X
        self.phase_title_panel_y = CHARACTER_CREATION_SCREEN_PHASE_TITLE_PANEL_STARTING_Y
        self.phase_title_panel_width = game_window_width * CHARACTER_CREATION_SCREEN_PHASE_TITLE_PANEL_WIDTH
        self.phase_title_panel_height = game_window_height * CHARACTER_CREATION_SCREEN_PHASE_TITLE_PANEL_HEIGHT
        self.data_display_data_panel_x = game_window_width * CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_STARTING_X
        self.data_display_data_panel_y = game_window_width * CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_STARTING_Y
        self.data_display_data_panel_width = game_window_width * CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_WIDTH
        self.data_display_data_panel_height = game_window_height * CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_HEIGHT

    def _create_button_panel_button_dimensions(self):
        self.button_panel_button_width = self.button_ui_panel_width * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_WIDTH
        self.button_panel_button_height = self.button_ui_panel_height * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_HEIGHT
        self.button_panel_button_x = 20
        self.button_panel_button_y = self.button_ui_panel_height * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_STARTING_Y
        self.button_panel_button_padding = self.button_ui_panel_height * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_PADDING
        
    def _create_character_creation_panels(self):
        self.button_panel = UI_Panel(
            # x, y, width, height, background_color
            self.button_ui_panel_x,
            self.button_ui_panel_y,
            self.button_ui_panel_width,
            self.button_ui_panel_height,
            CHARCOAL_SLATE
        )
        self.phase_title_panel = UI_Panel(
            self.phase_title_panel_x,
            self.phase_title_panel_y,
            self.phase_title_panel_width,
            self.phase_title_panel_height,
            CHARCOAL_SLATE
        )
        self.data_display_panel = UI_Panel(
            self.data_display_data_panel_x,
            self.data_display_data_panel_y,
            self.data_display_data_panel_width,
            self.data_display_data_panel_height,
            CHARCOAL_SLATE
        )

    def _create_navigation_buttons(self):
        self.navigation_buttons_names = {
            'confirm' : "Confirm",
            'go_back' : "Go Back"
        }
        self.navigation_buttons = []

    def _create_race_selection_buttons(self):
        self.race_selection_buttons = []
        self.race_selection_names = []
        race_data = list(ALL_RACES.values())
        self.number_of_race_buttons = len(race_data)
        self.full_height_of_race_buttons = (self.button_panel_button_height * self.number_of_race_buttons) + (self.button_panel_button_padding * (self.number_of_race_buttons - 1))
        current_y = self.button_panel_button_y - (self.full_height_of_race_buttons / 2)
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
                    self.button_panel_button_x,
                    current_y,
                    self.button_panel_button_width,
                    self.button_panel_button_height,
                    button_names['display_text'],
                    WHITE,
                    pygame.font.Font(FONT_PATH, CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_FONT_SIZE),
                    SLATE_GRAY,
                    MOSSY_STONE,
                    button_names['key_text']
                )
            )
            current_y += self.button_panel_button_height + self.button_panel_button_padding
                

    def _create_divider_line_dimensions(self):
        game_window_width, game_window_height = self.character_creation_screen_size
        self.divider_line_one_starting_x = game_window_width * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_ONE_STARTING_X
        self.divider_line_one_starting_y = CHARACTER_CREATION_SCREEN_DIVIDER_LINE_ONE_STARTING_Y
        self.divider_line_one_ending_x = game_window_width * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_ONE_ENDING_X
        self.divider_line_one_ending_y = game_window_height
        self.divider_line_two_starting_x = game_window_width * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_TWO_STARTING_X
        self.divider_line_two_starting_y = SCREEN_HEIGHT * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_TWO_STARTING_Y
        self.divider_line_two_ending_x = game_window_width
        self.divider_line_two_ending_y = SCREEN_HEIGHT * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_TWO_STARTING_Y

    def _create_race_selection_phase_layout(self):
        pass

    def _update_current_phase(self):
        phase_to_update = self.current_phase
        if phase_to_update == 'race_selection':
            pass
        elif phase_to_update == 'class_selection':
            pass
        elif phase_to_update == 'character_confirmation':
            pass

    def update(self):
        self._update_current_phase()

    def _draw_race_selection_phase(self):
        for index, value in enumerate(self.race_selection_buttons):
            button = value
            button.draw(self.surface)

    def _draw_class_selection_phase(self, surface):
        pass

    def _draw_character_confirmation_phase(self):
        pass

    def _draw_current_phase(self):
        phase_to_draw = self.current_phase
        if phase_to_draw == 'race_selection':
            self._draw_race_selection_phase()
        elif phase_to_draw == 'class_selection':
            self._draw_class_selection_phase()
        elif phase_to_draw == 'character_confirmation':
            self._draw_character_confirmation_phase()
    
    def draw(self, screen):
        self.surface.fill(CHARCOAL_SLATE)
        self.button_panel.draw(self.surface)
        self.phase_title_panel.draw(self.surface)
        self.data_display_panel.draw(self.surface)
        pygame.draw.line(self.surface, SLATE_GRAY, (self.divider_line_one_starting_x, self.divider_line_one_starting_y), (self.divider_line_one_ending_x, self.divider_line_one_ending_y), 2)
        pygame.draw.line(self.surface, SLATE_GRAY, (self.divider_line_two_starting_x, self.divider_line_two_starting_y), (self.divider_line_two_ending_x, self.divider_line_two_ending_y), 2)
        self._draw_current_phase()
        self.game.screen.blit(self.surface, (0, 0))

    def handle_phase_events(self, events):
        mouse_position = pygame.mouse.get_pos()
        event_phase = self.current_phase
        for event in events:
            pass

    def handle_events(self, events):
        self.handle_phase_events(events)