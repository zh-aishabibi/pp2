import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x1 = float(input("Enter x-coordinate for point 1: "))
y1 = float(input("Enter y-coordinate for point 1: "))
x2 = float(input("Enter x-coordinate for point 2: "))
y2 = float(input("Enter y-coordinate for point 2: "))

point1 = Point(x1, y1)
point2 = Point(x2, y2)

point1.show()
point2.show()

dx = float(input("Enter the change in x for point 1: "))
dy = float(input("Enter the change in y for point 1: "))
point1.move(dx, dy)
point1.show()

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")
