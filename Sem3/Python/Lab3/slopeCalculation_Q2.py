#slope of the linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 0
    return (y2 - y1)/(x2 - x1)


slope = calculate_slope(2, 2, 2, 2)
if slope == 0:
    print("Vertical Line.")
else:
    print("The slope of linear equation is : ", slope)



