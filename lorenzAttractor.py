import pygame
import os
from matrix import *
import math
import colorsys


os.environ["SDL_VIDEO_CENTERED"]='1'
#set desired resolution
width, height = 960, 540
size = (width, height)
white, black = (200, 200, 200), (0, 0, 0)
pygame.init()
pygame.display.set_caption("Lorenz Attractor")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#set fps 
fps = 60

sigma = 10
row = 28
beta = 8/3
x, y, z = 0.01, 0, 0
points = []
colors = []
scale = 6
angle = 0
previous = None

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
can_draw = False
run = True
while run:
    screen.fill(black)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    xRotation = [[1, 0, 0],
                  [0, math.cos(angle), -math.sin(angle)],
                  [0, math.sin(angle), math.cos(angle)]]

    yRotation = [[math.cos(angle), 0, -math.sin(angle)],
                  [0, 1, 0],
                  [math.sin(angle), 0, math.cos(angle)]]

    zRotation =[[math.cos(angle), -math.sin(angle), 0],
                 [math.sin(angle), math.cos(angle), 0 ],
                  [0, 0, 1]]
#maths equation for lorenz attractor
    time = 0.01
    dx = (sigma * (y - x))*time
    dy = (x * (row - z) - y)*time
    dz = (x * y - beta * z)*time

    x = x + dx
    y = y + dy
    z = z + dz
    hue = 0

    point = [[x], [y], [z]]
    points.append(point)
    for p in range(len(points)):

        rotated_2d = matrix_multiplication(yRotation, points[p])
        distance = 5

        val = 1/(distance - rotated_2d[2][0]) #z value
        projection_matrix = [[1, 0, 0],
                             [0, 1, 0]]

        projected2d = matrix_multiplication(projection_matrix, rotated_2d)
        x_pos = int(projected2d[0][0] * scale) + width//2 + 100
        y_pos = int(projected2d[1][0] * scale) + height//2
        if hue > 1:
            hue = 0
        if previous is not None:
            if hue >  0.006:
                pygame.draw.line(screen, (hsv2rgb(hue, 1, 1)), (x_pos, y_pos), previous, 4 )


        previous = (x_pos, y_pos)
        hue +=0.006


    angle += 0.01

    pygame.display.update()
pygame.quit()
