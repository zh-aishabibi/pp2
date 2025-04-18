import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Avoid the Obstacle")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define object sizes
object_size = 50
obstacle_size = 40

# Initialize player positions
player1_pos = [100, 300]  # Object 1 controlled with arrow keys
player2_pos = [600, 300]  # Object 2 controlled with WASD keys

# Object movement speed
player_speed = 5
obstacle_speed = 3

# Initialize obstacle position
obstacle_pos = [random.randint(0, 750), 0]

# Score counter
score = 0
font = pygame.font.SysFont('Arial', 30)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses for movement
    keys = pygame.key.get_pressed()

    # Control player 1 with arrow keys
    if keys[pygame.K_LEFT]:
        player1_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player1_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player1_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player1_pos[1] += player_speed

    # Control player 2 with WASD keys
    if keys[pygame.K_a]:
        player2_pos[0] -= player_speed
    if keys[pygame.K_d]:
        player2_pos[0] += player_speed
    if keys[pygame.K_w]:
        player2_pos[1] -= player_speed
    if keys[pygame.K_s]:
        player2_pos[1] += player_speed

    # Update obstacle position (moving down)
    obstacle_pos[1] += obstacle_speed

    # Reset obstacle if it goes off the screen
    if obstacle_pos[1] > 600:
        obstacle_pos = [random.randint(0, 750), 0]
        score += 1  # Increase score when obstacle is avoided

    # Check for collisions with players
    player1_rect = pygame.Rect(player1_pos[0], player1_pos[1], object_size, object_size)
    player2_rect = pygame.Rect(player2_pos[0], player2_pos[1], object_size, object_size)
    obstacle_rect = pygame.Rect(obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size)

    if player1_rect.colliderect(obstacle_rect) or player2_rect.colliderect(obstacle_rect):
        running = False  # End game if collision occurs

    # Draw everything
    screen.fill(BLACK)  # Clear screen

    # Draw players
    pygame.draw.rect(screen, GREEN, player1_rect)  # Player 1
    pygame.draw.rect(screen, BLUE, player2_rect)  # Player 2

    # Draw obstacle
    pygame.draw.rect(screen, RED, obstacle_rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  # Update the screen
    pygame.time.Clock().tick(60)  # Set frame rate

# Quit Pygame
pygame.quit()
