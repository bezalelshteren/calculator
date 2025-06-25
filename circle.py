import math
from shaipe import shape


class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        area =  math.pi * (self.radius ** 2)
        return area

    def calculate_scope(self):
        scope = 2 * math.pi * self.radius
        return scope

