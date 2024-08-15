def count_non_zero_elements(arr):
    non_zero_count = sum(1 for x in arr if x != 0)
    return non_zero_count
try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    count = count_non_zero_elements(numbers)
    print(f"The number of non-zero elements is: {count}")
except ValueError:
    print("Invalid input. Please enter a list of integers separated by spaces.")

