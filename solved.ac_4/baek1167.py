import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    arr = list(map(int, input().strip().split()))
    start = arr[0]
    for i in range(1, len(arr)-1, 2):
        graph[start].append([arr[i], arr[i+1]])

def bfs(start):
    dq = deque()
    dq.append(start)
    costs = [sys.maxsize for _ in range(V+1)]
    costs[start] = 0
    while dq:
        cur = dq.popleft()
        for i in range(len(graph[cur])):
            nxtPos, nxtCost = graph[cur][i]
            if costs[nxtPos] > costs[cur] + nxtCost:
                costs[nxtPos] = costs[cur] + nxtCost
                dq.append(nxtPos)
    m = -1
    idx = -1
    for i in range(1, V+1):
        if costs[i] < sys.maxsize and costs[i] > m:
            m = costs[i]
            idx = i
    return [m, idx]

cost, node = bfs(1)
costTwo, nodeTwo = bfs(node)
print(costTwo)