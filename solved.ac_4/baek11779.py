import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    start, end, cost = map(int, input().strip().split())
    graph[start].append((end, cost))
start, end = map(int, input().strip().split())

prev_node = [0] * (n+1)
costs = [float('inf')] * (n+1)
for i in range(n):
    prev_node[i] = -1
def dijkstra(s, e):
    heap = []
    costs[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        curCost, curPos = heapq.heappop(heap)
        for newPos, newCost in graph[curPos]:
            cost = curCost + newCost
            if cost < costs[newPos]:
                costs[newPos] = cost
                prev_node[newPos] = curPos
                heapq.heappush(heap, (cost, newPos))

dijkstra(start, end)
print(costs[end])

route = [end]
now = end
while now != start:
    now = prev_node[now]
    route.append(now)

route.reverse()
print(len(route))
print(' '.join(map(str,route)))