import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
dic = {}
for _ in range(N):
    x, y = list(map(int, input().split()))
    dic[x] = y

for _ in range(M):
    u, v = list(map(int, input().split()))
    dic[u] = v

cost = [float('inf') for _ in range(101)]
dq = deque()
dq.append(1)
cost[1] = 0

while dq:
    cur = dq.popleft()
    for i in range(6, -1, -1):
        new = cur + i
        if new in dic:
            new = dic[new]
        if new < 101 and cost[new] > cost[cur]+1:
            cost[new] = cost[cur]+1
            dq.append(new)

print(cost[100])