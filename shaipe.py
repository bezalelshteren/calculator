from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_scope(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}{self.calculate_area()}{self.calculate_scope()}"
