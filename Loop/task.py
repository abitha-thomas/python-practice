# #Q. Print numbers from 1 to 10 using a for loop.

# for i in range(1,11):
#     print(i)

# # Q. Print all even numbers from 1 to 50 using a for loop.

# for i in range(1,51):
#     if i % 2 ==0:
#         print(i)


# #Q. Print the sum of numbers from 1 to n (take n as input).

# n = int(input("Enter no: "))
# sum = 0
# for i in range(1, n + 1):
#     sum = sum + i
# print("Sum =", sum)

# #Q. Print each character of a string entered by the user.

# name=input("Enter a String: ")
# for i in name:
#     print(i)

# #  Q. Display the multiplication table of a number entered by the user.

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# # Q. Print numbers from 1 to 10 using a while loop.
# i = 1

# while i <= 10:
#     print(i)
#     i = i + 1

# #   Q. Print all odd numbers from 1 to 50 using a while loop.
# i = 1

# while i <= 50:
#     if i % 2 != 0:
#         print(i)

#     i = i + 1
# #Q. Compute the sum of digits of a number entered by the user.
# n = int(input("Enter a number: "))

# sum = 0

# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10

# print("Sum =", sum)

# Q. Reverse a number entered by the user using a while loop.
# n = int(input("Enter a number: "))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print(reverse)

# # Q. Calculate the factorial of a number using a loop.

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial =", factorial)


# Q. Find the largest number from a list entered by the user using a loop.

# numbers = list(map(int, input("Enter numbers: ").split()))
# largest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i
# print("Largest number =", largest)

# Q. Count the number of vowels in a string entered by the user.

text = input("Enter a string: ")
count = 0
for i in text:
    if i in "aeiou":
        count = count + 1
print("Number of vowels =", count)

# Q. Print the square of each number in a list using a loop.
# numbers = [2, 4, 6, 8]
# for i in numbers:
#     print(i ** 2)