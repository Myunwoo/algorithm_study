#https://www.acmicpc.net/problem/1197

#모든 경로를 오름차순으로 정렬
#방문여부는 유니온파인드로 저장

import sys

def find(x):
    global parent
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    global parent
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x

#V=정점의 개수, E=간선의 개수
V, E = map(int, input().split())

#유니온 파인드를 위한 배열
parent = [i for i in range(V+1)]

maps = []

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    maps.append([A,B,C])

maps.sort(key=lambda x:x[2])

result = 0
i = 0

for i in range(E):
    start=maps[i][0]
    end=maps[i][1]
    cost=maps[i][2]
    if find(start)!=find(end):
        union(start, end)
        result += cost
        i += 1


print(result)