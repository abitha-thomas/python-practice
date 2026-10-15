#positive or negative

num= int(input("Enter a number"))
if num > 1:
    print("Positive")
elif num < 1:
    print("Negative")
else:
    print("Zero")

#Even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#child ,Teen,Adult

age =int(input("Enter your age: "))
if age < 12:
    print("child")
elif age <=18:
    print("Teen")   
else:
    print("Adult") 
   
#largest of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both numbers are equal")


# vowels or consonant

ch = input("Enter a character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

 #age 

age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior Citizen")
else:
    print("Invalid age")


# leap yr

year = int(input("Enter a year: "))
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")