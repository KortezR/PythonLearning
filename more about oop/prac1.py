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
    square_list = []

    def __init__(self, a):
        self.a = a
        Square.square_list.append(self)

    def __repr__(self):
        return str(self.a) + " на " + str(self.a) + " на " + str(self.a) + " на " + str(self.a)

    def change_size(self, number):
        self.a += number

    def calculate_perimeter(self):
        return 4 * self.a

def is_the_same(a, b):
    return a is b


rec = Rectangle(2, 4)
squ = Square(5)
squ2 = squ
squ3 = Square(3)
print(rec.calculate_perimeter())
print(squ.calculate_perimeter())
rec.what_am_i()
squ.what_am_i()
print(Square.square_list)
print(squ)
print(is_the_same(rec, squ))
print(is_the_same(squ, squ2))
print(is_the_same(squ, squ3))

