num=int(input("Enter first number :"))
if num % 3 == 0 and num % 5 ==0:
    print("fizzBuzz")
elif num % 3 == 0:
    print("fizz")  
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)  

      
 
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))

if a >= b and a >= c:
    print("Largest number is:", a)

elif b>=a and b >=c:
    print("largest number is:",b)

else:
    print("largest number is",c)    