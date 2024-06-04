import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  graph = [list(map(int, input().strip().split())) for _ in range(2)]
  if n == 1:
    print(max(graph[0][0], graph[0][1]))
  elif n == 2:
    print(max(graph[0][0]+graph[1][1], graph[0][1]+graph[1][0]))
  else:
    