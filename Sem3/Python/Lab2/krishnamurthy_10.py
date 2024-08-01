def factorial(parameter):
    return 1 if parameter == 0 or parameter == 1 else parameter * factorial(parameter - 1)


def krishnamurthy(parameter):
    para = parameter
    sum = 0

    while parameter > 0:
        rem = parameter%10
        sum += factorial(rem)
        parameter//=10

    if(sum == para):
        return True
    else:
        return False    
    

try:
    number = int(input("Enter the number to check is it Krishnamurthy number or not ! : "))
    if(krishnamurthy(number)):
        print("Yes")
    else:
        print("No")
except ValueError:
    print("Error : Invalid format of number.")