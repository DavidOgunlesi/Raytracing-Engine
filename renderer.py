import pygame
import sys
from player import Player
from util import Vector2, normalise
import raycast as ray
import math
world = [
[1,1,1,1,1,1,1],
[1,0,0,0,0,0,1],
[1,0,0,0,0,0,1],
[1,0,0,0,0,0,1],
[1,0,0,0,1,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1]
]

pygame.init()
window = pygame.display.set_mode((1280, 720))
player = Player(world,Vector2(3,3),0,0)
angle = 45;
print(Vector2(math.cos(angle*math.pi/180),math.sin(angle*math.pi/180)))
print(ray.Raycast(world, player.position, normalise(Vector2(math.cos(angle*math.pi/180),math.sin(angle*math.pi/180))), 20))
sys.exit()
run = True
while run:
    #Cycles through all the events currently occuring
    for event in pygame.event.get():
        player.InputListen(event)
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)

    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size())//2]*2))

    pixel_array = pygame.PixelArray(window)

    for x in range(20):
        u = x / (20 - 1)
        color = (round(u*255), 0, round((1-u)*255))
        pixel_array[rect.left + x, rect.top:rect.bottom] = color

    pixel_array.close()

    pygame.display.flip()

pygame.quit()
exit()
