#https://www.acmicpc.net/problem/1916
import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

costs = [sys.maxsize for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
heap = []

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end, cost])

S, E = map(int, sys.stdin.readline().split())

def dijkstra(s):
    global costs, graph, heap

    costs[s] = 0
    heappush(heap,[0, s])
    while heap:
        prev_cost, prev_node = heappop(heap)
        if costs[prev_node] < prev_cost:
            continue
        for next_node, next_cost in graph[prev_node]:
            new_cost = prev_cost + next_cost
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                heappush(heap,[new_cost, next_node])

dijkstra(S)
print(costs[E])