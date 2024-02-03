class Point:
    def __init__(self):
        pass

    def show(self):
        self.p1 = int(input())
        self.p2 = int(input())

    def move(self):
        self.p1, self.p2 = self.p2, self.p1

    def dist(self):
        self.sum = self.p1**2 + self.p2**2
        return self.sum**0.5

point = Point()
point.show()
point.move()
print(point.dist())
