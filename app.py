import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Full-Screen Mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
pygame.display.set_caption("Aim Trainer")

# Colors
BACKGROUND_COLOR = (45, 45, 45)  # Dark grey, eye-friendly
TARGET_COLOR = (70, 130, 180)
TEXT_COLOR = (255, 255, 255)  # White for text

# Game Variables
target_radius = 50  # Increased target size
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
surface = pygame.Surface(screen.get_size())
surface.set_alpha(128)  # Alpha for blurred background

def reset_game():
    return (random.randint(target_radius, SCREEN_WIDTH - target_radius),
            random.randint(target_radius, SCREEN_HEIGHT - target_radius),
            0,
            time.time())

def display_menu(paused):
    surface.fill(BACKGROUND_COLOR)
    screen.blit(surface, (0, 0))
    menu_text = font.render("R: Resume - Q: Quit", True, TEXT_COLOR) if paused else font.render("Game Over! R: Replay - Q: Quit", True, TEXT_COLOR)
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 15))
    pygame.display.flip()

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

def game_loop():
    target_position_x, target_position_y, score, start_time = reset_game()
    last_hit_time = start_time
    game_duration = 30
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
                        display_menu(paused)
                elif event.key == pygame.K_r:
                    if paused or game_over:
                        target_position_x, target_position_y, score, start_time = reset_game()
                        last_hit_time = start_time
                        paused = False
                        game_over = False
                elif event.key == pygame.K_q:
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
                message = performance_message(score)
                display_menu(game_over)
                performance_text = font.render(message, True, TEXT_COLOR)
                screen.blit(performance_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20))
                pygame.display.flip()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
