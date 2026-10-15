while True:
    print("1.Addition")
    print("2.Substarction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice=int(input("Enter Your Choice (1/2/3/4/5):"))
    if choice == '1':

        num1 = float(input("Enter the First Number:"))
        num2= float(input("Enter the Second Number:"))
        print(num1,"+",num2, "=", num1+num2)

    elif choice =='2':
            num1 = float(input("Enter the First Number:"))
            num2= float(input("Enter the Second Number:"))
            print(num1,"-",num2, "=",num1-num2)


    elif choice =='3':
            num1 = float(input("Enter the First Number:"))
            num2= float(input("Enter the Second Number:"))
            print(num1,"*",num2, "=",num1*num2)


    elif choice =='4':
          num1 = float(input("Enter the First Number:"))
          num2= float(input("Enter the Second Number:"))
          print(num1,"/",num2, "=",num1/num2)

    elif choice =='5':
            break
    else:
            print("Invalid input")
                 

                        
            
