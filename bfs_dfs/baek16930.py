import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
graph = [list(input().strip()) for _ in range(N)]
costs = [[sys.maxsize for _ in range(M)] for _ in range(N)]
startN, startM, endN, endM = map(int, input().strip().split())
costs[startN-1][startM-1] = 0

def bfs():
    global costs
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]
    dq = deque()
    dq.append([startN-1, startM-1])
    while dq:
        curN, curM = dq.popleft()
        curCost = costs[curN][curM]
        for i in range(4):
            for k in range(1, K+1):
                newN = curN + dn[i]*k
                newM = curM + dm[i]*k
                if 0<=newN<N and 0<=newM<M and graph[newN][newM] == '.' and costs[newN][newM]>curCost+1:
                    costs[newN][newM] = curCost+1
                    dq.append([newN, newM])
                elif 0<=newN<N and 0<=newM<M and graph[newN][newM] == '#':
                    break

bfs()

print(-1 if costs[endN-1][endM-1] == sys.maxsize else costs[endN-1][endM-1])