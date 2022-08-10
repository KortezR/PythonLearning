class Shape:
    def what_am_i(self):
        print("Я - фигура")


class Rectangle(Shape):
    def __init__(self, a, b):
        self.b = b
        self.a = a

    def calculate_perimeter(self):
        return 2 * self.a * self.b


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def change_size(self, number):
        self.a += number

    def calculate_perimeter(self):
        return 4 * self.a


rec = Rectangle(2, 4)
squ = Square(5)
print(rec.calculate_perimeter())
print(squ.calculate_perimeter())
rec.what_am_i()
squ.what_am_i()

