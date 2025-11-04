from abc import ABC,abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class bike(vehicle):
    def start(self):
        print("Bike Started")

class car(vehicle):
    def start(self):
        print("Car started")

Car = car()
Car.start()