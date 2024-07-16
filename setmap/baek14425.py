import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
S = set()
for _ in range(N):
    S.add(input().strip())
arr = [input().strip() for _ in range(M)]
count = 0
for a in arr:
    if a in S:
        count += 1
print(count)