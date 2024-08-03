#  Queue using array

queue = []

def enqueue(element):
    queue.append(element)
    print(f"{element} is enqueued to the queue.")

def dequeue():
    # queue.reverse()
    element = queue.pop(0)
    print(f"{element} is dequeued from the stack.")

def peek():
    return queue[0]

def display():
    print("Displaying queue: ")
    for i in range(len(queue)):
        print(queue[i], end=" ")
    print()

while(True):
    print("\n-----------")
    print("Queue Menu:")
    print("-----------")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) == 0:
            print("First element will be pushed...")
        element = int(input("Enter the element: "))
        enqueue(element)

    if choice == 2:
        if len(queue) == 0:
            print("Queue is empty...")
        else:
            dequeue()

    if choice == 3:
        if len(queue)>0:
            print("Peek is: ",peek())
        else:
            print("Queue is empty!")

    if choice == 4:
        if len(queue) == 0:
            print("Queue is empty!\n")
        else:
            display()
        
    if choice == 5:
        exit()

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print("Invalid choice.")
