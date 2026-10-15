class Student:
    def __init__(self,name,age):
        self.name= name
        self.age=age

    def display(self):
        print("Name:",self.name,"Age:",self.age)  

s1 = Student("Jenish", 21)
s2 = Student("Rahul", 20)

s1.display()
s2.display() 



