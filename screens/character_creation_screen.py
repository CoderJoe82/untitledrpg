import pygame
from settings import *
from engine.state import State
from screens.button import Button

class CharacterCreationScreen(State):
    def __init__(self, game):
        super().__init__(game)
        self.character_creation_screen_size = self.game.screen.get_size()
        self.surface = pygame.Surface(self.character_creation_screen_size)
        self.phases = {
            'race_selection' : {...},
            'class_selection' : {...},
            'character_confirmation' : {...}
        }
        self.current_phase = 'race_selection'

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
        pass

    def _draw_class_selection_phase(self):
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
    
    def draw(self):
        self.surface.fill(CHARCOAL_SLATE)
        self._draw_current_phase()
        self.game.screen.blit(self.surface, (0, 0))

    def handle_phase_events(self, events):
        mouse_position = pygame.mouse.get_pos()
        event_phase = self.current_phase
        for event in events:
            for index, value in enumerate(character_selection_screen_buttons):
                button = value
                if button.is_clicked(event, mouse_position):
                    if button.key_text == 'race_selection':
                        self.current_phase = 'race_selection'
                    elif button.key_text == 'class_selection':
                        self.current_phase = 'class_selection'
                    elif button.key_text == 'character_confirmation':
                        self.current_phase = 'character_confirmation'

    def handle_events(self, events):
        self.handle_phase_events(events)