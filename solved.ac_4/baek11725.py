import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(parent):
  for i in graph[parent]:
    if visited[i] == -1:
      visited[i] = parent
      dfs(i)
      

N = int(input())
graph = [[] for _ in range(N)]
visited = [-1 for _ in range(N)]

for _ in range(N-1):
  a, b = map(int, input().strip().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

dfs(0)

for i in range(1, N):
  print(visited[i]+1)