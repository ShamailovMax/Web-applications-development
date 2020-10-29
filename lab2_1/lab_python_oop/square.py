from lab_python_oop.rectungle import Rectangle


class Square(Rectangle):

    FTYPE = "Квадрат"

    def __init__(self, color, side):
        self._side = side
        super().__init__(color, self._side, self._side)

    def __repr__(self):
        return f'{Square.get_ftype()} {self._fcolor.color_property} цвета со стороной {self._side} площадью {self._area()}.'