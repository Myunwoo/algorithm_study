import sys
input = sys.stdin.readline
K, N = list(map(int, input().split()))
arr = [int(input()) for _ in range(K)]

m = max(arr)
count = 0
while True:
  count = 0
  for a in arr:
    count += (a // m)
  if count == N:
    break
  m -= 1

print(m)