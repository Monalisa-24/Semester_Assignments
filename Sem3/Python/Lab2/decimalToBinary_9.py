print("\nConvert Decimal to Binary\n-------------------------")

def DecimalToBinary(number):

    if number == 0:
        return 0
    else:
        binary = ""

        while number > 0:
            rem = number%2
            binary = str(rem)+binary
            number//=2
        return binary


decimal = int(input("Take a decimal number : "))
binary = DecimalToBinary(decimal)
print(f"{decimal} in Binary is : {binary}")



print("\nConvert that Binary to Decimal again\n------------------------------------")

def BinaryToDecimal(number):
    decimal = 0
    power = 0

    if number == 0:
        return 0
    else:
        while number > 0:
            rem = number%10
            decimal += rem * (2**power)
            number //=10
            power += 1
        return decimal

bin = int(binary)
print(f"{bin} in Decimal is : {BinaryToDecimal(bin)}\n")
