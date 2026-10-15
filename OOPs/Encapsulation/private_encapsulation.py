class Student:
    def __init__(self,name,age):
     self.__name = name
     self.__age = age

    def display(self):
       print("Name:", self.__name) 
       print("Age:", self.__age) 

s1 = Student("Jenish", 15)
s1.display()