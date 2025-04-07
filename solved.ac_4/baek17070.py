import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(input().strip().split()) for _ in range(N)]
costs = [[1000001 for _ in range(N)] for _ in range(N)]
costs[0][0] = 0
costs[0][1] = 0

dq = deque()
dq.append([0, 0, 0, 1, 0])

while dq:
    oneN, oneM, twoN, twoM, direction = dq.popleft()
