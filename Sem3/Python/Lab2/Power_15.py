# Write a Python program that prompts the user to enter a base number and an exponent,
# and then calculates the power of the base to the exponent. The program should not use the
# exponentiation operator (**) or the math.pow() function.


def Power(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base * Power(base, exp - 1)
    else:  # When exp < 0
        return 1 / Power(base, -exp)

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

result = Power(base, exp)
print(f"{base} to the power of {exp} is : {result}.")
