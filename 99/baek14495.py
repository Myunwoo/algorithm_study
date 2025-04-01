import sys
n = int(sys.stdin.readline())

arr = [0 for _ in range(117)]
arr[1] = 1
arr[2] = 1
arr[3] = 1

for i in range(4, 117):
    arr[i] = arr[i-1] + arr[i-3]

print(arr[n])