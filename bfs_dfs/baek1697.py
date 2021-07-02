#https://www.acmicpc.net/problem/1697

from collections import deque

N, K = map(int, input().split())

dq = deque()
visited = [False for _ in range(100001)];

dq.append([N, 0])

def bfs():
    global dq

    while dq:
        node = dq.popleft()
        position = node[0]
        count = node[1]

        if not visited[position]:
            visited[position] = True
            if position == K:
                return count
            for next_position in (position-1, position+1, position*2):
                if next_position < 0 or next_position > 100000:
                    continue
                dq.append([next_position, count+1])

print(bfs())