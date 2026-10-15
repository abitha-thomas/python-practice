class Markerror(Exception):
    pass
try:
  mark=int(input("Enter your mark:"))
  if mark < 0:
    raise Markerror("Marks cannot be negative")

  if mark > 100:
    raise Markerror("Marks cannot be greater than 100")
except ValueError:
 print("Invalid input .Please Enter a valid Integer")



print ("Valid marks")

