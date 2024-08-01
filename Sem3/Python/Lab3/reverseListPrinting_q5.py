def reverse_list(fruitArray):
    rev_fruitArray = []
    length = len(fruitArray) - 1
    for i in range(length, -1, -1):
        rev_fruitArray.append(fruitArray[i])
    return rev_fruitArray


fruitArray = ["guava", "banana", "blueberry", "mango", "strawberry"]
print(fruitArray)
printRevfruitArray = reverse_list(fruitArray)
print(printRevfruitArray)