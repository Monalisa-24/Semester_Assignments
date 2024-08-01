def Factorial(parameter):
    if parameter == 0 or parameter == 1:
        return 1
    elif parameter < 0:
        return 0
    else:
        fact = 1
        while parameter > 1:
            fact *= parameter
            parameter -= 1

        return fact

print(f"12! : {Factorial(12)}")