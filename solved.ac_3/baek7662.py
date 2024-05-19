import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    hq = []
    for _ in range(k):
        operand, val = input().strip().split()
        val = int(val)
        if operand == 'I':
            heapq.heappush(hq, (val, -val))
        elif operand == 'D' and hq:
            if val == 1:
                hq.pop()
            elif val == -1:
                heapq.heappop(hq)
    
    if len(hq) > 1:
        print(hq[len(hq)-1][0], hq[0][0])
    elif len(hq) == 1:
        print(hq[0][0], hq[0][0])
    elif len(hq) == 0:
        print('EMPTY')