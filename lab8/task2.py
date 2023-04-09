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
        self.copy = pygame.transform.scale(self.image_0, (40, 40))
        self.rect = self.image.get_rect()
        self.start_pos = (random.randint(5, size_of_main_screen[0] - 5), random.randint(5, size_of_main_screen[1] - 5))
        self.rect.center = self.start_pos
        self.speed = 5
        self.gameover = False
        self.massive_snake = [self.rect.center]
        self.add_part = 0
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.flag = False
    def move(self):
        self.touch_buttom = pygame.key.get_pressed()
        if self.touch_buttom[K_UP]:
            self.up = True
            self.left = False
            self.right = False
            self.down = False
        elif self.touch_buttom[K_DOWN]:
            self.up = False
            self.left = False
            self.right = False
            self.down = True
        elif self.touch_buttom[K_LEFT]:
            self.up = False
            self.left = True
            self.right = False
            self.down = False
        elif self.touch_buttom[K_RIGHT]:
            self.up = False
            self.left = False
            self.right = True
            self.down = False
        
        tmp = tuple(self.massive_snake[0])
        if self.up:
            if self.massive_snake[0][1] < 0:
                self.gameover = True
            else:
                # self.rect.center = (self.rect.center[0], self.rect.center[1] - self.speed)
                self.massive_snake[0] = (self.massive_snake[0][0], self.massive_snake[0][1] - self.speed)

        if self.down:
            if self.massive_snake[0][1]  > self.size_of_main_screen[1]:
                self.gameover = True
            else:
                # self.rect.center = (self.rect.center[0], self.rect.center[1] + self.speed)
                self.massive_snake[0] = (self.massive_snake[0][0], self.massive_snake[0][1] + self.speed)

        if self.left:
            if self.massive_snake[0][0]  < 0:
                self.gameover = True
            else:
                # self.rect.center = (self.rect.center[0] - self.speed, self.rect.center[1])
                self.massive_snake[0] = (self.massive_snake[0][0] - self.speed, self.massive_snake[0][1])
        if self.right:
            if self.massive_snake[0][0] > self.size_of_main_screen[0]:
                self.gameover = True
            else:
                # self.rect.center = (self.rect.center[0] + self.speed, self.rect.center[1])
                self.massive_snake[0] = (self.massive_snake[0][0] + self.speed, self.massive_snake[0][1])
        self.rect.center = self.massive_snake[0]
        tmp2 = 0
        if self.flag:
            for i in range(1, len(self.massive_snake)):
                # tmp2 = (self.massive_snake[i])
                # # self.massive_snake[i] = tmp
                
                # if tmp[0] == self.massive_snake[i][0]:
                #     if tmp[1] - self.massive_snake[i][1] > 0:
                #         self.massive_snake[i] = (tmp[i][0], tmp[i - 1][1] - 40)
                #         # self.massive_snake[i] = self.massive_snake[i][0], self.massive_snake[i][1] 
                #         tmp = tuple(tmp2)
                #     else:
                #         self.massive_snake[i] = (tmp[0], tmp[1] + 40)
                #         tmp = tuple(tmp2)
                # else:
                #     if tmp[0] - self.massive_snake[i][0] > 0:
                #         # self.massive_snake[i] = (self.massive_snake[i][0] + 40, self.massive_snake[i - 1][0])
                #         self.massive_snake[i] = (tmp[0] - 40, tmp[1])
                #         tmp = tuple(tmp2)
                #     else:
                #         self.massive_snake[i] = (tmp[0] + 40, tmp[1])
                #         tmp = tuple(tmp2)


                tmp2 = tuple(self.massive_snake[i])
                self.massive_snake[i] = tmp
                tmp = tuple(tmp2)

            
    def paint(self, main_screen):
        self.main_screen = main_screen
        
        # self.main_screen.blit(self.image, self.rect.center)
        for i in self.massive_snake:
            self.main_screen.blit(self.image, i)
        print(len(self.massive_snake))

    def eda(self):
        self.steak = pygame.image.load("steak.png")
        self.image_steak = pygame.transform.scale(self.steak, (40, 40))
        self.rect_steak = self.image_steak.get_rect()
        self.rect_steak.center = (random.randint(20, self.size_of_main_screen[0] - 20), random.randint(20, self.size_of_main_screen[1] - 20))

    def build_eda(self):
        self.main_screen.blit(self.image_steak, self.rect_steak.center)
    def add_part_of_snake(self):
        if self.add_part >= 1:
            self.last_element = self.massive_snake[-1]
            self.massive_snake.append((self.last_element[0], self.last_element[1] + 40))
            self.add_part = 0
            self.flag = True
            
    def collide_with_ourself(self):
        for i in range(1, len(self.massive_snake)):
            self.copy.rect.center = i
            if self.rect.colliderect(self.copy.rect.center):
                self.gameover = True
            
        
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
    some_snake.add_part_of_snake()
    main_screen.fill(pygame.Color("green"))
    some_snake.paint(main_screen)
    pic_coin = point_font.render("Score: " + str(points), True, pygame.Color("blue"))
    pic_level = level_font.render("Level: " + str(level), True, pygame.Color("yellow"))
    main_screen.blit(pic_coin, (some_snake.size_of_main_screen[0] - 95, 18))
    main_screen.blit(pic_level, (some_snake.size_of_main_screen[0] - 79, 45))
    some_snake.move()
    
    if not flag:
        some_snake.build_eda()
    
    if some_snake.gameover:
        main_screen.fill(pygame.Color("red"))
        game_over_font = pygame.font.SysFont("Vergena", 50)
        game_over = game_over_font.render("Ooops, Game over", True, pygame.Color("white"))
        main_screen.blit(game_over, (185, main_screen.get_rect().center[1] - 100))
        score_overall = game_over_font.render("Your score is: " + str(points), True, pygame.Color("white"))
        main_screen.blit(score_overall, (main_screen.get_rect().center[0] - 130, main_screen.get_rect().center[1]))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        exit()

    if some_snake.rect.colliderect(some_snake.rect_steak):
        flag = True
        points += 1
        cnt += 1
        some_snake.add_part += 1
    pygame.display.update()

    FramePerSecond.tick(FPS)

    

