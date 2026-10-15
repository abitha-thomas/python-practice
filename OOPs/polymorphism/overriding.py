class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("child class method")

obj = Child()  
obj.show()      