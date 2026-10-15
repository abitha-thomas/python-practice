class Father:
    def money(self):
        print("Father has money")

class Mother:
    def care(self):
        print("Mother takes care")

class Child(Father,Mother):
    def love(self):
        print("Child loves parents")  

obj = Child()
obj.money()   #Accessing father method
obj.care()    #Accessing mother method
obj.love()    #Accessing child method         
