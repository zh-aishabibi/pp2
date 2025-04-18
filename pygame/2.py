import pygame,sys
pygame.init()

clock = pygame.time.Clock()
w = 800
h = 600
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("paint")
active_color = (0,0,0)
active_size = 0
painting = []

def draw_menu():
    pygame.draw.rect(screen, "gray",(0,0,w,70))
    pygame.draw.line(screen, "black", (0, 70), (w, 70), 2)
    xl_brush = pygame.draw.rect(screen, "black", (10, 10, 50, 50))
    pygame.draw.circle(screen, "white", (35,35), 20)
    l_brush = pygame.draw.rect(screen, "black", (70, 10, 50, 50))
    pygame.draw.circle(screen, "white", (95,35), 15)
    m_brush = pygame.draw.rect(screen, "black", (130, 10, 50, 50))
    pygame.draw.circle(screen, "white", (155,35), 10)
    s_brush = pygame.draw.rect(screen, "black", (190, 10, 50, 50))
    pygame.draw.circle(screen, "white", (215,35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    blue = pygame.draw.rect(screen, "blue", (w-35,10,25,25))
    red = pygame.draw.rect(screen, "red", (w-35,35,25,25))
    green = pygame.draw.rect(screen, "green", (w-60,10,25,25))
    yellow = pygame.draw.rect(screen, "yellow", (w-60,35,25,25))
    teal = pygame.draw.rect(screen, (0,255,255), (w-85,10,25,25))
    purple = pygame.draw.rect(screen, (255,0,255), (w-85,35,25,25))
    white = pygame.draw.rect(screen, (0,0,0,), (w-110,10,25,25))
    black = pygame.draw.rect(screen, (255,255,255), (w-110,35,25,25))

    rbd_list = [(0,0,255), (255,0,0), (0,255,0), (255,255,0), (0,255,255), (255,0,255), (0,0,0), (255,255,255)]
    color_rect = [blue, red, green, yellow, teal, purple, white, black]
    return brush_list, color_rect, rbd_list
def draw(paints):
     for i in range(len(paints)):
            pygame.draw.circle(screen, paints[i][0], (paints[i][1]), paints[i][2])

run = True
while run:
    clock.tick(120)
    screen.fill("white") 

    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    if left_click and mouse[1] > 70:
         painting.append((active_color, mouse, active_size))

    if mouse[1] > 70:
         pygame.draw.circle(screen, active_color, mouse, active_size)

    draw(painting)
    brushes , colors , r = draw_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(brushes)):
                    if brushes[i].collidepoint(event.pos):
                        active_size = 20-(i*5)

        if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(colors)):
                    if colors[i].collidepoint(event.pos):
                        active_color = r[i]

        

    pygame.display.flip() 
pygame.quit()