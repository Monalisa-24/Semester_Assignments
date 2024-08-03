def checkMultipleOrNot(m,n):
    if m%n==0:
        return True
    else:
        return False
    

m = int(input("Entr the number: "))
n = int(input("Entr the number: "))

if(checkMultipleOrNot(m,n)):
    print(f"Yes, {m} is the multiple of {n}")
else:
    print(f"No, {m} is not the multiple of {n}")
