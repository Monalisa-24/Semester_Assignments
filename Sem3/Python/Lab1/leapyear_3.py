year = int(input("Take an year to check leapyear or not : "))

if year%100 == 0:
    if year%400 == 0:
        print(f"{year} is a leap year, which has 366 days")
    else:
        print(f"{year} is not a leap year, which has 365 days")
else:
    if year%4 == 0:
        print(f"{year} is a leap year, which has 366 days")
    else:
        print(f"{year} is not a leap year, which has 365 days")