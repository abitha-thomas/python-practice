# file = open("test.txt",'x')
# file.close()

# f = open("test.txt","w")
# f.write("Hello World")
# f.close()

# f=open("test.txt","r")
# print(f.read())

with open("ErrorHandling/task.txt","x")as f:
    f.write("hello python")
with open("ErrorHandling/test.txt","r")as f:
    data = f.read()
    print(data)