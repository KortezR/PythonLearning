import math


class Circle:
    def __init__(self, r):
        self.r = r
        print(str(self.area()) + " - площадь данного круга")

    def area(self):
        return self.r ** 2 * math.pi


circle1 = Circle(5)
