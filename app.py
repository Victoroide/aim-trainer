import pygame
from game.game_settings import init_settings
from game.game_logic import main

def dev():
    # Initialize settings
    settings = init_settings()

    # Initialize Pygame
    pygame.init()

    # Setup the screen and other Pygame objects
    screen = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']))
    pygame.display.set_caption("Aim Trainer")

    # More initialization as needed, then start the game loop
    main()

if __name__ == "__main__":
    dev()
