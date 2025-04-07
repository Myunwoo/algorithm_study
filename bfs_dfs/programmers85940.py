from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    costs = [[float('inf') for _ in range(M)] for _ in range(N)]
    dq = deque()
    dq.append([0, 0])
    costs[0][0] = 0
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]
    
    while dq:
        curN, curM = dq.popleft()
        for i in range(4):
            newN = curN + dn[i]
            newM = curM + dm[i]
            if 0<=newN<N and 0<=newM<M and maps[newN][newM] == 1 and costs[newN][newM] > costs[curN][curM] + 1:
                dq.append([newN, newM])
                costs[newN][newM] = costs[curN][curM] + 1
                
    return -1 if costs[N-1][M-1] == float('inf') else costs[N-1][M-1] + 1