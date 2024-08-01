def sum(para1, para2):
    sum = para1 + para2
    return sum

try:
    num1 = int(input("Enter the number 1 : "))
    num2 = int(input("Enter the number 2 : "))

    print(f"Sum = {sum(num1, num2)}")
except ValueError:
    print("Error : Enter the correct formatted input!")