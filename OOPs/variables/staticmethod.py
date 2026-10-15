class MathOperations:
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0
    
    @staticmethod
    def display():
        return("Welcome to MathOperations")

m1 = MathOperations()
print(m1.add(10,5))
print(m1.is_even(8))
print(m1.display())

print(MathOperations.add(10,5))
print(MathOperations.is_even(8))
print(MathOperations.display())

