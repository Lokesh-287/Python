def add(a, b, c=0):
    return a + b + c

print(add(2, 3))
print(add(2, 3, 4))
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area = πr²")

class Rectangle(Shape):
    def area(self):
        print("Area = l × b")

shapes = [Circle(), Rectangle()]
for s in shapes:
    s.area()
