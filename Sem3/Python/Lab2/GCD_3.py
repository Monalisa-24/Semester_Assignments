def GCD(num1, num2):
    if num1 == 0 or num2 == 0:
        return num1+num2

    if num1 == num2:
        return num1
    
    if num1 > num2:
        return GCD(num1 - num2, num2)
    else:
        return GCD(num1, num2 - num1)
    

num1 = int(input("Take number 1 : "))
num2 = int(input("Take number 2 : "))

print(f"The GCD of {num1} and {num2} : {GCD(num1, num2)}")