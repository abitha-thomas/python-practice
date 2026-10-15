d={"name":"Alice","age":35,"city":"Newyork"}
print(d.pop("age"))
print(d)

# popitem
d={"name":"Alice","age":35,"city":"Newyork"}  #last item remove
print(d.popitem())
print(d)

# setdefault
d={"name":"Alice","age":35,"city":"Newyork"}
print(d.setdefault("address"))
