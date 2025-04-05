import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))  # Create a window of size 800x600
pygame.display.set_caption("flip() Example")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))  # Draw a red rectangle
    

pygame.quit()
