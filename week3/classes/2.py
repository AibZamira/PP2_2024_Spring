class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


shape = Shape()
print(f"Shap's area: {shape.area()}")

square = Square(int(input("Length: ")))
print(f"Square's area: {square.area()}")
