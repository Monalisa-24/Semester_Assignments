# Write a program to compute the value of Euler’s number that is used as the base of 
# natural logarithms. Use the following formula. e= 1+ 1/1! +1 /2! + 1/3+................ 1/n!


def factorial(number):
    return 1 if number == 0 or number == 1 else number*factorial(number - 1)


def Euler_Number(term):
    eulerNumber = 0
    for i in range(term):
        eulerNumber += 1/factorial(i)
    return eulerNumber

term = int(input("How many term do you want to approximate e ? : "))
eulerNumber_value = Euler_Number(term)
print(f"Approximation of Euler's number e with {term} term is : {eulerNumber_value}")