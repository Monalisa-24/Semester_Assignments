# 1 
# 2 3 4 
# 5 6 7 8 9 

row = int(input("Enter how many rows: "))

num = 1

for i in range(1, row+1):
    column = (2*i-1)
    for j in range(1, column+1):
        print(num, end=" ")
        num+=1
    print(end="\n")