class Shape:
    def __init__(self):
        self.area_value = 0

    def area(self):
        print(f"Area of the shape: {self.area_value}")


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.area_value = self.length ** 2

    def area(self):
        print(f"Area of the square: {self.area_value}")


shape = Shape()
shape.area()

square = Square(5)
square.area()
