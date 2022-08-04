class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print(str(self.area()) + " - площадь этого треугольника")

    def area(self):
        p = (self.a + self.b + self.c) / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s


triangle1 = Triangle(5, 6, 7)
