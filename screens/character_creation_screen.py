import pygame
from settings import *
from engine.state import State
from screens.button import Button
from screens.ui_panel import UI_Panel
from data.races.all_races import ALL_RACES
from screens.character_creation_phases.race_selection_phase import RaceSelectionPhase

class CharacterCreationScreen(State):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.character_creation_screen_size = self.game.screen.get_size()
        self.surface = pygame.Surface(self.character_creation_screen_size)
        self._create_character_creation_panel_dimensions()
        self._create_button_panel_button_dimensions()
        self._create_divider_line_dimensions()
        self._create_character_creation_panels()
        self._create_navigation_button_dimensions()
        self.phases = {
            'race_selection' : RaceSelectionPhase(self),
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
        self.data_display_data_panel_y = game_window_height * CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_STARTING_Y
        self.data_display_data_panel_width = game_window_width * CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_WIDTH
        self.data_display_data_panel_height = game_window_height * CHARACTER_CREATION_SCREEN_DISPLAY_DATA_PANEL_HEIGHT
        
    def _create_character_creation_panels(self):
        self.button_panel = UI_Panel(
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

    def _create_divider_line_dimensions(self):
        game_window_width, game_window_height = self.character_creation_screen_size
        self.divider_line_one_starting_x = game_window_width * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_ONE_STARTING_X
        self.divider_line_one_starting_y = CHARACTER_CREATION_SCREEN_DIVIDER_LINE_ONE_STARTING_Y
        self.divider_line_one_ending_x = game_window_width * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_ONE_ENDING_X
        self.divider_line_one_ending_y = game_window_height
        self.divider_line_two_starting_x = game_window_width * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_TWO_STARTING_X
        self.divider_line_two_starting_y = game_window_height * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_TWO_STARTING_Y
        self.divider_line_two_ending_x = game_window_width
        self.divider_line_two_ending_y = game_window_height * CHARACTER_CREATION_SCREEN_DIVIDER_LINE_TWO_STARTING_Y

    def _create_button_panel_button_dimensions(self):
        self.button_panel_button_width = self.button_ui_panel_width * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_WIDTH
        self.button_panel_button_height = self.button_ui_panel_height * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_HEIGHT
        self.button_panel_button_x = (self.button_ui_panel_width * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_STARTING_X) - (self.button_panel_button_width / 2)
        self.button_panel_button_y = self.button_ui_panel_height * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_STARTING_Y
        self.button_panel_button_padding = self.button_ui_panel_height * CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_PADDING

    def _create_navigation_button_dimensions(self):
        self.navigation_button_width = self.data_display_data_panel_width * CHARACTER_CREATION_SCREEN_NAVIGATION_BUTTON_WIDTH
        self.navigation_button_height = self.data_display_data_panel_height * CHARACTER_CREATION_SCREEN_NAVIGATION_BUTTON_HEIGHT
        self.navigation_starting_y = self.data_display_data_panel_y + (self.data_display_data_panel_height * CHARACTER_CREATION_SCREEN_NAVIGATION_BUTTON_Y)
        self.navigation_starting_x = self.data_display_data_panel_x + (self.data_display_data_panel_width * CHARACTER_CREATION_SCREEN_NAVIGATION_BUTTON_X)
        self.navigation_button_padding = self.data_display_data_panel_width * CHARACTER_CREATION_SCREEN_NAVIGATION_BUTTON_PADDING

    def update(self):
        self.phases[self.current_phase].update()
        
    def draw_current_phase(self):
        self.phases[self.current_phase].draw(self.surface)
    
    def draw(self, screen):
        self.surface.fill(CHARCOAL_SLATE)
        self.button_panel.draw(self.surface)
        self.phase_title_panel.draw(self.surface)
        self.data_display_panel.draw(self.surface)
        self.draw_current_phase()
        pygame.draw.line(self.surface, SLATE_GRAY, (self.divider_line_two_starting_x, self.divider_line_two_starting_y), (self.divider_line_two_ending_x, self.divider_line_two_ending_y), 2)
        pygame.draw.line(self.surface, SLATE_GRAY, (self.divider_line_one_starting_x, self.divider_line_one_starting_y), (self.divider_line_one_ending_x, self.divider_line_one_ending_y), 2)
        self.game.screen.blit(self.surface, (0, 0))        

    def handle_events(self, events):
        self.phases[self.current_phase].handle_events(events)