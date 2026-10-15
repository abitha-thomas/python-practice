class Math:
    def add(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print(a + b + c)
        elif a != None and b !=None :
            print(a + b)
        else:
            print(a)    

obj = Math()
obj.add(10,20)
obj.add(5,10,15)

class Calc:
    def add(self, *args):
        print(sum(args))

obj = Calc()
obj.add(10,20)
obj.add(5,10,15)