class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def circumference(self):
        return 2 * 3.14 * self.radius
class Cube(Square):
    def area(self):
        return 6 * self.side ** 2
    def volume(self):
        return self.side ** 3
rectangle = Rectangle(5, 10)
square = Square(5)
circle = Circle(5)
cube = Cube(5)
print(rectangle.area())
print(square.area())
print(circle.area())
print(circle.circumference())
print(cube.area())
print(cube.volume())
