n = int(input("Enter Number of Sides: "))
arr = [[0 for _ in range(n)] for _ in range(n)]

top, bottom, left, right = 0, n - 1, 0, n - 1
num = 1

while num <= n * n:
    for i in range(left, right + 1):
        arr[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        arr[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            arr[bottom][i] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            arr[i][left] = num
            num += 1
        left += 1

print("The Matrix: ")
for i in range(n):
    for j in range(n):
        print(f"{arr[i][j]:3d}", end=" ")
    print()