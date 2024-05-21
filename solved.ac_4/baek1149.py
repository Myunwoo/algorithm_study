N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        graph[i][j] = graph[i][j] + min(graph[i-1][(j+1)%3], graph[i-1][(j+2)%3])

print(min(graph[len(graph)-1]))