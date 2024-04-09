from math import sqrt
class Shapes:
  def __init__(self, name):
    self.name = name

# Derived classes
class Circle(Shapes):
  pi = 3.14
  def __init__(self, name, radius):
    super().__init__(name)
    self.radius = radius
    print("Calculate Circle\n")
  def area(self):
    print(f'{self.name} area is: {((self.radius**2)*Circle.pi):,.2f}')
  def perimeter(self):
    print(f'{self.name} perimeter is: {(self.radius*2):,.2f}')
    print("----------------------")

class Rectangle(Shapes):
  def __init__(self, name, height, width):
    super().__init__(name)
    self.height = height
    self.width = width
    print("Calculate Rectangle\n")

  def area(self):
    print(f'{self.name} area is: {(self.height*self.width):,.2f}')
  def perimeter(self):
    print(f'{self.name} perimeter is: {((self.height + self.width) * 2):,.2f}')
    print("----------------------")

class Triangle(Shapes):
  
  def __init__(self, name, sidea, sideb, sidec):
    super().__init__(name)
    self.sidea = sidea
    self.sideb = sideb
    self.sidec = sidec
    self.s = (self.sidea + self.sideb + self.sidec) / 2
    print("Calculate Triangle\n")
  
  def area(self):
    print(f'{self.name} area is: {(sqrt(self.s * (self.s - self.sidea) * (self.s - self.sideb) * (self.s - self.sidec))):,.2f}')
  def perimeter(self):
    print(f'{self.name} perimeter is: {(self.s * 2):,.2f}')
    print("----------------------")


# create objects
circle1 = Circle("Circle", 2)
circle1.area()
circle1.perimeter()

rect1 = Rectangle("Rectangle", 2, 4)
rect1.area()
rect1.perimeter()

triangle1 = Triangle("Triangle", 4, 4, 4)
triangle1.area()
triangle1.perimeter()