T = int(input())
from collections import deque

def bfs(A, B):
    visited = [False for _ in range(10001)]
    word = ''
    dq = deque()
    dq.append((A, word))
    visited[A] = True
    while dq:
        a, w = dq.popleft()
        if a == B:
            return w
        # D
        d = (a * 2) % 10000
        if not visited[d]:
            visited[d] = True
            dq.append((d, w+'D'))
        # S
        s= (a - 1) % 10000
        if a - 1 > 0 and not visited[s]:
            visited[s] = True
            dq.append((s, w+'S'))
        # L
        l = a // 1000 + (a % 1000)*10
        if not visited[l]:
            visited[l] = True
            dq.append((l, w+'L'))
        # R
        r = a // 10 + (a % 10) * 1000
        if not visited[r]:
            visited[r] = True
            dq.append((r, w+'R'))


for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))