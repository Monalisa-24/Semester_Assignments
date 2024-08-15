def find_second_highest(arr):
    if len(arr) < 2:
        return "Array should contain at least two elements."
    unique_elements = set(arr)
    if len(unique_elements) < 2:
        return "Array should contain at least two distinct elements."
    highest = max(unique_elements)
    unique_elements.remove(highest)
    second_highest = max(unique_elements)
    return second_highest
try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    result = find_second_highest(numbers)
    print(f"The second highest element is: {result}")
except ValueError:
    print("Invalid input. Please enter a list of integers separated by spaces.")

