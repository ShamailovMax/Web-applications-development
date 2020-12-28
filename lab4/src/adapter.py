# Структурный паттерн Adapter


class Old:
    def get(self):
        return "1234"


class New:
    def get_integer_type(self):
        return 456


class Adapter(New):

    """
    Создал сам паттерн 
    (в качестве первого взял простейший адаптер)
    """

    def get(self):
        return str(self.get_integer_type())


def main(obj):
    print("Результат: " + obj.get())


if __name__ == '__main__':
    obj = Adapter()
    main(obj)