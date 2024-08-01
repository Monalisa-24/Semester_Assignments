number = int(input("Take a number to find factors of it : "))

count = 0

print("The factors are : ")
for i in range(1, number+1):
    if(number%i == 0):
        print(i, end=" ")
        count+=1

print(f"\nSo {number} has {count} factors...")