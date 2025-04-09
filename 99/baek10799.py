import sys
arr = list(sys.stdin.readline().strip())

count = 0
result = 0

for i in range(len(arr)):
    if arr[i] == '(':
        count += 1
    else:
        if arr[i-1] == '(':
            count -= 1
            result += count
        else:
            count -= 1
            result += 1
print(result)
