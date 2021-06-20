N, M = map(int, input().split())

tiles = [list(map(int,input())) for _ in range(N)]

count = 0

def dfs(x, y):
    global tiles
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if tiles[x][y] == 0:
        tiles[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count += 1

print(count)