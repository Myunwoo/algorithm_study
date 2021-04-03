#https://www.acmicpc.net/problem/11657

import sys
INFINITE = sys.maxsize

N, M = map(int, input().split())

vertices = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    vertices[A].append([B,C])

#노드 번호가 1부터 시작하기 때문에 인덱스 0은 사용하지 않고, 0이후부터 N개의 배열요소를 사용하겠음.
costs = [INFINITE for _ in range(N+1)]
costs[1] = 0

#모든 노드에 대해서 고려하기
for _ in range(N):
    is_update = False
    #cur노드를 하나씩 올리기
    for cur in range(1,N+1):
        if costs[cur] == INFINITE:
            continue

        #cur노드의 인접 노드 모두 탐색해보기
        for node, cost in vertices[cur]:
            #1에서 node로 가려는 값 vs 1에서 cur로 가려는 값 + cur에서 node로 가려는 값
            if costs[node] > costs[cur] + cost:
                costs[node] = costs[cur] + cost
                is_update = True
    
    if not is_update:
        break

if is_update:
    print(-1)
else:
    for i in range(2, N+1):
        if costs[i] == INFINITE:
            print(-1)
        else:
            print(costs[i])    