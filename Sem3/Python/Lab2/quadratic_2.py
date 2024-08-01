import math

def solve_quadratic(a, b, c):
    dis = b**2 - 4*a*c
    sqrt_val = math.sqrt(abs(dis))

    if dis > 0:
        print("Real and different roots:")
        print(f"{(-b + sqrt_val) / (2*a):.2f}")
        print(f"{(-b - sqrt_val) / (2*a):.2f}")

    elif dis == 0:
        print("Real and same roots:")
        print(f"{-b / (2*a):.2f}")
    
    else:
        print("Complex roots:")
        real_part = -b / (2*a)
        imaginary_part = sqrt_val / (2*a)
        print(f"{real_part:.2f} + {imaginary_part:.2f}i")
        print(f"{real_part:.2f} - {imaginary_part:.2f}i")

try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    solve_quadratic(a, b, c)

except ValueError:
    print("Please enter valid numbers for coefficients.")
