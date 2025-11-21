import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE, GAME_TITLE
from models.player import Player
from engine.state_manager import StateManager
from ui.views import MainMenuState

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('assets/images/title_screen_background.png')
        self.is_running = True
        self.state_manager = StateManager(self)
        self.state_manager.states = {
            "main_menu" : MainMenuState(self)
        }
        self.state_manager.change_state("main_menu")
        self.player = Player()
        print(f"Player created with {self.player.hp} HP")

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FRAME_RATE)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.state_manager.handle_events(event)

    def update(self):
        self.state_manager.update()

    def draw(self):
        self.state_manager.draw(self.screen)
        pygame.display.flip()