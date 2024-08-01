term = int(input("Take how many term of prime number series you want : "))

flag = True

for num in range(2, term+1):
    for i in range(2, num):
        if num == 2:
            print(num)
        if num% i == 0:
            break
    else:
        print(num, end=" ")