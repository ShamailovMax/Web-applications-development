from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):

    FTYPE = "Прямоугольник"

    def __init__(
        self, 
        color, 
        width, 
        height
    ):
        self._width = width
        self._height = height
        self._fcolor = FigureColor()
        self._fcolor.color_property = color

    def _area(self):
        return self._width * self._height

    def __repr__(self):
        return f'{Rectangle.get_ftype()} {self._fcolor.color_property} цвета шириной {self._width}, высотой {self._height} и площадью {self._area()}.'