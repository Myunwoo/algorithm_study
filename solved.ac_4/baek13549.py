import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int,input().split())
dq = deque()
dq.append(a)
costs = [sys.maxsize for _ in range(100001)]
costs[a] = 0

while dq:
    curA = dq.popleft()
    for nxtA in (curA*2, curA+1, curA-1):
        if 0 <= nxtA < 100001:
            if nxtA == curA*2 and costs[nxtA] > costs[curA]:
                costs[nxtA] = costs[curA]
                dq.append(nxtA)
            elif (nxtA == curA+1 or nxtA == curA-1) and costs[nxtA] > costs[curA] + 1:
                costs[nxtA] = costs[curA] + 1
                dq.append(nxtA)
print(costs[b])