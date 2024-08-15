def merge_float_arrays(arr1, arr2):
    return arr1 + arr2
def get_float_array_input(prompt):
    return list(map(float, input(prompt).split()))
print("Enter the elements of the first float array separated by spaces:")
array1 = get_float_array_input("Array 1: ")
print("Enter the elements of the second float array separated by spaces:")
array2 = get_float_array_input("Array 2: ")
merged_array = merge_float_arrays(array1, array2)
print(f"The merged float array is: {merged_array}")
