class Parent:
    def __init__(self):
        print("Parent constructor")

    def show(self):
        print("Parent class method")

class Child(Parent):
    def __init__(self):
        super().__init__()  # calls parent constructor
    
    def display(self):
        super().show()

obj = Child()
obj.display()