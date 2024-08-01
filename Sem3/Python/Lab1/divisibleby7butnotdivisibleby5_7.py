print("Displaying the numbers which is divisible by 7 but not divisible by 5 between 1000 and 2000")


def divisibleBy7butNotBy5(startRange, endRange):
    for num in range(startRange, endRange+1):
        if(num%7 == 0 and num%5 != 0):
            print(num, end="   ")


divisibleBy7butNotBy5(1000, 2000)

