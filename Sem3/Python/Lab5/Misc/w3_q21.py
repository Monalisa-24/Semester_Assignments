from collections import Counter
def find_duplicates_and_frequencies(arr):
    frequency = Counter(arr)
    duplicates = {element: freq for element, freq in frequency.items() if freq > 1}
    return duplicates
try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    duplicates = find_duplicates_and_frequencies(numbers)
    if duplicates:
        print("Duplicate elements and their frequencies:")
        for element, freq in duplicates.items():
            print(f"Element {element} occurs {freq} times.")
    else:
        print("No duplicate elements found.")
except ValueError:
    print("Invalid input. Please enter a list of integers separated by spaces.")
