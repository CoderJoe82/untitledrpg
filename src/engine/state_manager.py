import pygame
import sys
from abc import ABC, abstractmethod
from ui.widgets import Button

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