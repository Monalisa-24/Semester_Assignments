def print_list(list):
    print("Printing list below:")
    for l in list:
        print(l)
    return list


list = ["guava", "banana", "blueberry", "mango", "strawberry"]
printList = print_list(list)
print(printList)