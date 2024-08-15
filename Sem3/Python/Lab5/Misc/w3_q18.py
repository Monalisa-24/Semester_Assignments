def add_arrays_index_wise(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have the same length.")
    return [a + b for a, b in zip(arr1, arr2)]
def get_integer_array_input(prompt):
    return list(map(int, input(prompt).split()))
print("Enter the elements of the first integer array separated by spaces:")
array1 = get_integer_array_input("Array 1: ")
print("Enter the elements of the second integer array separated by spaces:")
array2 = get_integer_array_input("Array 2: ")
try:
    result_array = add_arrays_index_wise(array1, array2)
    print(f"The resulting array after index-wise addition is: {result_array}")
except ValueError as e:
    print(e)
