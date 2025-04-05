import pygame
pygame.init()

# Load an image
image = pygame.image.load("week7/images/clock.png")# F
imag = pygame.transform.scale(image, (800,600))
flipped_imag = pygame.transform.flip(imag, True, False) #flip the image horizontally

# Display the flipped image
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(flipped_imag, (0, 0))
    pygame.display.flip()
