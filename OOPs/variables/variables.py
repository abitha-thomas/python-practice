#instance variable
class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course 

s1 = Student("Jenish",15,"DA")
s2 = Student("Rahul",20,"DS")

print(s1.name,s1.age, s1.course)
print(s2.name, s2.age, s2.course)   # Rahul 20

s1.name = "Ahmed"
s1.age = 25

print(s1.name, s1.age, s1.course)   # Ahmed 25
print(s2.name, s2.age, s2.course)   # Rahul 20


# class variable
class Student:
    college_name = "Techolas College"  # Class Variable

    def __init__(self, name, age):
        self.name = name   # Instance Variable
        self.age = age
        
s1 = Student("Jenish", 15)
s2 = Student("Rahul", 20)

print(s1.name, s1.college_name)
print(s2.name, s2.college_name)

Student.college_name = "Global Institute"  # Class Variable change - for all objects

print(s1.name, s1.college_name)
print(s2.name, s2.college_name)