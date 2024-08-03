def factorial(n):
    return 1 if n==0 or n==1 else n*factorial(n-1)

def sum_of_sin_series(x, n):
    sum = 0
    for i in range(n):
        sum += ((-1**i)*(x**(2*i+1)))/factorial(2*i+1)
    return sum


x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))
print(f"Sinx = {sum_of_sin_series(x, n):.2f}")