while True:
    print("Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    try:
        choice=int(input("Enter your choice:(1/2/3/4/5):" ))
    except ValueError:
        print("you got an error because you didn't enter number")
    except:
        print("You got an error")
    else:
        if choice==1:
            try:
                num1=float(input("Enter first number: "))
                num2=float(input("Enter second number: "))
                print(num1, "+" , num2, "=",num1+num2)
            except ValueError:
                print("you got an error because you didn't enter number")
        elif choice==2:
            try:
                num1=float(input("Enter first number: "))
                num2=float(input("Enter second number: "))
                print(num1, "-" , num2, "=",num1-num2)
            except ValueError:
                print("you got an error because you didn't enter number")
        elif choice==3:
            try:
                num1=float(input("Enter first number: "))
                num2=float(input("Enter second number: "))
                print(num1, "*" , num2, "=",num1*num2)
            except ValueError:
                print("you got an error because you didn't enter number")
        elif choice==4:
            try:
                num1=float(input("Enter first number: "))
                num2=float(input("Enter second number: "))
                print(num1, "/" , num2, "=",num1/num2)
            except ValueError:
                print("you got an error because you didn't enter number")
            except ZeroDivisionError:
                print("You got an error because you divided by zero")                    
        elif choice==5:
            break