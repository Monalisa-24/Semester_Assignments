def HCF(first, last):
    if first == 0 or last == 0:
        return first+last
    if first == last:
        return first
    
    if first > last:
        return HCF(first - last,last)
    else:
        return HCF(first, last - first)


firstNumber= int(input("Enter the first number : "))
lastNumber= int(input("Enter the last number : "))
print(f"HCF of {firstNumber} and {lastNumber} : {HCF(firstNumber, lastNumber)}")
