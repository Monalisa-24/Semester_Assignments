def calculateMedian(index, inputList):
    inputList.sort()
    print(f"Sorted order : {inputList}")
    if index%2 != 0 :
        median = inputList[(index)//2]
        print(f"Median is : {median}")
    if index%2 == 0:
        median = (inputList[(index - 1)//2]+inputList[(index)//2])/2
        print(f"Median is : {median}")



index = int(input("How many numbers do you want? : "))
inputList = []
for i in range(0, index):
    num = int(input("Take a number : "))
    inputList.append(num)

print(f"The input list is : {inputList}")
calculateMedian(index, inputList)
