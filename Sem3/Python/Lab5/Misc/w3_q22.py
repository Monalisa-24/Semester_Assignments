def print_alternate_numbers(arr):
    alternate_numbers = arr[::2]  
    return alternate_numbers
try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    alternate_numbers = print_alternate_numbers(numbers)
    print("Every alternate number from the array:")
    print(alternate_numbers)
except ValueError:
    print("Invalid input. Please enter a list of integers separated by spaces.")
