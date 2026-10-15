def total(*numbers):
    return sum(numbers)
print(total(10,20,30,100))

#arbitarary argument with positional arguments

def student_info(name,age, *subjects):
    print("Name:", name)
    print("Age:", age)
    print("Subjects:", subjects)

student_info("Rahul",20,"Maths","Science","English")