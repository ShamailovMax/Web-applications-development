from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math as m            


class Circle(Figure):

    FTYPE = "Круг"

    def __init__(self, color, radius):
        self.radius = radius
        self.fcolor = FigureColor()
        self.fcolor.color_property = color

    def _area(self):
        return m.pi * (self.radius ** 2)

    def __repr__(self):
        return f'{Circle.get_ftype()} {self.fcolor.color_property} цвета, радиусом {self.radius} и площадью {self._area()}'