from Rectangle import rectangle
from Square import square
from circle import circle
from triangle import Triangle
from shaipe import shape



class calculator:
    def __init__(self,shape):
        self.list_of_shape = {}
        self.shape = shape
        self.type_shape = self.shape.__class__.__name__
        self.add_shape_to_list()


    def calculate(self):
        print(self.shape)


    def add_shape_to_list(self):

        if self.type_shape in self.list_of_shape:
            self.list_of_shape[self.type_shape] = []
            self.list_of_shape[self.type_shape].append(self.shape)
        else:
            self.list_of_shape[self.type_shape] = self.shape

    def get_the_shape(self):
        for i in self.list_of_shape:
            print(i)



triangle = Triangle(5,6)
rectangle2 = rectangle(2,5)
rectangle1 = rectangle(8,7)
square = square(5)
circle = circle(8)
calculator1 = calculator(rectangle2)
calculator1 = calculator(rectangle1)
calculator1 = calculator(circle)
calculator1 = calculator(square)
calculator.calculate()
calculator.get_the_shape()