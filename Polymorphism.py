"""Problem 10 — Polymorphism (medium)
Create three classes Circle, Rectangle, Triangle — each with an area() method. 
Write a function print_areas(shapes) that takes a list of any mix of these objects and prints each area. 
Same function, different behaviour per object."""

class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return(3.14*self.r*self.r)
class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return(self.l*self.b)
class Triangle:
    def __init__(self,l,b):
          self.l=l
          self.b=b
    def area(self):
        return(0.5*self.l*self.b)
def print_area(shapes):
    for shape in shapes:
        print(f"Area:{shape.area()}")

shapes=[Circle(5),Rectangle(4,4),Triangle(3,4)]
print_area(shapes)