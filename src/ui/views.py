import pygame
import sys
from engine.state_manager import GameState
from ui.widgets import Button
from settings import TITLE_SCREEN_BUTTON_WIDTH, TITLE_SCREEN_BUTTON_HEIGHT, TITLE_SCREEN_BUTTON_Y_START, TITLE_SCREEN_BUTTON_Y_PADDING

class MainMenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 36)
        self.button_width = TITLE_SCREEN_BUTTON_WIDTH
        self.button_height = TITLE_SCREEN_BUTTON_HEIGHT
        self.button_names = ["New Game", "Load Game", "Options", "Quit"]
        self.buttons = []
        self.screen_width = self.game.screen.get_width()
        self.screen_height = self.game.screen.get_height()
        self.create_buttons()

    def create_buttons(self):
        #  def __init__(self, x, y, width, height, text, font):
        current_x = (self.screen_width  / 2) - (self.button_width / 2)
        current_y = self.screen_height * TITLE_SCREEN_BUTTON_Y_START
        for name in self.button_names:
            self.buttons.append(Button(current_x, current_y, self.button_width, self.button_height, name, self.font))
            current_y += self.button_height + TITLE_SCREEN_BUTTON_Y_PADDING
            

    def draw(self, screen):
        screen.blit(self.game.background, (0, 0))
        for button in self.buttons:
            button.draw(screen, (200, 200, 200))

    def handle_events(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                if button.text == "Quit":
                    pygame.quit()
                    sys.exit()
                elif button.text == "New Game":
                    print("Start!")

    def update(self):
        pass