import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

s = sum(arr[:K])
answer = s

for i in range(1, N-K+1):
    s -= arr[i-1]
    s += arr[i+K-1]
    answer = max(answer, s)

print(answer)