number = int(input("Take a number to check if the number is perfect number or a armstrong number : "))

def perfectNumber(n):
    sum = 0
    for i in range(1, n):
        if n%i == 0:
            sum = sum+i
    
    if(n == sum):
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")


def armstrongNumber(n):
    n1 = n
    count = 0
    while(n != 0):
        digit = n%10
        count+=1
        n//=10

    # print(f"Length of the number is  : {count}")

    n = n1
    sum = 0
    while(n != 0):
        digit = n%10
        sum += (digit**count)
        n//=10


    # print(f"Sum is : {sum}")

    if(n1 == sum):
        print(f"{n1} is an armstrong number.")
    else:
        print(f"{n1} is not an armstrong number.")



perfectNumber(number)
armstrongNumber(number)