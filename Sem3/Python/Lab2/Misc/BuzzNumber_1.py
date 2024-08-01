# Buzz Number means number that ends with 7 or divisible by 7

number = int(input("Take a number to check is it Buzz number or not ? : "))
lastDigit = number%10
# print(lastDigit)
if(lastDigit == 7 or number%7 == 0):
    print(f"Yes, {number} is a Buzz Number.")
else:
    print(f"No, {number} is not a Buzz Number.")


