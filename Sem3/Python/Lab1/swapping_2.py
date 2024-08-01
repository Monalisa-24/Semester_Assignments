print("Swapping two numbers : ")

a = int(input("Take a number for a : "))
b = int(input("Take a number for b : "))

print(f"Before Swapping : a = {a} and b = {b}")

a, b = b, a

print(f"After Swapping : a = {a} and b = {b}")