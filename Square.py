from shaipe import shape


class square(shape):
    def __init__(self,length):
        self.length = length

    def calculate_area(self):
        return self.length * self.length

    def calculate_scope(self):
        return self.length * 4
