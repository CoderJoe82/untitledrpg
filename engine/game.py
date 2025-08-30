from settings import *
import pygame
from screens.title_screen import TitleScreen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.title_screen = TitleScreen(self)
        self.current_state = self.title_screen

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            if self.current_state:
                self.current_state.handle_events(events)
                self.current_state.update()

            self.draw()
    
    def draw(self):
        if self.current_state:
            self.current_state.draw(self.screen)

        pygame.display.flip()