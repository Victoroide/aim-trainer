import pygame

class Display:
    def __init__(self, screen, surface, font, background_color, text_color, screen_width, screen_height):
        self.screen = screen
        self.surface = surface
        self.font = font
        self.background_color = background_color
        self.text_color = text_color
        self.screen_width = screen_width
        self.screen_height = screen_height

    def display_screen(self, paused, game_over, score=None):
        self.surface.fill(self.background_color)
        self.screen.blit(self.surface, (0, 0))

        if game_over and score is not None:
            final_score_text = self.font.render(f"Final Score: {score}", True, self.text_color)
            self.surface.blit(final_score_text, (self.screen_width // 2 - final_score_text.get_width() // 2, self.screen_height // 2 - 50))

        if paused:
            menu_text = self.font.render("R: Resume - Q: Quit", True, self.text_color)
        elif game_over:
            menu_text = self.font.render("Game Over! R: Replay - Q: Quit", True, self.text_color)
        else:
            menu_text = self.font.render("", True, self.text_color) 

        self.screen.blit(menu_text, (self.screen_width // 2 - menu_text.get_width() // 2, self.screen_height // 2 - 15))
        pygame.display.flip()
