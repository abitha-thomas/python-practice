class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def display(self):
        return f"Name: {self.name}, Roll: {self.roll}"
s1 = Student("Rahul",101)
print(s1.display())    
            