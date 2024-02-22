import sys
import heapq
input = sys.stdin.readline

answer = []
T = int(input())
for _ in range(T):
    minHeap = []
    maxHeap = []
    visited = [False for _ in range(1000001)]
    k = int(input())
    for index in range(k):
        operation, num = input().split()
        if operation == 'I':
            heapq.heappush(minHeap, (int(num), index))
            heapq.heappush(maxHeap, (int(num)*-1, index))
            visited[index] = True
        elif operation == 'D':
            if num == '1' and not maxHeap:
                v, i = heapq.heappop(maxHeap)
                visited[i] = False
            elif num == '-1' and not minHeap:
                v, i = heapq.heappop(minHeap)
                visited[i] = False

    small = float('inf')
    big = float('inf')*-1

    while minHeap:
        v, i = heapq.heappop(minHeap)
        if visited[i]:
            small = min(small, v)
            break
    
    while maxHeap:
        v, i = heapq.heappop(maxHeap)
        if visited[i]:
            big = max(big*-1, v)
            break

    print(big, small)