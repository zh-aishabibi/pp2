class Shape:
    def __init__(self):
        self.area_value = 0

    def area(self):
        print(f"Area of the shape: {self.area_value}")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area_value = self.length * self.width

    def area(self):
        print(f"Area of the rectangle: {self.area_value}")


shape = Shape()
shape.area()

a =input("length: ")
b = input ("width: ")

rectangle = Rectangle(int(a),int(b))
rectangle.area()
