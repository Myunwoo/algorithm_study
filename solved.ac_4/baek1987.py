R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
route = set()
result = 0

def dfs(x, y, count):
    global ans, result, graph, route
    result = max(result, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not graph[nx][ny] in route:
            route.add(graph[nx][ny])
            dfs(nx, ny, count+1)
            route.remove(graph[nx][ny])

route.add(graph[0][0])
dfs(0, 0, 1)

print(result)