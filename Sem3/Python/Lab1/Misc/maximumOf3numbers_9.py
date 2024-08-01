number1 = int(input("Take a number1 : "))
number2 = int(input("Take a number2 : "))
number3 = int(input("Take a number3 : "))

if number1 > number2 and number1 > number3:
    print(f"number1 : {number1} is maximum")
elif number2 > number1 and number2 > number3:
    print(f"number2 : {number2} is maximum")
else:
    print(f"number3 : {number3} is maximum")


