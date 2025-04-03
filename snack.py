import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake settings
snake_speed = 5
snake_body = [(100, 50), (90, 50), (80, 50)]
direction = 'RIGHT'
change_to = direction

# Food position
food_pos = (random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, 
            random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE)
food_spawn = True

clock = pygame.time.Clock()

def show_score(score):
    font = pygame.font.SysFont('arial', 20)
    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

# Game loop
def game_loop():
    global direction, change_to, food_pos, food_spawn, snake_body
    score = 0

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Change direction
        direction = change_to
        x, y = snake_body[0]

        if direction == 'UP':
            y -= BLOCK_SIZE
        elif direction == 'DOWN':
            y += BLOCK_SIZE
        elif direction == 'LEFT':
            x -= BLOCK_SIZE
        elif direction == 'RIGHT':
            x += BLOCK_SIZE

        # Add new position
        new_head = (x, y)
        snake_body.insert(0, new_head)

        # Check collision with food
        if new_head == food_pos:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # Respawn food
        if not food_spawn:
            food_pos = (random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, 
                        random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE)
            food_spawn = True

        # Check collisions with boundaries or itself
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake_body[1:]:
            time.sleep(1)
            game_loop()  # Restart game

        # Draw everything
        screen.fill(BLUE)
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
        show_score(score)
        pygame.display.update()

        # Control speed
        clock.tick(snake_speed)

# Start game
game_loop()
