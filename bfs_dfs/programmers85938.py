from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def bfs(start):
        dq = deque()
        dq.append(start)
        visited[start] = True
        while dq:
            cur = dq.popleft()
            for i in range(n):
                if cur == i:
                    continue
                if computers[cur][i] == 1 and not visited[i]:
                    dq.append(i)
                    visited[i] = True
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i)
    return answer