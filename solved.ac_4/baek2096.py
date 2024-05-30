N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
maxCosts = [[0, 0, 0] for _ in range(2)]
maxCosts[1] = graph[0]
minCosts = [[0, 0, 0] for _ in range(2)]
minCosts[1] = graph[0]

for i in range(1, N):
    maxCosts[0] = maxCosts[1]
    minCosts[0] = minCosts[1]
    maxCosts[1] = [0, 0, 0]
    minCosts[1] = [0, 0, 0]
    for j in range(3):
        if j == 0:
            maxCosts[1][j] = max(graph[i][j]+maxCosts[0][j], graph[i][j]+maxCosts[0][j+1])
            minCosts[1][j] = min(graph[i][j]+minCosts[0][j], graph[i][j]+minCosts[0][j+1])
        elif j == 1:
            maxCosts[1][j] = max(graph[i][j]+maxCosts[0][j-1], graph[i][j]+maxCosts[0][j], graph[i][j]+maxCosts[0][j+1])
            minCosts[1][j] = min(graph[i][j]+minCosts[0][j-1], graph[i][j]+minCosts[0][j], graph[i][j]+minCosts[0][j+1])
        elif j == 2:
            maxCosts[1][j] = max(graph[i][j]+maxCosts[0][j-1], graph[i][j]+maxCosts[0][j])
            minCosts[1][j] = min(graph[i][j]+minCosts[0][j-1], graph[i][j]+minCosts[0][j])

print(max(maxCosts[1]), min(minCosts[1]))