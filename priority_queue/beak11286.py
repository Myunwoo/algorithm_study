#https://www.acmicpc.net/problem/11286

import sys
import heapq

abs_heap = []
results = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x != 0:
        heapq.heappush(abs_heap, (abs(x), x))
    else:
        if not abs_heap:
            results.append((0,0))
        else:
            results.append(heapq.heappop(abs_heap))


for result in results:
    print(result[1])