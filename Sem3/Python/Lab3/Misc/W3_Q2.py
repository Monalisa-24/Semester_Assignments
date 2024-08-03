#  Stack using array

stack = []

def push(element):
    stack.append(element)
    print(f"{element} is pushed to the stack.")

def pop():
    element = stack.pop()
    print(f"{element} is popped from the stack.")

def peek():
    return stack[len(stack) - 1]

def display():
    print("Displaying stack: ")
    for i in stack:
        print(i, end=" ")
    print()
    
while(True):
    print("\n-----------")
    print("Stack Menu:")
    print("-----------")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(stack) == 0:
            print("First element will be pushed...")
        element = int(input("Enter the element: "))
        push(element)

    if choice == 2:
        if len(stack) == 0:
            print("Stack is empty...")
        else:
            pop()

    if choice == 3:
        if len(stack)>0:
            print("Peek is: ",peek())
        else:
            print("Stack is empty!")

    if choice == 4:
        if len(stack) == 0:
            print("Stack is empty!\n")
        else:
            display()
        
    if choice == 5:
        exit()

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print("Invalid choice.")
