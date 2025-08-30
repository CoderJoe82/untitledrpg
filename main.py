from engine.game import Game

if __name__ == '__main__':
    game = Game()
    game.run()

#
# GAME STRUCTURE BLUEPRINT
#
# -----------------------------------------------------------------------------
# I. OVERALL DESIGN: STATE MACHINE
# -----------------------------------------------------------------------------
#
# - The game exists in one 'state' at a time (e.g., MainMenu, Gameplay, Paused).
# - A central 'Game' controller manages the active state.
# - This avoids complex if/elif/else logic in the main loop.
# - The main loop's only job is to delegate tasks to the current state.
#
# -----------------------------------------------------------------------------
# II. CORE COMPONENTS
# -----------------------------------------------------------------------------
#
# 1. The Main 'Game' Class (The Controller)
#    - Initializes Pygame, the screen, and the clock.
#    - Holds a dictionary containing an instance of every state (e.g., self.states = {"menu": MainMenu(), "game": Gameplay()}).
#    - Holds a variable for the currently active state (e.g., self.current_state).
#    - Contains the main game loop.
#    - Contains a method to handle state transitions (e.g., change_state("gameplay")).
#
# 2. The Base 'State' Class (A Generic Template)
#    - All specific states (MainMenu, etc.) will inherit from this class.
#    - It ensures every state has the same essential methods.
#    - Essential methods for every state to have:
#      - __init__(self, game): To get a reference to the main game controller.
#      - handle_events(self, events): To process player input (keyboard, mouse).
#      - update(self): To update game logic (movement, timers, AI).
#      - draw(self, screen): To render all visuals to the screen.
#
# 3. Specific State Classes (e.g., MainMenu, Gameplay)
#    - Inherits from the base 'State' class.
#    - Implements its own unique logic for the handle_events, update, and draw methods.
#    - For example, the MainMenu's handle_events checks for button clicks, while Gameplay's checks for player movement keys.
#    - Each state is a self-contained module.
#
# -----------------------------------------------------------------------------
# III. THE MAIN GAME LOOP (Inside the Game class)
# -----------------------------------------------------------------------------
#
# - The loop should be kept simple.
# - While running:
#   1. Get events from pygame.event.get().
#   2. Pass those events to the current state: self.current_state.handle_events(events).
#   3. Update the current state: self.current_state.update().
#   4. Draw the current state: self.current_state.draw(self.screen).
#   5. Update the main display and tick the clock.
#
# -----------------------------------------------------------------------------
# IV. GOOD PRACTICES & ORGANIZATION
# -----------------------------------------------------------------------------
#
# 1. Constants File (e.g., settings.py)
#    - Create a separate file for global variables that don't change.
#    - Examples: SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLORS, TILE_SIZE.
#    - Import these constants where needed to avoid 'magic numbers'.
#
# 2. Data-Driven Design
#    - Separate game data from game logic.
#    - Store stats for items, characters, enemies, etc., in external files (JSON is great for this).
#    - The game loads this data at startup instead of having it hard-coded.
#
# 3. Asset Management
#    - Create a central place (a class or a dictionary in the Game object) to load assets.
#    - Load all images, fonts, and sounds ONCE when the game starts.
#    - This prevents slow, repetitive file loading during gameplay.
#    - States can then request assets from this central manager.
#