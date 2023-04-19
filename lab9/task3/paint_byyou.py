import pygame
from pygame.locals import *
import time
import math

pygame.init()

clock = pygame.time.Clock()

def draw_right_triangle(x_up, y_up, x_down, y_down, main_screen, color, size):
    a = x_down - x_up
    b = a / 2
    h = b * math.sqrt(3)
    x_pos = x_down - b
    y_pos = y_down - h
    pygame.draw.line(main_screen, color, (x_down, y_down), (x_pos, y_pos), size)
    pygame.draw.line(main_screen, color, (x_up, y_down), (x_pos, y_pos), size)
    pygame.draw.line(main_screen, color, (x_up, y_down), (x_down, y_down), size)
    
def draw_equilateral_triangle(x_up, y_up, x_down, y_down, main_screen, color, size):
    h = y_down - y_up
    a = x_down - x_up
    b = a / 2
    x_pos = x_up + b
    y_pos = y_up
    pygame.draw.line(main_screen, color, (x_down, y_down), (x_pos, y_pos), size)
    pygame.draw.line(main_screen, color, (x_up, y_down), (x_pos, y_pos), size)
    pygame.draw.line(main_screen, color, (x_up, y_down), (x_down, y_down), size)

def draw_rhombus(x_up, y_up, x_down, y_down, main_screen, color, size):
    b = (x_down - x_up) / 2
    a = (y_down - y_up) / 2

    x1_pos = x_up + b
    y1_pos = y_up

    x2_pos = x_down
    y2_pos = y_down - a

    x3_pos = x_down - b
    y3_pos = y_down

    x4_pos = x_up
    y4_pos = y_up + a

    pygame.draw.line(main_screen, color, (x1_pos, y1_pos), (x2_pos, y2_pos), size)
    pygame.draw.line(main_screen, color, (x2_pos, y2_pos), (x3_pos, y3_pos), size)
    pygame.draw.line(main_screen, color, (x3_pos, y3_pos), (x4_pos, y4_pos), size)
    pygame.draw.line(main_screen, color, (x4_pos, y4_pos), (x1_pos, y1_pos), size)

def dwar_two_point(point_1, point_2, radius, main_screen, color):
    dx = abs(point_2[0] - point_1[0])
    dy = abs(point_1[1] - point_2[1])
    for i in range(0, max(dx, dy)):
        procent = i / max(dy, dx)
        x = point_1[0] + (point_2[0] - point_1[0]) * procent 
        y = point_1[1] + (point_2[1] - point_1[1]) * procent
        pygame.draw.circle(main_screen, color, (x, y), radius)

