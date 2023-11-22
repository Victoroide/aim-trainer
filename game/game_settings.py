import pygame
def init_settings():
    pygame.init()
    display_info = pygame.display.Info()
    SCREEN_WIDTH, SCREEN_HEIGHT = display_info.current_w, display_info.current_h

    BACKGROUND_COLOR = (45, 45, 45)  # Dark grey, eye-friendly
    TARGET_COLOR = (70, 130, 180)
    TEXT_COLOR = (255, 255, 255)  # White for text

    target_radius = 50

    return {
        "SCREEN_WIDTH": SCREEN_WIDTH,
        "SCREEN_HEIGHT": SCREEN_HEIGHT,
        "BACKGROUND_COLOR": BACKGROUND_COLOR,
        "TARGET_COLOR": TARGET_COLOR,
        "TEXT_COLOR": TEXT_COLOR,
        "target_radius": target_radius,
    }
