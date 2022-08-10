class Horse:
    def __init__(self, color, owner):
        self.color = color
        self.owner = owner


class Rider:
    def __init__(self, name):
        self.name = name


rid = Rider("John")
hor = Horse("Brown", rid)
print(hor.owner.name)
