from collections import deque

# 어떤 열에 걸쳐있는지 배열로 리턴, 해당 덩어리의 총 석유양 리턴
def bfs(n, m, visited, land, N, M, oils):
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]
    dq = deque()
    dq.append((n, m))
    count = 1
    visited[n][m] = True
    colDic = {}
    colDic[m] = True
    while dq:
        curN, curM = dq.popleft()
        
        for i in range(4):
            newN = curN + dn[i]
            newM = curM + dm[i]
            if 0<=newN<N and 0<=newM<M and not visited[newN][newM] and land[newN][newM] == 1:
                visited[newN][newM] = True
                dq.append((newN, newM))
                count += 1
                colDic[newM] = True

    for c in colDic:
        oils[c] += count

def solution(land):
    answer = 0
    N = len(land)
    M = len(land[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    oils = [0 for _ in range(len(land[0]))]
    
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j, visited, land, N, M, oils)
    
    answer = max(oils)
    
    return answer