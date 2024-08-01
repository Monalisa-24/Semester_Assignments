def check_season(month):
    month = month.upper()
    if(month == "NOVEMBER" or month == "DECEMBER" or month == "JANUARY"):
        print("Winter")
    elif(month == "FEBRUARY" or month == "MARCH" or month == "APRIL"):
        print("Spring")
    elif(month == "MAY" or month == "JUNE" or month == "JULY"):
        print("Summer")
    elif(month == "AUGUST" or month == "SEPTEMBER" or month == "OCTOBER"):
        print("Autumn")
    else:
        print("Incorrect month name.\n")


month = input("Enter the month : ")
check_season(month)

