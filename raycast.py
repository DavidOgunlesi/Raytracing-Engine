from typing import Type
from util import Vector2, sign, normalise
import math
from math import floor, ceil, sqrt

def RenderViewSamples(world, screenWidth: int, position: Type[Vector2], lookAngle: Type[Vector2], maxDist: int):
    planeDist = 5
    planeVector = (position + Vector2(0, planeDist)).rotate(lookAngle)
    leftPlane = planeVector+Vector2(-screenWidth, 0).rotate(lookAngle)
    rightPlane = planeVector+Vector2(screenWidth, 0).rotate(lookAngle)
    sampleVector = rightPlane-leftPlane
    #sample points on screen along camera plane vector
    raySamples = []
    for i in range(1,screenWidth):
        currPoint = (sampleVector/screenWidth)*i
        #currPoint = planeVector+Vector2(-screenWidth+i, 0).rotate(lookAngle)
        #cast rays at sample points
        #lookAngleRad = lookAngle*math.pi/180
        NCurrPoint = normalise(currPoint)
        #v = Vector2(math.cos(lookAngle*math.pi/180),math.sin(lookAngle*math.pi/180))
        print(90-math.atan2(NCurrPoint.x, NCurrPoint.y)*180/math.pi)
        #print(currPoint, normalise(currPoint))
        #direction = normalise(Vector2(math.cos(lookAngleRad),math.sin(lookAngleRad)))
        ray = Raycast(world, position, normalise(currPoint), maxDist)
        raySamples.append(ray)
        #.GetCollisionPointPercentage(ray.collisionPoint)
    return raySamples


"""
Create a Ray
"""
def Raycast(world, startPos: Type[Vector2], direction: Type[Vector2], maxDist: int):
    #for i in range(0, screenWidth):
    #print("start pos", startPos)
    #print("direction", direction)
    #print("maxDist", maxDist)
    ray = Ray(world, startPos, direction, maxDist)
    ray.Propagate(True)
    return ray

class Ray:

    def __init__(self, world, startPos: Type[Vector2], direction: Type[Vector2], maxDist: int):
        self.world = world
        self.direction = direction
        self.maxDist = maxDist
        self.currX = startPos.x
        self.currY = startPos.y
        self.currDist = 0
        self.visitedCells = []
        self.collisionPoint = Vector2()

    def Propagate(self, isFirst = False, stepSize = 1, initialXStep = 0, initialYStep = 0):
        # Step ray forward using DDA algorithm to ensure accurate intersections
        # https://www.youtube.com/watch?v=NbSee-XM7WA
        if isFirst:
            stepX = self.currX-floor(self.currX)
            stepY = 1-(self.currY-floor(self.currY))
            if stepX == 0:
                stepX = 1
            if stepY == 0:
                stepY = 1
            initialXStep += self.__xRayLength(stepX, self.direction)
            initialYStep += self.__yRayLength(stepY, self.direction)
            #print("stepX", stepX)
            #print("stepY", stepY)
        else:
            initialXStep += self.__xRayLength(stepSize, self.direction)
            initialYStep += self.__yRayLength(stepSize, self.direction)

        currentXStep = initialXStep
        currentYStep = initialYStep
        if initialXStep >= initialYStep:
            #print("xStepBigger")
            # step in y until y is greater than x
            while (currentYStep <= initialXStep):
                currentYStep += self.__yRayLength(stepSize, self.direction)
                self.currDist+=currentYStep
                # mark visited cell
                self.currY += sign(self.direction.y)
                pos = Vector2(self.currX,self.currY)
                #print(pos)
                self.visitedCells.append(pos)
        else:
            #print("yStepBigger")
            # step in x until x is greater than y
            while (currentXStep < initialYStep):
                currentXStep += self.__xRayLength(stepSize, self.direction)
                self.currDist+=currentXStep
                # mark visited cell
                self.currX += sign(self.direction.x)
                pos = Vector2(self.currX,self.currY)
                #print(pos)
                self.visitedCells.append(pos)

        #print(self.currDist)
        # Repeat again unless collided with wall or reached max distance

        if self.currDist <= self.maxDist and (len(self.world)>int(round(self.currY)) and len(self.world[0])>int(round(self.currX))) and (self.world[int(round(self.currY))][int(round(self.currX))]==0):
            #print("continuing ray")
            self.Propagate(False, 1,currentXStep,currentYStep)
        else:
            self.collisionPoint = Vector2(self.currX,self.currY)
            #print(self.direction, "hit", self.collisionPoint)

    def __xRayLength(self, stepSize, gradient: Type[Vector2]):
        if gradient.x==0:
            return gradient.y
        return sqrt(stepSize+(gradient.y/gradient.x)**2)

    def __yRayLength(self, stepSize, gradient: Type[Vector2]):
        if gradient.y==0:
            return gradient.x
        return sqrt(stepSize+(gradient.x/gradient.y)**2)

    def GetCollisionPointPercentage(self, point: Type[Vector2]) -> Vector2:
        if point.x == None or point.y == None:
            return None
        return Vector2((self.currX-floor(self.currX))*100, (self.currY-floor(self.currY))*100)
