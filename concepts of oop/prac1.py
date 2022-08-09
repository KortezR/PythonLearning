class Rectangle:
    def __init__(self, a, b):
        self.b = b
        self.a = a

    def calculate_perimeter(self):
        return 2*self.a*self.b


class Square:
    def __init__(self, a):
        self.a = a

    def calculate_perimeter(self):
        return 4*self.a


rec = Rectangle(2, 4)
squ = Square(5)
print(rec.calculate_perimeter())
print(squ.calculate_perimeter())
