def multiple_of_10(start, end):
    for i in range(start, end+1):
        if(i % 10 == 0):
            print(i, end=" ")


startRange = int(input("Take the start range : "))
endRange = int(input("Take the end range : "))
n  = int(input("Take the number of which multiple you want! : "))
print(f"Multiple of {n} between {startRange} and {endRange} : ")
{multiple_of_10(startRange, endRange)}
