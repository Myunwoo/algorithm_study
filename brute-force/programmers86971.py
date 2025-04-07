from collections import deque
import sys

def bfs(start, n, wires, visited, graph):
    dq = deque()
    dq.append(start)
    visited[start] = True
    result = 1
    while dq:
        cur = dq.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dq.append(nxt)
                result += 1
    return result
                

def calcCost(i, n, wires):
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    result = []
    for wireIdx in range(len(wires)):
        if wireIdx == i:
            continue
        start, end = wires[wireIdx]
        graph[start-1].append(end-1)
        graph[end-1].append(start-1)
    for nodeIdx in range(n):
        if not visited[nodeIdx]:
            result.append(bfs(nodeIdx, n, wires, visited, graph))
    
    return result

def solution(n, wires):
    answer = sys.maxsize
    
    for i in range(len(wires)):
        calcCost(i, n, wires)
        a, b = calcCost(i, n, wires)
        answer = min(answer, abs(a-b))
    return answer