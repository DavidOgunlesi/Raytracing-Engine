import pygame
from pygame.locals import *
from util import Vector2
from typing import Type

class Player:
    def __init__(self, world: list[int], position: Type[Vector2], rotation: float, fov, speed = 0.1, turnSpeed = 5):
        self.world = world
        self.position = position
        self.rotation = rotation
        self.fov = fov
        self.speed = speed
        self.turnSpeed = turnSpeed


    def InputListen(self, event):
        #Keyboard inputs
        keys = pygame.key.get_pressed()
        #Movement
        if keys[pygame.K_w]:
            self.__Move(Vector2(0,self.speed))
            print(self.position)
        if keys[pygame.K_a]:
            self.__Move(Vector2(-self.speed,0))
            print(self.position)
        if keys[pygame.K_s]:
            self.__Move(Vector2(0,-self.speed))
            print(self.position)
        if keys[pygame.K_d]:
            self.__Move(Vector2(self.speed,0))
            print(self.position)
        #Turning
        if keys[pygame.K_LEFT]:
            self.__Rotate(-self.turnSpeed)
            print(self.rotation)
        if keys[pygame.K_RIGHT]:
            self.__Rotate(self.turnSpeed)
            print(self.rotation)

    def __Move(self, MovementVector: Type[Vector2]):
        yDir = self.position.y + MovementVector.y
        xDir = self.position.x + MovementVector.x
        #out of bounds
        if(len(self.world) <= yDir or yDir < 0 or len(self.world[0]) <= xDir or xDir < 0 ):
            print(len(self.world) >= yDir, yDir < 0, len(self.world[0]) >= xDir, xDir < 0 )
            return
        #Validation-stop player from walking through walls
        if (self.world[int(yDir)][int(xDir)]==0):
            self.position.x = xDir
            self.position.y = yDir

    def __Rotate(self, direction):
        self.rotation += direction
        #Validation
        #keep rotation within 0-359 circle angle range
        if (self.rotation > 359):
            self.rotation = 0
        if (self.rotation < 0):
            self.rotation = 359
