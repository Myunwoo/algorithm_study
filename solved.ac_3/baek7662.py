import sys
import heapq
input = sys.stdin.readline

answer = []
T = int(input())
for _ in range(T):
    heap = []
    k = int(input())
    for _ in range(k):
        o, v = input().split()
        if o == 'I':
            heapq.heappush(heap, int(v))
        else:
            if not heap:
                continue
            if v == '1':
                heap.pop()
            else:
                heapq.heappop(heap)
    if not heap:
        answer.append('EMPTY')
    else:
        answer.append([max(heap), min(heap)])

for a in answer:
    if a != 'EMPTY':
        print(a[0], a[1])
    else:
        print(a)