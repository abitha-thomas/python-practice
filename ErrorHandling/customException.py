class DrivingError(Exception):
    pass
age = int(input("Enter your age:"))
if age < 18:
    raise DrivingError("Age must be at least 18")
print("Thanks")