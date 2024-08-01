print("Compute (a)5 to the power of 8  (b)square root of 400  (c)exponent of 5  (d)Logarithm of 625 base 5\n")

import math

# (a)
print(f"5 to the power 8 : {int(math.pow(5,8))}")
print(f"Without math.pow() : 5 to the power 8 : {5**8}\n")

# (b)
print(f"Square root of 400 : {math.sqrt(400)}\n")

# (c)
print(f"Exponent of 5 : {math.exp(5)}\n")

# (d)
print(f"Logarithm of 625 base 5 : {math.log(625, 5)}\n")
