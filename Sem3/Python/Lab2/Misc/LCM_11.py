def GCD(first, last):
    if first == 0 or last == 0:
        return first+last
    if first == last:
        return first
    
    if first > last:
        return GCD(first - last,last)
    else:
        return GCD(first, last - first)
    
def LCM(first, last):
    return int((first*last)/GCD(first, last))


try:
    firstNumber= int(input("Enter the first number : "))
    lastNumber= int(input("Enter the last number : "))
    if firstNumber == 0 and lastNumber == 0:
        raise ZeroDivisionError("LCM of 0, 0 can not be determined.")
    print(f"LCM of {firstNumber} and {lastNumber} : {LCM(firstNumber, lastNumber)}")
except ZeroDivisionError as ex:
    print(f"Error : {ex}")