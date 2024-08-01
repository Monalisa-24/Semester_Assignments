number = int(input("Take a number : "))
num = abs(number)

count = 0
while num!= 0:
    digit = num%10
    count +=1
    num//=10

print(f"The count of digits in {number} : {count}")