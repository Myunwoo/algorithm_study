T = int(input())
from collections import deque

def bfs(A, B):
    visited = [False for i in range(10001)]
    word = ''
    dq = deque()
    dq.append((A, word))
    visited[int(A)] = True
    while dq:
        a, w = dq.popleft()
        numA = int(a)
        if numA == int(B):
            return w
        # D
        d = (numA * 2) % 10000
        if not visited[d]:
            visited[d] = True
            dq.append((str(d), w+'D'))
        # S
        s= (numA - 1) % 10000
        if numA - 1 > 0 and not visited[s]:
            visited[s] = True
            dq.append((str(s), w+'S'))
        # L
        l = numA // 1000 + (numA % 1000)*10
        if not visited[l]:
            visited[l] = True
            dq.append((str(l), w+'L'))
        # R
        r = numA // 10 + (numA % 10) * 1000
        if not visited[r]:
            visited[r] = True
            dq.append((str(r), w+'R'))


for _ in range(T):
    A, B = input().split()
    print(bfs(A, B))