import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start, end = 0, max(arr)
answer = -1

while start<=end:
    mid = (end+start)//2
    count = 0
    for a in arr:
        if a > mid:
            count += mid
        else:
            count += a
    
    if count < M:
        start = mid+1
        answer = max(mid, answer)
    elif count > M:
        end = mid-1
    else:
        answer = max(mid, answer)
        break

print(answer)