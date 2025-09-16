from data.classes.all_classes import ALL_CLASSES
from screens.character_creation_phases.selection_phase import SelectionPhase
from screens.character_creation_phases.data_ui_panel import ClassDataPanel

class ClassSelectionPhase(SelectionPhase):
    def __init__(self, screenmanager):
        super().__init__(screenmanager, list(ALL_CLASSES.values()), "Choose Your Class", ClassDataPanel)

    def _on_selection(self, key_text):
        self.info_panel_data.set_current_phase_category(key_text)

    def _is_selection_made(self):
        if self.info_panel_data.current_phase_category is not None:
            return True
        else:
            return False
        
    def _on_confirm(self):
        self.manager.player_choices['class'] = self.info_panel_data.current_phase_category
        self.manager.current_phase = 'class_selection'

    def _on_go_back(self):
        self.manager.current_phase = 'race_selection'