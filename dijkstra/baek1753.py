#https://www.acmicpc.net/problem/1753
import sys
from heapq import heappush, heappop

V, E = map(int, sys.stdin.readline().split())
first = int(sys.stdin.readline().strip())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end,cost])

INF = sys.maxsize

costs = [INF for _ in range(V+1)]
heap=[]

def dijkstra(s):
    global graph,costs,heap

    costs[s]=0
    #heap에 시작점, 비용 추가
    heappush(heap,[0, s])
    while heap:
        prev_cost, prev_node = heappop(heap)
        
        for next_node, next_cost in graph[prev_node]:
            new_cost = prev_cost + next_cost
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                heappush(heap, [new_cost, next_node])


dijkstra(first)
for i in range(1,len(costs)):
    if costs[i] == INF:
        print('INF')
    else:
        print(costs[i])