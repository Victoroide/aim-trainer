import pygame
from game.game_settings import init_settings
from game.game_logic import main

def dev():
    settings = init_settings()

    pygame.init()

    screen = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']))
    pygame.display.set_caption("Aim Trainer")

    main()

if __name__ == "__main__":
    dev()
