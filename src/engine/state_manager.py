import pygame
import sys
from abc import ABC, abstractmethod

class StateManager:
    def __init__(self, game):
        self.game = game
        self.states = {}
        self.current_state = None

    def change_state(self, state_name):
        if state_name in self.states:
            self.current_state = self.states[state_name]
            print(f"Switching to {state_name}")

    def handle_events(self, event):
        if self.current_state:
            self.current_state.handle_events(event)

    def update(self):
        if self.current_state:
            self.current_state.update()

    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)

class GameState(ABC):
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def handle_events(self, event):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass