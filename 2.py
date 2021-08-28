#https://www.acmicpc.net/problem/14698
import sys
from collections import deque
from heapq import heapify,heappop,heappush
Q=1000000007

results=[]
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    slimes=list(map(int, sys.stdin.readline().strip().split()))
    heapify(slimes)

    cost=1
    while len(slimes)>1:
        a=heappop(slimes)
        b=heappop(slimes)
        cost*=a*b
        heappush(slimes,a*b)


    results.append(cost%Q)

for r in results:
    print(r)