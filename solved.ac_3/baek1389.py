import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(M):
  a, b = list(map(int,input().split()))
  graph[a][b] = 1
  graph[b][a] = 1

# i 점에서 출발하여
for i in range(N):
  # j 점을 거칠 때
  for j in range(N):
    if i == j:
      continue
    for idx in range(N):
      graph[i][j] = min(graph[i][j], graph[i][idx])
    