term = int(input("Take how many term of fibonacci series you need : "))

def fibonacci(t):
    t1, t2 = 0, 1
    count, sum = 0, 0


    print(f"Fibonacci series upto {t} is below : ")
    if t<=0:
        print("Please enter a valid term...")
    elif t == 1:
        print(t1)
        print(f"sum of the series is : {t1}")
    else:
        while count<t:        
            print(t1)
            sum += t1
            t3 = t1+t2
            t1 = t2
            t2 = t3
            count += 1
            
        print(f"sum of the series is : {sum}")


fibonacci(term)