import math

def discriminant(a,b,c):
    return (b**2 - 4*a*c)

def _solve_quadratic_eqn_(a, b, c):
    dis = discriminant(a, b, c)

    if dis < 0:
        print("No real solutions exist")
    elif dis == 0:
        x = (-b)/(2*a)
        print(f"One real solution : ({x})")
    else:
        sqrt_discriminant = math.sqrt(dis)
        x1 = (-b + sqrt_discriminant)/(2*a)
        x2 = (-b - sqrt_discriminant)/(2*a)
        print(f"The solutions are : {(x1, x2)}")
    

_solve_quadratic_eqn_(1, -2, 1)
