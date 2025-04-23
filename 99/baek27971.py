import sys
from collections import deque
N, M, A, B = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

counts = [sys.maxsize for _ in range(N+1)]
counts[0] = 0
posibleNums = [True for _ in range(N+1)]
for a in arr:
    for i in range(a[0], a[1]+1):
        posibleNums[i] = False

dq = deque()
dq.append(0)

while dq:
    cur = dq.popleft()
    curCount = counts[cur]

    newCurA = cur + A
    if newCurA == N:
        counts[newCurA] = min(curCount + 1, counts[newCurA])
    elif newCurA < N and posibleNums[newCurA] and curCount + 1 < counts[newCurA]:
        dq.append(newCurA)
        counts[newCurA] = curCount + 1
    
    newCurB = cur + B
    if newCurB == N:
        counts[newCurB] = min(curCount + 1, counts[newCurB])
    elif newCurB < N and posibleNums[newCurB] and curCount + 1 < counts[newCurB]:
        dq.append(newCurB)
        counts[newCurB] = curCount + 1

print(-1 if counts[N] == sys.maxsize else counts[N])