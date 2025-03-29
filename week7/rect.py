import pygame
from sys import exit 

def disscore():
    current = pygame.time.get_ticks() - start
    c = int(current/1000)
    scoresurf = f.render(f"Time: {c}", False, (64,64,64))
    rectscore = scoresurf.get_rect(center = (400,50))
    screen.blit (scoresurf, rectscore)

pygame.init()
start = 0
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

active = True

surface2 = pygame.image.load("Sky.png").convert() 
groundsur = pygame.image.load("ground.png").convert()
stand = pygame.image.load("player_stand.png").convert_alpha()
sized = pygame.transform.scale2x(stand)
standrect = sized.get_rect(center = (400,200))

f = pygame.font.Font(r"c:\Users\Адина\Downloads\Pixeltype.ttf", 50)

surface3 = f.render("youtube", False, (111,196,200))
scorerect = surface3.get_rect(center = (400,50))

restart = f.render("restart", False, (111,196,200))
restartrect = restart.get_rect(center= (400, 351))

snail = pygame.image.load("snail1.png").convert_alpha()
snailrect = snail.get_rect(midbottom = (700 ,300))

gravity =0

player = pygame.image.load("player_walk_1.png").convert_alpha()
playerrect = player.get_rect(midbottom = (80,300)) #rectangle around player
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()
        if active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playerrect.collidepoint(event.pos) and playerrect.bottom >= 300:
                    gravity = -20     

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and playerrect.bottom >= 300:
                    gravity = -20 
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                active = True
                snailrect.left = 800
                start = pygame.time.get_ticks()

    if active:

        screen.blit(surface2, (0,0)) #surf, position in x y 
        screen.blit(groundsur, (0,300))
        disscore()
            
        snailrect.left -= 6                             
        if snailrect.left < -100:
            snailrect.left = 800
        screen.blit(snail,snailrect)

        gravity += 1
        playerrect.bottom += gravity 
            # playerrect.left += 4
            # if playerrect.left >=850:
            #     playerrect.left = -50            
        if playerrect.bottom > 300:
             playerrect.bottom = 300

        screen.blit(player, playerrect)

        if playerrect.colliderect(snailrect):
                active = False 
                screen.fill((94,129,162))
                screen.blit(sized, standrect)
                screen.blit(surface3, scorerect)
                screen.blit(restart, restartrect)

        pygame.display.update()
        clock.tick(60)