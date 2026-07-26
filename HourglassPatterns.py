rows = 5

for i in range(1, rows + 1):
    for j in range(1, i - 1 + 1):
        print(" ", end = " ")
    for j in range(1, rows + 1 - i + 1):
        print("*", end = " ")
    for j in range(1 ,rows - i + 1):
        print("*", end = " ")
    print() 
    
for i in range(rows - 1, 1- 1 ,- 1):
    for j in range(1, i - 1 + 1):
        print(" ", end = " ")
    for j in range(1, rows + 1 - i + 1):
        print("*", end = " ")
    for j in range(1,rows - i + 1 ):
        print("*", end = " ")
    print()
    
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i - 1 + 1):
        print(" ", end = " ")
    for j in range(1, rows + 1 - i + 1):
        print(j, end = " ")
    for j in range(1 ,rows - i + 1):
        print(j, end = " ")
    print()
    
for i in range(rows - 1, 1- 1 ,- 1):
    for j in range(1, i - 1 + 1):
        print(" ", end = " ")
    for j in range(1, rows + 1 - i + 1):
        print(j,  end = " ")
    for j in range(1,rows - i + 1 ):
        print(j, end = " ")
    print()
    
