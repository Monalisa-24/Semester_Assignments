def prime_numbers(number):
    count = 0
    flag = True

    for i in range(2, number+1):
        if number % i == 0:
            count+=1

    if count>1:
        flag = False
        return flag
    else:
        flag = True
        return flag
    



def prime_number_series(startRange, endRange):
    for i in range(startRange, endRange+1):
        prime = prime_numbers(i)
        if(prime):
            print(i, end=" ")

startRange = int(input("Enter the startRange: "))
endRange = int(input("Enter the endRange: "))

if startRange>1:    
    prime_number_series(startRange, endRange)
else:
    print("Please enter a valid start range. It should be > 1.")




# number = int(input("\nEnter a number to check prime or not: "))

# if number == 0 or number == 1:
#     print(f"{number} is not a prime number.")
# elif number < 0:
#     print(f"{number} is a negative number.")
# else:
#     if(prime_numbers(number)):
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number")


