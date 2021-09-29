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
[1,0,0,0,0,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1]
]

pygame.init()
screenDimensions = Vector2(1280, 720)
window = pygame.display.set_mode((screenDimensions.x, screenDimensions.y))
player = Player(world,Vector2(3,3),0,0)
lookAngle = 45;
#print(Vector2(math.cos(angle*math.pi/180),math.sin(angle*math.pi/180)))
#print(ray.Raycast(world, player.position, , 20))
#sys.exit()
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

    #create ray ray samples
    samples = ray.RenderViewSamples(world,pygame.display.get_surface().get_width(), player.position, player.rotation+10, 20)
    print("fired ",len(samples)," rays")
    i = 0;
    for raySample in samples:
        #u = x / (20 - 1)
        color = (round(255/raySample.currDist), 0, round(255/raySample.currDist))
        #rect.top:rect.bottom
        height = pygame.display.get_surface().get_height()
        distSize = height/raySample.currDist
        #print(raySample.currDist)
        upper = int(height/2 + distSize/2)
        lower = int(height/2 - distSize/2)
        pixel_array[i,upper:lower] = color
        i+=1

    pixel_array.close()
    pygame.display.flip()

pygame.quit()
exit()
