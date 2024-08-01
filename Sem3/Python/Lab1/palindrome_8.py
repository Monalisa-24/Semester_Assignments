number = int(input("Take a number to check palindrome or not : "))
n = number

reverse = 0

while number != 0:
    digit = number % 10
    reverse = reverse*10 + digit
    number//=10


if n == reverse:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")