from settings import *
from engine.state import State

class TitleScreen(State):
    def __init__(self, game):
        super().__init__(game)

    def draw(self, screen):
        screen.fill(WHITE)