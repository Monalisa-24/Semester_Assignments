number = int(input("Take a number to check odd or even : "))

if number == 0:
    print(f"It is equals to ZERO.")
elif number % 2 == 0:
    print(f"{number} is a even number.")
else:
    print(f"{number} is a odd number.")