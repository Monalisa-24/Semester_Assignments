def sum_of_series(n):
    sum = 0
    for i in range(1,n+1):
        if(i%2 != 0):
            sum += (1/i)
        else:
            sum -= (1/i)
    print(f"Sum of this series is : {sum:.3f}")


sum_of_series(5)