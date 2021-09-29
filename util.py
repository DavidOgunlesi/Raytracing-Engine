import math
from typing import Type

class Vector2:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def __mul__(self, other:int):
        return Vector2(self.x*other, self.y*other)

    def __sub__(self, other):
        return Vector2(self.x-other.x, self.y-other.y)

    def __rmul__(self, other:int):
        return Vector2(self.x*other, self.y*other)

    def __str__(self):
         return "[{}, {}]".format(self.x, self.y)

    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def rotate(self, angle:float):
        rad = angle*math.pi/180
        x = self.x*math.cos(rad)*-math.sin(rad)
        y = self.y*math.sin(rad)*-math.cos(rad)
        return Vector2(x, y)

sign = lambda x: math.copysign(1, x)

def normalise(vector2: Type[Vector2]) -> Vector2:
    length = math.sqrt(vector2.x**2 + vector2.y**2)
    if length == 0:
        print("Error! Trying to normalise a 0 length vector!")
        return Vector2(0,0)
    return Vector2(vector2.x/length,vector2.y/length)