color = pygame.Color("black")
size_rect = 1
flag_some = False
flag_some_second = False
flag_some_third = False
flag_some_fourth = False
circuit_var_flag = False
def main():

    radius = 4
    flag_circle = False
    main_screen = pygame.display.set_mode((700, 700))
    main_screen.fill("white")
    points_list = []
    image = pygame.image.load("back.jpg")
    image = pygame.transform.scale(image, (main_screen.get_rect().size[0] // 4, main_screen.get_rect().size[1] // 6))
    main_screen.blit(image, (0, 0))
    flag = False
    right_triangle = False
    equilateral_triangle = False
    rhombus = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        mouse_press = pygame.mouse.get_pressed()
        keyboard = pygame.key.get_pressed()
        coord_mouse = pygame.mouse.get_pos()
        if keyboard[K_r]:
            global color
            color = pygame.Color("red")
            points_list = list()
        elif keyboard[K_e]:
            color = "white"
            points_list = list()
        elif keyboard[K_k]:
            flag = True
        elif keyboard[K_c]:
            flag_circle = True
        elif keyboard[K_b]:
            color = "black"
        elif keyboard[K_y]:
            color = "yellow"
        elif keyboard[K_o]:
            color = "orange"
        elif keyboard[K_p]:
            color = pygame.Color("purple")
        elif keyboard[K_v]:
            color = "violet"
        elif keyboard[K_1]:
            right_triangle = True
        elif keyboard[K_2]:
            equilateral_triangle = True
        elif keyboard[K_3]:
            rhombus = True
        if flag:
            global size_rect
            if keyboard[K_LSHIFT]:
                size_rect += 1
            elif keyboard[K_LCTRL]:
                size_rect = max(1, size_rect - 1)
            global flag_some
            if color == "white":
                color = "black"
            if mouse_press[0]:
                flag_some = True
                points_list.append(coord_mouse)
            if flag_some and not mouse_press[0] and len(points_list) >= 2:
                flag = False
                v1 = points_list[0]
                v2 = points_list[-1]
                # some_rect = pygame.Rect(points_list[0], ((points_list[-1][0] - points_list[0][0]), (points_list[-1][1] - points_list[0][1])))
                size_rect = max(1, radius // 4)
                some_rect = pygame.Rect(min(v1[0], v2[0]), min(v1[1], v2[1]), abs(v1[0] - v2[0]), abs(v1[1] - v2[1]))
                pygame.draw.rect(main_screen, color, some_rect, size_rect)
                points_list = list()
        elif flag_circle:
            
            global circuit_var_flag
            if color == "white":
                color = "black"
            if mouse_press[0]:
                circuit_var_flag = True
                points_list.append(coord_mouse)
            if len(points_list) >= 2:
                
                j1 = points_list[0]
                j2 = points_list[-1]
                size_of_circuit = max(1, radius // 4)
                
            if circuit_var_flag and not mouse_press[0] and len(points_list) >= 2:
                flag_circle = False
                
                j1 = points_list[0]
                j2 = points_list[-1]
                size_of_circuit = max(1, radius // 4)
                pygame.draw.circle(main_screen, color, (min(j1[0], j2[0]) + abs(j1[0] - j2[0]) / 2,
                min(j1[1], j2[1]) + abs(j1[1] - j2[1]) / 2), max(abs(j1[1] - j2[1]), abs(j1[0] - j2[0])) / 2, size_of_circuit)
                points_list = list()
                
        elif right_triangle:
            
            global flag_some_second 
            if color == "white":
                color = "black"
            if mouse_press[0]:
                flag_some_second = True
                points_list.append(coord_mouse)
            if flag_some_second and not mouse_press[0] and len(points_list) >= 2:
                right_triangle = False
                v1 = points_list[0]
                v2 = points_list[-1]
                
                size_triangle = max(1, radius // 4)
                draw_right_triangle(min(v1[0], v2[0]), min(v1[1], v2[1]), max(v1[0], v2[0]), max(v1[1], v2[1]), main_screen, color, size_triangle)
              
                points_list = list()
        elif equilateral_triangle:
            global flag_some_third
            if color == "white":
                color = "black"
            if mouse_press[0]:
                flag_some_third = True
                points_list.append(coord_mouse)
            if flag_some_third and not mouse_press[0] and len(points_list) >= 2:
                equilateral_triangle = False
                v1 = points_list[0]
                v2 = points_list[-1]
                
                size_triangle = max(1, radius // 4)
                draw_equilateral_triangle(min(v1[0], v2[0]), min(v1[1], v2[1]), max(v1[0], v2[0]), max(v1[1], v2[1]), main_screen, color, size_triangle)
              
                points_list = list()
        elif rhombus:
            global flag_some_fourth
            if color == "white":
                color = "black"
            if mouse_press[0]:
                flag_some_fourth = True
                points_list.append(coord_mouse)
            if flag_some_fourth and not mouse_press[0] and len(points_list) >= 2:
                rhombus = False
                v1 = points_list[0]
                v2 = points_list[-1]
                
                size_rhombus = max(1, radius // 4)
                draw_rhombus(min(v1[0], v2[0]), min(v1[1], v2[1]), max(v1[0], v2[0]), max(v1[1], v2[1]), main_screen, color, size_rhombus)
              
                points_list = list()

        else:
            if keyboard[K_UP]:
                radius += 1
            elif keyboard[K_DOWN]:
                radius = max(1, radius - 1)
            if not mouse_press[0]:
                points_list = list()
            if coord_mouse != (0, 0) and mouse_press[0]:
                points_list.append(pygame.mouse.get_pos())
                # points_list = points_list[-240:]
            
            for i in range(len(points_list) - 1):
                dwar_two_point(points_list[i], points_list[i + 1], radius, main_screen, color)
                
        
        pygame.display.update()
        clock.tick(60)
      
main()

