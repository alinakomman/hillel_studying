from abc import ABC, abstractmethod
import math


class Figures(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Triangle(Figures):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    def get_square(self):
        s = (self._a + self._b + self._c) / 2
        square = math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))
        return square

    def get_perimeter(self):
        perimeter = self._a + self._b + self._c
        return perimeter


class Round(Figures):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def get_square(self):
        square = math.pi * self._radius ** 2
        return square

    def get_perimeter(self):
        perimeter = 2 * math.pi * self._radius
        return perimeter


figures = [Triangle(3, 4, 5), Round(6)]

total_perimeter = 0
total_square = 0

for figure in figures:
    total_perimeter += figure.get_perimeter()
    total_square += figure.get_square()

print(f"Total perimeter of all figures: {total_perimeter}")
print(f"Total square of all figures: {total_square}")
