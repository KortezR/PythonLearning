class Hexagon:
    def __init__(self, a):
        self.a = a
        print(str(self.calculate_perimeter()) + " - периметр данного правильного шестиугольника")

    def calculate_perimeter(self):
        return 6*self.a


hexagon1 = Hexagon(6)
