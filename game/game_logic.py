import random, time, pygame
import game.game_settings
from game.display import Display
settings = game.game_settings.init_settings()
SCREEN_WIDTH = settings['SCREEN_WIDTH']
SCREEN_HEIGHT = settings['SCREEN_HEIGHT']
target_radius = settings['target_radius']
def reset_game():
    return (random.randint(target_radius, SCREEN_WIDTH - target_radius),
            random.randint(target_radius, SCREEN_HEIGHT - target_radius),
            0,
            time.time())

def calculate_score(hit, current_time, last_hit_time):
    if hit:
        time_difference = current_time - last_hit_time
        score_increment = max(1, 10 - int(time_difference * 2))  # More points for faster hits
        return score_increment
    else:
        return -5  # Subtract points for a miss
    
def performance_message(score):
    if score > 50:
        return "Excellent Performance!"
    elif score > 20:
        return "Good Job!"
    else:
        return "Keep Practicing!"
    
def main():
    # Initialize Pygame and settings
    pygame.init()
    # Use the settings like so:
    SCREEN_WIDTH = settings['SCREEN_WIDTH']
    SCREEN_HEIGHT = settings['SCREEN_HEIGHT']
    BACKGROUND_COLOR = settings['BACKGROUND_COLOR']
    TARGET_COLOR = settings['TARGET_COLOR']
    TEXT_COLOR = settings['TEXT_COLOR']
    target_radius = settings['target_radius']

    # Setup the display, font, and clock
    screen = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']))
    pygame.display.set_caption("Aim Trainer")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    surface = pygame.Surface(screen.get_size())
    surface.set_alpha(128)

    # Create a Display instance
    display = Display(screen, surface, font, settings['BACKGROUND_COLOR'], settings['TEXT_COLOR'], settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT'])
    
    target_position_x, target_position_y, score, start_time = reset_game()
    last_hit_time = start_time
    game_duration = 10  # Duration of each round in seconds
    running = True
    paused = False
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                    if paused or game_over:
                        display.display_screen(paused, game_over, score) 
                elif event.key == pygame.K_r:
                    if paused or game_over:
                        target_position_x, target_position_y, score, start_time = reset_game()
                        last_hit_time = start_time
                        paused = False
                        game_over = False
                elif event.key is pygame.K_q:
                    running = False

            if not paused and not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    distance = ((mouse_x - target_position_x) ** 2 + (mouse_y - target_position_y) ** 2) ** 0.5
                    if distance < target_radius:
                        score_change = calculate_score(True, time.time(), last_hit_time)
                        last_hit_time = time.time()
                        target_position_x, target_position_y = random.randint(target_radius, SCREEN_WIDTH - target_radius), random.randint(target_radius, SCREEN_HEIGHT - target_radius)
                    else:
                        score_change = calculate_score(False, time.time(), last_hit_time)
                    score += score_change

        if not paused:
            screen.fill(BACKGROUND_COLOR)
            pygame.draw.circle(screen, TARGET_COLOR, (target_position_x, target_position_y), target_radius)
            score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
            screen.blit(score_text, (10, 10))

            if time.time() - start_time > game_duration and not game_over:
                game_over = True
                display.display_screen(False, True, score) # Display final score and menu
                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                target_position_x, target_position_y, score, start_time = reset_game()
                                last_hit_time = start_time
                                game_over = False
                                waiting_for_input = False
                                display.display_screen(False, False)
                            elif event.key == pygame.K_q:
                                running = False
                                waiting_for_input = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()