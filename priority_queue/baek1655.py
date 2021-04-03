#https://www.acmicpc.net/problem/1655

import sys
import heapq

N = int(sys.stdin.readline().strip())

left = []
right = []
results = []

for i in range(N):
    num = int(sys.stdin.readline().strip())
    if i % 2 == 0:
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    
    #left와 right에 번갈아 가며 값을 삽입하기 때문에, left의 첫 수가 right의 첫 수보다 커지는 경우가 발생함.
    if len(right) > 0 and left[0][1] > right[0][1]:
        lv = heapq.heappop(left)
        rv = heapq.heappop(right)
        heapq.heappush(left, (-rv[1], rv[1]))
        heapq.heappush(right, (lv[1], lv[1]))
    
    results.append(left[0][1])

for result in results:
    print(result)