from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(map, n, m):
            dn = [1, -1, 0, 0]
            dm = [0, 0, 1, -1]
            dq = deque()
            map[n][m] = '0'
            dq.append([n, m])
            while dq:
                curN, curM = dq.popleft()
                for i in range(4):
                    newN = curN + dn[i]
                    newM = curM + dm[i]
                    if 0 <= newN < len(map) and 0 <= newM < len(map[0]) and map[newN][newM] == '1':
                        map[newN][newM] = '0'
                        dq.append([newN, newM])

        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(grid, i, j)
                    answer += 1  
        return answer