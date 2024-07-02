import math

M = int(input())
N = int(input())
limit = 10001
arr = [True for _ in range(limit)]
arr[1] = False

for i in range(2, math.floor(limit ** 0.5)):
    if arr[i]:
        idx = i
        count = 2
        while idx*count < limit:
            arr[idx*count] = False
            count += 1

result = -1
s = 0

for i in range(M, N+1):
    if arr[i]:
        if result == -1:
            result = i
        s += i

if s == 0:
    print(-1)
else:
    print(s)
    print(result)