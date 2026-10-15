try:
    no1=int(input("Enter the first number:"))
    no2=int(input("Enter the Second number:"))
    div = no1/no2
except ZeroDivisionError:
    print("You Got an Error Because you divided by zero")
except ValueError:
    print("You Got an Error Because you did not enter a number:")
else:
    print(div)
finally:
    print("Finally")
print("Thanks for using this program")                    