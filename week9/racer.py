import pygame, sys, random, time
from pygame.locals import *

pygame.init()

# Настройка FPS (кадров в секунду)
FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 405
SCREEN_HEIGHT = 600
SPEED = 5 
SCORE = 0  
COINS = 0 
level = 5 
L =0

font = pygame.font.SysFont("Verdana", 60)  
font_small = pygame.font.SysFont("Verdana", 20)  
game_over = font.render("Game Over", True, BLACK)  

background = pygame.image.load("week8/images/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Race")

# Класс врага (движется сверху вниз)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("week8/images/Enemy.png")  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) 

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) # Двигаем вниз
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1  # Увеличиваем очки
            self.rect.top = 0  # Перемещаем врага наверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс монет (игрок может собирать)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("week8/images/coin.png")  
        self.image = pygame.transform.scale(self.image, (30, 30))  # Уменьшаем размер
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  # Начальное положение

    def move(self):
        self.rect.move_ip(0, SPEED)  # Двигаем вниз
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0  # Перемещаем монету наверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("week8/images/coin.png")  
        self.image = pygame.transform.scale(self.image, (50, 50))  # Уменьшаем размер
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  # Начальное положение

    def move(self):
        self.rect.move_ip(0, SPEED)  # Двигаем вниз
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0  # Перемещаем монету наверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока (управляемая машина)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("week8/images/Player.png")  
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # Начальная позиция игрока

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)  # Движение влево
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)  # Движение вправо

# Создание игровых объектов
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

coins2 = pygame.sprite.Group()
coins.add(C2)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

# Игровой цикл
while True:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка фона и счёта
    DISPLAYSURF.blit(background, (0, 0))
    
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    level_text = font_small.render(f"Level: {L}", True, BLACK)
    
    DISPLAYSURF.blit(score_text, (10, 10))  # Очки врагов слева
    DISPLAYSURF.blit(coin_text, (300, 10))  # Количество монет справа
    DISPLAYSURF.blit(level_text, (300,50))  # Уровень по центру

    # Обновляем положение всех объектов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()  # Проигрываем звук аварии
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)  # Красный экран при Game Over
        DISPLAYSURF.blit(game_over, (30, 250))  # Отображаем "Game Over"

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Удаляем все спрайты
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка столкновения игрока с монетой
    collected_coin = pygame.sprite.spritecollideany(P1, coins)
    if collected_coin:
        collected_coin.kill()  # Удаляем монету
        COINS += 1  # Увеличиваем счётчик монет

     # Проверка столкновения игрока с монетой
    collected_coin = pygame.sprite.spritecollideany(P1, coins2)
    if collected_coin:
        collected_coin.kill()  # Удаляем монету
        COINS += 2  # Увеличиваем счётчик монет

    if COINS >= level:
        SPEED += 1
        level += 5
        L +=1
    
    # Если все монеты собраны, создаём новую монету
    if len(coins) == 0:
        new_coin = Coin()
        new = Coin2()
        coins.add(new_coin)
        coins2.add(new)
        all_sprites.add(new_coin)
        all_sprites.add(new)

    # Обновляем экран и FPS
    pygame.display.update()
    FramePerSec.tick(FPS)

"""
🎯 Монеты дают от 1 до 2 очков

🔺 Каждые 5 монет = новый уровень

🏎️ Скорость увеличивается с каждым level

❌ Столкновение = Game Over

"""