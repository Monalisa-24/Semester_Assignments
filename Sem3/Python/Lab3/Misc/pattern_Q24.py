#       1        
#     2 1 2     
#   3 2 1 2 3  
# 4 3 2 1 2 3 4

row = int(input("Enter how many rows: "))

for i in range(1, row+1):
    for j in range(1, (row-i)+1):
        print(" ", end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")

    for j in range(2, i+1):
        print(j, end=" ")
    print()