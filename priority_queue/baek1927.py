#https://www.acmicpc.net/problem/1927

import sys
import heapq

max_heap = []
results = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if not max_heap:
            results.append(0)
        else:
            results.append(heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap,x)


for result in results:
    print(result)