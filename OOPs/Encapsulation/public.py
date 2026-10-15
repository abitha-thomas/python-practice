class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Duplicate(Student):
    def change_name(self,name):
        print("Name:",self.name) 
        self.name = name

obj = Duplicate("John",20)
print(obj.name)   #accessing public variable
obj.change_name("Jane") 
print(obj.name)   #modified varibale            

