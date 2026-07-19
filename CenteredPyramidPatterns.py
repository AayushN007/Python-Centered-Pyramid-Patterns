# Pattern 1 - Full Star Pyramid

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i - 1):
        print("*", end=" ")
    print()


# Pattern 2 - Palindromic Number Pyramid

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


# Pattern 3 - Centered Increasing Number Pyramid

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(rows - i + 1, rows + 1):
        print(j, end=" ")
    for j in range(rows - 1, rows - i, -1):
        print(j, end=" ")
    print()


# Pattern 4 - Reverse Palindromic Number Pyramid

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" ")
    print()


# Pattern 5 - Palindromic Alphabet Pyramid

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(chr(j + 64), end=" ")
    for j in range(2, i + 1):
        print(chr(j + 64), end=" ")
    print()


# Pattern 6 - Constant Number Pyramid

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(rows, end=" ")
    print()

# Pattern 7 - Full Constant Number Pyramid

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i):
        print(rows, end=" ")
    for j in range(i - 1):
        print(rows, end=" ")
    print()