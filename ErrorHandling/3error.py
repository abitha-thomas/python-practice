try:
    x = int("abc")
except ZeroDivisionError as e:
    print("Cannot divide by zero")

except Exception as e: # Exception is a base class for all exceptions
    print(type(e).__name__ ,":", e)


print("Thanks")