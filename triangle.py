from shaipe import shape
import math

class Triangle(shape):
    def __init__(self,high,base):
        self.high = high
        self.base = base

    def calculate_area(self):
        return self.base * self.high / 2

    def calculate_scope(self):
        side = math.sqrt((self.base/2) ** 2 + self.high ** 2)
        scope = self.base + 2 * side
        return scope