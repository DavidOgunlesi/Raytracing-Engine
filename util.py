import math
from typing import Type

class Vector2:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def __str__(self):
         return "[{}, {}]".format(self.x,self.y)

sign = lambda x: math.copysign(1, x)

def normalise(vector2: Type[Vector2]) -> Vector2:
    length = math.sqrt(vector2.x**2 + vector2.y**2)
    return Vector2(vector2.x/length,vector2.y/length)
