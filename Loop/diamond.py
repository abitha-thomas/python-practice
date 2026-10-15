rows = 5
# Upper pyramid
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

print("------------------")

# Lower pyramid
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))



    