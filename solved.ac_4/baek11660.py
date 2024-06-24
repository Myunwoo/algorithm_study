import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(1, N):
    graph[i][0] += graph[i-1][0]
    graph[0][i] += graph[0][i-1]

for i in range(1, N):
    for j in range(1, N):
        graph[i][j] += (graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1])

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().strip().split())
    result = graph[x2-1][y2-1]
    if x1>1:
        result -= graph[x1-2][y2-1]
    if y1>1:
        result -= graph[x2-1][y1-2]
    if x1>1 and y1>1:
        result += graph[x1-2][y1-2]
    print(result)