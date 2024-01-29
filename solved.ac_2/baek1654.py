import sys
K, N = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in arr:
        count += i // mid
        
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)