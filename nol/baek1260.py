import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())

graph = [[False for _ in range(N)] for _ in range(N)]
visited = [False for _ in range(N)]
answerDfs = []
answerBfs = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True

def dfs(V):
    if visited[V]:
        return
    answerDfs.append(V)
    visited[V] = True

    for i in range(N):
        if graph[V][i]:
            dfs(i)

def bfs(V):
    dq = deque()
    dq.append(V)
    while dq:
        curIdx = dq.popleft()
        if visited[curIdx]:
            continue
        answerBfs.append(curIdx)
        visited[curIdx] = True

        for i in range(N):
            if graph[curIdx][i]:
                dq.append(i)

def printAnswer(arr):
    for i in range(len(arr)):
        if i < len(arr)-1:
            print(arr[i]+1, end=' ')
        else:
            print(arr[i]+1)


dfs(V-1)
visited = [False for _ in range(N)]
bfs(V-1)

printAnswer(answerDfs)
printAnswer(answerBfs)