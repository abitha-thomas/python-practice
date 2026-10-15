class Student:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def display(self):
        print("Name:", self._name)
        print("Age:", self._age)  

s1 = Student("Jenish",21)
s1.display()
print(s1._name)       #still accessible but not recommended    
      