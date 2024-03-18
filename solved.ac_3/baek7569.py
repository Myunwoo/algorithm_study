from collections import deque
import sys
input = sys.stdin.readline

M, N, H = list(map(int, input().strip().split()))=
graph = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]

dh = [0, 0, 1, -1, 0, 0]
dn = [0, 0, 0, 0, 1, -1]
dm = [1, -1, 0, 0, 0, 0]

def bfs(graph, cost, h, n, m):
  dq = deque()
  dq.append((h, n, m))