rows = int(input("Enter how many rows: "))

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(1, i):
        print(" ", end=" ")

    # Print the number
    print(i, end=" ")

    # Calculate the number of asterisks
    num_asterisks = 2 * (rows - i) - 1
    
    # Print asterisks
    for j in range(num_asterisks):
        print(" ", end=" ")
    
    # Print the number again if it's not the last row
    if num_asterisks > 0:
        print(i, end=" ")
    
    # Move to the next line
    print()
