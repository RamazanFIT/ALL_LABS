import pygame
import os
import time
import random

pygame.init()
display = pygame.display.set_mode((700, 700))
image = pygame.image.load("apple.jpg")
image = pygame.transform.scale(image, display.get_rect().size)

display.blit(image, (0, 0))
pygame.display.update()
path = "musics\\"

list_of_music = os.listdir(path)
print(list_of_music)
current = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_p]:
        current = random.randint(0, len(list_of_music) - 1)
        pygame.mixer.music.load(path + list_of_music[current])
        pygame.mixer.music.play(1)
        
    elif key[pygame.K_SPACE]:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
      
    elif key[pygame.K_n]:
        if current == len(list_of_music) - 1:
            current = 0
        else:
            current += 1
        pygame.mixer.music.load(path + list_of_music[current])
        pygame.mixer.music.play(1)
       
    elif key[pygame.K_b]:
        if(current == 0):
            current = len(list_of_music) - 1
        else:
            current -= 1
        pygame.mixer.music.load(path + list_of_music[current])
        pygame.mixer.music.play(1)
    time.sleep(0.1)