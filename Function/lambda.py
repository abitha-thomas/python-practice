def square(x):
    return x * x
print(square(5))

#single argmnt

square = lambda x:x * x
print(square(10))

#multiple Argmnt

add = lambda a,b:a+b
print(add(5,3))

# no arguments

say_hello = lambda : "Hello world"
print(say_hello()) 

discount_price = lambda price, discount: price - (price * discount/100)
print(discount_price(500,10)) 