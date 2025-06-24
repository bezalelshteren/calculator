from abc import ABC, abstractmethod

class shaipe(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_scope(self):
        pass