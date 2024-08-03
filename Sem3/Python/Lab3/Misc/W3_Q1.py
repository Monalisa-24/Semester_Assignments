arr = [1, 2, 3, 4, 5, 6]

sum=0
avg=0

for i in range(0,len(arr)):
    sum += arr[i]
print(f"Sum : {sum}")

avg = sum/len(arr)
print(f"Average : {avg}")