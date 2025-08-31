from settings import *
from engine.state import State

class WelcomeScreen(State):
    def __init__(self, game):
        super().__init__(game)
        self.welcome_screen_size = self.game.screen.get_size()
        self.surface = pygame.Surface(self.welcome_screen_size)
        
    def draw(self, screen):
        self.game.screen.blit(self.surface, (0, 0))

    def handle_events(self, events):
        pass