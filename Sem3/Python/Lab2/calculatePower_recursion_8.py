def Power(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*Power(base, exp - 1)
    
base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

result = Power(base, exp)
print(f"{base} to the power of {exp} is : {result}.")