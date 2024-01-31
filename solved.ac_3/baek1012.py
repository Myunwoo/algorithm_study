import sys
from collections import deque
input = sys.stdin.readline

def bfs(N, M, yard, n, m):
    dq = deque()
    dq.append([n, m])
    yard[n][m] = 0
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]
    while dq:
        curN, curM = dq.popleft()
        for i in range(4):
            newN = curN + dn[i]
            newM = curM + dm[i]
            if 0 <= newN < N and 0 <= newM < M and yard[newN][newM] == 1:
                dq.append([newN, newM])
                yard[newN][newM] = 0


T = int(input())
answer = []
for _ in range(T):
    count = 0
    M, N, K = list(map(int, input().split()))
    yard = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = list(map(int, input().split()))
        yard[y][x] = 1
    
    for n in range(N):
        for m in range(M):
            if yard[n][m] == 1:
                count += 1
                bfs(N, M, yard, n, m)
    answer.append(count)

for a in answer:
    print(a)