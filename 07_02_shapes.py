'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.area = (3.14 * self.radius * self.radius)
        return f'The area of a circle with a radius of {self.radius} is {self.area}.'

    def circumference(self):
        self.circumference = (self.radius * 3.14 * 2)
        return f'The circumference of a circle with a radius of {self.radius} is {self.circumference}.'

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.area = (self.length * self.width)
        return f'The area of a rectangle with a length of {self.length} and a width of {self.width} is {self.area}.'

    def perimeter(self):
        self.perimeter = (self.length + self.length + self.width + self.width)
        return f'The perimeter of a rectangle with a length of {self.length} and a width of {self.width} is {self.perimeter}.'


rect1 = Rectangle(5,10)
circ1 = Circle(6)

print(circ1.area())
print(circ1.circumference())
print(rect1.perimeter())
print(rect1.area())