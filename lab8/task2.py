import pygame
from pygame.locals import *
import time
import random
pygame.init()

class Snake(pygame.sprite.Sprite):
    def __init__(self, size_of_main_screen):
        super().__init__()
        self.size_of_main_screen = size_of_main_screen
        self.image_0 = pygame.image.load("square.jpg")
        self.image = pygame.transform.scale(self.image_0, (40, 40))
        self.rect = self.image.get_rect()
        self.start_pos = (random.randint(5, size_of_main_screen[0] - 5), random.randint(5, size_of_main_screen[1] - 5))
        self.rect.center = self.start_pos
        self.speed = 5
    def move(self):
        self.touch_buttom = pygame.key.get_pressed()
        if self.touch_buttom[K_UP]:
            if self.rect.center[1] < 0:
                self.rect.center = (self.rect.center[0], 20)
            else:
                self.rect.center = (self.rect.center[0], self.rect.center[1] - self.speed)

        if self.touch_buttom[K_DOWN]:
            if self.rect.center[1]  > self.size_of_main_screen[1]:
                self.rect.center = (self.rect.center[0], self.rect.center[1] - 40)
            else:
                self.rect.center = (self.rect.center[0], self.rect.center[1] + self.speed)

        if self.touch_buttom[K_LEFT]:
            if self.rect.center[0]  < 0:
                self.rect.center = (20, self.rect.center[1])
            else:
                self.rect.center = (self.rect.center[0] - self.speed, self.rect.center[1])
        if self.touch_buttom[K_RIGHT]:
            if self.rect.center[0] > self.size_of_main_screen[0]:
                self.rect.center = (self.rect.center[0] - 40, self.rect.center[1])
            else:
                self.rect.center = (self.rect.center[0] + self.speed, self.rect.center[1])

    def paint(self, main_screen):
        self.main_screen = main_screen
        
        self.main_screen.blit(self.image, self.rect.center)

    def eda(self):
        self.steak = pygame.image.load("steak.png")
        self.image_steak = pygame.transform.scale(self.steak, (40, 40))
        self.rect_steak = self.image_steak.get_rect()
        self.rect_steak.center = (random.randint(20, self.size_of_main_screen[0] - 20), random.randint(20, self.size_of_main_screen[1] - 20))

    def build_eda(self):
        self.main_screen.blit(self.image_steak, self.rect_steak.center)
        
points = 0
point_font = pygame.font.SysFont("Vergana", 30)
level_font = pygame.font.SysFont("Vergana", 30)
main_screen = pygame.display.set_mode((700, 700))

some_snake = Snake(main_screen.get_rect().size)
level = 0
FramePerSecond = pygame.time.Clock()
cnt = 0
FPS = 60
flag = True
while True:
    if cnt == 4:
        cnt = 0
        if some_snake.speed <= 10:
            some_snake.speed += 2
            level += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if flag:
        some_snake.eda()
        flag = False
        while some_snake.rect_steak.colliderect(some_snake.rect):
            some_snake.eda()

    main_screen.fill(pygame.Color("green"))
    some_snake.paint(main_screen)
    pic_coin = point_font.render("Score: " + str(points), True, pygame.Color("blue"))
    pic_level = level_font.render("Level: " + str(level), True, pygame.Color("yellow"))
    main_screen.blit(pic_coin, (some_snake.size_of_main_screen[0] - 95, 18))
    main_screen.blit(pic_level, (some_snake.size_of_main_screen[0] - 79, 45))
    some_snake.move()
    
    if not flag:
        some_snake.build_eda()
    
    

    if some_snake.rect.colliderect(some_snake.rect_steak):
        flag = True
        points += 1
        cnt += 1
    pygame.display.update()

    FramePerSecond.tick(FPS)

    


