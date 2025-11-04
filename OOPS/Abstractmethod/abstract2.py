from abc import ABC,abstractmethod

class Shape(ABC):

    def display(self):
        print("it is a shape")

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,wight):
        self.length=length
        self.wight=wight

    def area(self):
        return self.length*self.wight
    def perimeter(self):
        return self.length+self.wight

r =Rectangle(5,3)
print("Area : ",r.area())
print("Perimeter : ",r.perimeter())
r.display()