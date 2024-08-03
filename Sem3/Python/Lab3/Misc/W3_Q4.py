array1= [
    [1, 2, 3, 4],
    [5, 6, 7 ,8]
]

array2= [
    [5, 6, 7, 8],
    [1, 2, 3, 4]
]



sum_result = [
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

try:
    for i in range(len(array1)):
        for j in range(len(array1[0])):
            sum_result[i][j] = array1[i][j] + array2[i][j]

    print("Addition of two arrays : ")
    for result in sum_result:
        print(result)

except IndexError as e:
    print(e, " : Arrays need to be same length!")