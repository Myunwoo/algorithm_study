n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
costs = [[-1]*(i+1) for i in range(n)]
costs[0] = graph[0]

for i in range(n-1):
    for j in range(len(graph[i])):
        costs[i+1][j] = max(costs[i+1][j], graph[i+1][j]+costs[i][j])
        costs[i+1][j+1] = max(costs[i+1][j+1], graph[i+1][j+1]+costs[i][j])

print(max(costs[len(costs)-1]))