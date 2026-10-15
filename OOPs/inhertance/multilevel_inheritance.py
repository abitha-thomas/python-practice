class Grandparent:
    def property(self):
        print("Grandparent property")

class Parent(Grandparent):
    def money(self):
        print("parent money")        

class Child(Parent):   
    def car(self):
        print("Child car")    

obj = Child()
obj.property()
obj.money()
obj.car()
