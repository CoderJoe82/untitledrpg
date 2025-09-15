from data.races.all_races import ALL_RACES
from screens.character_creation_phases.selection_phase import SelectionPhase
from screens.character_creation_phases.data_ui_panel import RaceDataPanel

class RaceSelectionPhase(SelectionPhase):
    def __init__(self, screenmanager):
        super().__init__(screenmanager, list(ALL_RACES.values()), "Choose Your Race", RaceDataPanel)

    def _on_selection(self, key_text):
        self.info_panel_data.set_current_phase_category(key_text)

    def _is_selection_made(self):
        if self.info_panel_data.current_phase_category is not None:
            return True
        else:
            return False
        
    def _on_confirm(self):
        self.manager.current_phase = 'class_selection'

    def _on_go_back(self):
        self.manager.game.change_game_state('welcome')