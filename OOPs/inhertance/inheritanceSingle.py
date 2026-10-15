class Parent:
    def displayA(self):
        print("Parent class")

class Child(Parent):
    def displayB(self):
        print("child class")  


obj = Child()
obj.displayA()
obj.displayB()    
