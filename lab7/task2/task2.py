import pygame
import os
import time

pygame.init()
screen = pygame.display.set_mode()


path = "C:\\Users\\Akken\\Desktop\\labs\\lab7\\task2\\musics\\"
picture = pygame.image.load("Снимок.PNG")
list_of_music = os.listdir(path)
picture = pygame.transform.scale(picture, screen.get_rect().size)
screen.blit(picture, (0, 0))
# print(list_of_music)
pygame.display.update()
current = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_p]:
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