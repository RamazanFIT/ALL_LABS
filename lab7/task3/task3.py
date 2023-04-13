import pygame



pygame.init()
screen_1 = pygame.display.set_mode((700, 700))
image = pygame.image.load("background.png")
image = pygame.transform.scale(image, screen_1.get_rect().size)
clock = pygame.time.Clock()
x = 25
y = 25
FPS = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen_1.blit(image, (0, 0))
    bolean = True
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and y >= 45:
        y -= 20
    elif key[pygame.K_DOWN] and y <= 665:
        y += 20
    elif key[pygame.K_LEFT] and x >= 45:
        x -= 20
    elif key[pygame.K_RIGHT] and x <= 665:
        x += 20
    
    
    if bolean:
        red_ball = pygame.draw.circle(screen_1, pygame.Color('red'), (x, y), 25)
    
    pygame.display.update()
    clock.tick(FPS)

