def SumOfDigits(parameter):
    sum = 0 
    while parameter > 0:
        rem = parameter%10
        sum += rem
        parameter//=10

    return sum


number = int(input("Enter a number : "))
print(f"Sum of digit : {number} = {SumOfDigits(number)}")