import pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((500, 500))

# Pause for 2 seconds (2000 milliseconds)
pygame.time.delay(2000)

screen.fill((255, 255, 255))
pygame.display.flip()

# Wait for the user to close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
