import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [[-1 for _ in range(N)] for _ in range(N)]
costs = [sys.maxsize for _ in range(N)]

for _ in range(N-1):
    A, B, C = list(map(int, sys.stdin.readline().strip().split()))
    graph[A-1][B-1] = C
    graph[B-1][A-1] = C

costs[0] = 0
dq = deque()
dq.append(0)

while dq:
    cur = dq.popleft()
    curCost = costs[cur]
    for i in range(N):
        if i == cur:
            continue
        if graph[cur][i] > -1 and  curCost + graph[cur][i] < costs[i]:
            costs[i] = curCost + graph[cur][i]
            dq.append(i)

print(max(costs))