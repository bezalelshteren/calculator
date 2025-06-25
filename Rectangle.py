from Square import square
from shaipe import shape


class rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_scope(self):
        return self.length * 2 + self.width * 2

