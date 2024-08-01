print("print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3.\n")

firstTerm = int(input("Take the first term : "))
commonRatio = int(input("Take the common ratio : "))
terms = int(input("Take how many terms : "))

for n in range(terms):
    term = firstTerm * (commonRatio ** n)
    print(f"Term {n+1}: {term}")
