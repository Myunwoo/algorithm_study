import sys
input = sys.stdin.readline
import heapq

N, M, X = map(int, input().strip().split())
graph = [[] for _ in range(N)]
distance = [float('inf') for _ in range(N)]

for _ in range(M):
    start, end, time = map(int, input().strip().split())
    graph[start-1].append([end-1, time])

def dijkstra(s):
    visited = [float('inf') for _ in range(N)]
    heap = []
    heapq.heappush(heap, (0, s))
    visited[s] = 0

    while heap:
        # 현재 노드 cur, cur까지 오는 비용 dist
        dist, cur = heapq.heappop(heap)
        # cur과 연결된 노드로의 이동
        for target, val in graph[cur]:
            # 현재까지 조사된 target으로 이동하는 비용보다, cur노드에서 target으로 이동하는 비용이 작을 때
            if dist+val < visited[target]:
                visited[target] = dist+val
                heapq.heappush(heap, (visited[target], target))
    return visited

arr = dijkstra(X-1)
dic = {}
for i in range(N):
    dic[i] = arr[i]

result = -1
for i in range(N):
    if i != X-1:
        result = max(result, dic[i]+dijkstra(i)[X-1])     
print(result)