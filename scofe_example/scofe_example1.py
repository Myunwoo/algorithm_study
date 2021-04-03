import sys

N, K = map(int, input().split())

array = list(map(int, input().split()))

count = 0
count += (N-1) // (K-1)
if (N-1) % (K-1) != 0:
    count += 1

print(count)