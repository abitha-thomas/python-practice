class A:
    def methodA(self):
        print("Class A")

class B(A):
    def methodB(self):
        print("Class B")

class C(A):
    def methodC(self):
        print("Class C")  

class D(B,C):
    def methodD(self):
        print("Class D")  

obj = D()
obj.methodA()  # D can access methodA() from A because B and C both inherit from A
obj.methodB()  # D can access methodB() from B
obj.methodC()  # D can access methodC() from C
obj.methodD()  # D can access methodD() from D itself                          