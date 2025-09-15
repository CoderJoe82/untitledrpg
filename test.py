# import pygame
# from settings import *
# from screens.button import Button
# from data.races.all_races import ALL_RACES
# from screens.character_creation_phases.character_creation_phase import CharacterCreationPhase
# from engine.utils import draw_formatted_text


# class SelctionPhase(CharacterCreationPhase):
#     def __init__(self, screen_manager, data_list, header_rect_text, panel):
#         super().__init__(screen_manager)
#         self.manager = screen_manager
#         self.panel = panel
#         self.info_panel_data = panel(
#             self.manager.data_display_data_panel_x,
#             self.manager.data_display_data_panel_y,
#             self.manager.data_display_data_panel_width,
#             self.manager.data_display_data_panel_height,
#             self.manager.navigation_starting_y,
#             self.manager.character_creation_screen_size
#         )
#         self.character_data = data_list
#         self.header_rect_text = header_rect_text
#         self._create_phase_selection_buttons()
#         self._create_race_navigation_buttons()
#         self._create_header_text()

#     def _create_phase_selection_buttons(self):
#         self.phase_selection_buttons = []
#         self.phase_selection_button_names = []
#         self.number_of_phase_buttons = len(self.character_data)
#         self.full_height_of_phase_buttons = (
#             self.manager.button_panel_button_height * self.number_of_phase_buttons
#         ) + (
#             self.manager.button_panel_button_padding * (self.number_of_phase_buttons - 1)
#         )
#         current_y = self.manager.button_panel_button_y - (
#             self.full_height_of_phase_buttons / 2
#         )
#         for index, value in enumerate(self.character_data):
#             data = value
#             self.phase_selection_button_names.append(
#                 {
#                     "key_text": data["id"],
#                     "display_text": data["display_name"],
#                     "font_color": data["font_color"],
#                 }
#             )
#         for index, value in enumerate(self.phase_selection_button_names):
#             button_names = value
#             self.phase_selection_buttons.append(
#                 Button(
#                     self.manager.button_panel_button_x,
#                     current_y,
#                     self.manager.button_panel_button_width,
#                     self.manager.button_panel_button_height,
#                     [
#                         [
#                             (
#                                 button_names["display_text"][0],
#                                 button_names["font_color"],
#                             ),
#                             (button_names["display_text"][1:], WHITE),
#                         ]
#                     ],
#                     WHITE,
#                     pygame.font.Font(
#                         FONT_PATH,
#                         CHARACTER_CREATION_SCREEN_BUTTON_PANEL_BUTTON_FONT_SIZE,
#                     ),
#                     SLATE_GRAY,
#                     MOSSY_STONE,
#                     button_names["key_text"],
#                 )
#             )
#             current_y += (
#                 self.manager.button_panel_button_height
#                 + self.manager.button_panel_button_padding
#             )

#     def _create_race_navigation_buttons(self):
#         self.navigation_buttons = []
#         self.navigation_button_texts = {"confirm": "Confirm", "go_back": "Go Back"}
#         self.number_of_navigation_buttons = len(self.navigation_button_texts)
#         self.full_width_of_navigation_buttons = (
#             self.manager.navigation_button_width * self.number_of_navigation_buttons
#         ) + self.manager.navigation_button_padding
#         current_x = self.manager.navigation_starting_x - (
#             self.full_width_of_navigation_buttons / 2
#         )
#         for key, value in self.navigation_button_texts.items():
#             key_text = key
#             button_text = value
#             self.navigation_buttons.append(
#                 Button(
#                     current_x,
#                     self.manager.navigation_starting_y,
#                     self.manager.navigation_button_width,
#                     self.manager.navigation_button_height,
#                     button_text,
#                     WHITE,
#                     pygame.font.Font(
#                         FONT_PATH, CHARACTER_CREATION_SCREEN_NAVIGATION_BUTTON_FONT_SIZE
#                     ),
#                     SLATE_GRAY,
#                     MOSSY_STONE,
#                     key_text,
#                 )
#             )
#             current_x += (
#                 self.manager.navigation_button_width
#                 + self.manager.navigation_button_padding
#             )

#     def _create_header_text(self):
#         self.header_rect = pygame.Rect(
#             self.manager.phase_title_panel_x,
#             self.manager.phase_title_panel_y,
#             self.manager.phase_title_panel_width,
#             self.manager.phase_title_panel_height,
#         )
#         self.header_rect_display_text = self.header_rect_text
#         self.header_rect_font = pygame.font.Font(FONT_PATH, LARGE_FONT_SIZE)
#         self.header_rect_display_text_alignment = "center"
#         self.header_rect_display_text_vert_alignment = "center"

#     def update(self):
#         mouse_position = pygame.mouse.get_pos()
#         for button in self.phase_selection_buttons:
#             button.update(mouse_position)
#         for button in self.navigation_buttons:
#             button.update(mouse_position)

#     def _on_confirm(self):
#         pass

#     def _on_go_back(self):
#         pass
    
#     def _on_selection(self):
#         pass
    
#     def _is_selection_made(self):
#         pass

#     def draw(self, surface):
#         draw_formatted_text(
#             surface,
#             [[(self.header_rect_display_text, WHITE)]],
#             self.header_rect,
#             self.header_rect_font,
#             self.header_rect_display_text_alignment,
#             self.header_rect_display_text_vert_alignment,
#         )
#         self.info_panel_data.draw(surface)
#         for button in self.phase_selection_buttons:
#             button.draw(surface)
#         for button in self.navigation_buttons:
#             button.draw(surface)

#     def handle_events(self, events):
#         mouse_position = pygame.mouse.get_pos()
#         for event in events:
#             for button in self.navigation_buttons:
#                 if button.is_clicked(event, mouse_position):
#                     if button.key_text == "go_back":
#                         self._on_go_back()
#                     if button.key_text == "confirm":
#                         if self._is_selection_made():
#                             self._on_confirm()
#             for button in self.phase_selection_buttons:
#                 if button.is_clicked(event, mouse_position):
#                     self._on_selection(button.key_text)