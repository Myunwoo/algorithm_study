import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

result = sum(arr[0:K])
cur = result

for i in range(K, N):
    cur = cur + arr[i] - arr[i-K]
    result = max(result, cur)

print(result)