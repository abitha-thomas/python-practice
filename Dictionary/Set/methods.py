#add

fruits={"apple","banana","apple"}
fruits.add("kiwi")
print(fruits)

#clear
number={1,2,3}
number.clear()
print(number)

#discard
name={"anu","amaya","neena"}
name.discard("anu")
print(name)

#intersection
A={1,2,3}
B={2,3,4}
print(A.intersection(B))

#subset
A={1,2}
B={1,2,3}
print(A.issubset(B))

 # superset
a = {10,20,30}
b={10,20}
print(a.issuperset(b))

#pop
st={"apple","kiwi",1,5}
x=st.pop()
print(x)

#symmetric difference
A={1,2,3}
B={2,3,4}
print(A.symmetric_difference(B))

#union
A={1,2,3}
B={2,4,5}
print(A.union(B))

#update
numbers={1,2}
numbers.update({3,4,50})
print(numbers)


# operations



#  Union

a={1,2,3,4}
b={3,4,5,6}
result = a | b
print(result)

# intersection

A = {4, 5, 6, 7 }
B = {3, 4, 5, 6}
result = A & B
print(result)

# difference

A = {"apple", "banana", "orange"}
B = {"banana", "mango", "grapes"}
print(A - B)

# Symmetric Difference

A = {"apple", "banana", "orange"}
B = {"banana", "mango", "grapes"}
result = A ^ B
print(result)

# setsubset

A={1,2,3,4,5}
B={1,2,3}
print(B.issubset(A))