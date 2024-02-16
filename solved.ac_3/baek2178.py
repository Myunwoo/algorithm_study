import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [list(input().rstrip()) for _ in range(N)]
costs = [[float('inf') for _ in range(M)] for _ in range(N)]

dq = deque()
dq.append([0, 0])
costs[0][0] = 0

dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

while dq:
  curN, curM = dq.popleft()
  curCost = costs[curN][curM]
  for i in range(4):
    newN = curN + dn[i]
    newM = curM + dm[i]
    if 0 <= newN < N and 0 <= newM < M and costs[newN][newM] > curCost+1 and graph[newN][newM] == '1':
      costs[newN][newM] = curCost + 1
      dq.append([newN, newM])
  # for c in costs:
  #   print(c)
  # print()

print(costs[N-1][M-1]+1)