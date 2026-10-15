age = int(input("Enter your age: "))
if age>=18:
    drive = input("Can you drive? (yes/no): ")
    if drive.lower() =="yes":
        print("you have license")

    else:
        print("you don't have License ")

else:
    print("You dont have eligibility for applying for license ")    