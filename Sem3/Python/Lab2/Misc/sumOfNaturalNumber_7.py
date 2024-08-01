def Sum_NaturalNumbers(range):
    sum = 0
    i = 1
    while i <= range:
        sum += i
        i += 1
    return sum

n = int(input("Take the range : "))
print(f"Sum of {n} natural numbers : {Sum_NaturalNumbers(n)}")