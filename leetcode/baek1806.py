import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

answer = sys.maxsize
l = 0
r = 0
curSum = arr[0]

while l < N:
    if curSum >= S:
        answer = min(answer, r-l+1)
    
    if r == N - 1:
        l += 1
        curSum -= arr[l-1]
    elif l == r:
        r += 1
        curSum += arr[r]
    elif curSum < S:
        r += 1
        curSum += arr[r]
    elif curSum >= S:
        l += 1
        curSum -= arr[l-1]

print(0 if answer == sys.maxsize else answer)