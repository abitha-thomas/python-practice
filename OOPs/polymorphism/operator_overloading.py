class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        print(self.marks + other.marks) 

s1 = Student(50)    
s2 = Student(70)
print("Total Marks:", s1.marks + s2.marks)     
s1.__add__(s2)
