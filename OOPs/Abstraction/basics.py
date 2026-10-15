from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")


class Bike(Vehicle):
    def start(self):
        print("Bike Started")        

    def stop(self):
        print("Bike Started")    

c = Car()    
b = Bike()
c.start()
b.start()
b.stop()    