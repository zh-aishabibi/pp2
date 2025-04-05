import pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((500, 500))

running = True
start_ticks = pygame.time.get_ticks()  # Get the start time in milliseconds

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the elapsed time in milliseconds
    elapsed_time = pygame.time.get_ticks()  - start_ticks

    # Display the elapsed time on the screen
    font = pygame.font.SysFont(None, 40)
    text = font.render(f"Time: {elapsed_time // 1000} seconds", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(text, (50, 50))

    # Update the display
    pygame.display.flip()

pygame.quit()
