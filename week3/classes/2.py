class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0


shape = Shape()
print(shape.area())

square = Square(3)
print(square.area())
