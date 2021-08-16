#https://www.acmicpc.net/problem/14235
from heapq import heapify,heappop,heappush
import sys

N=int(sys.stdin.readline())
presents=[]
results=[]
for _ in range(N):
    a=list(map(int,sys.stdin.readline().strip().split()))
    #아이를 만난 경우
    if a[0]==0:
        if presents:
            p=heappop(presents)
            results.append(p[1])
        else:
            results.append(-1)
    #선물이 있는 경우
    else:
        for i in range(1,len(a)):
            heappush(presents,[-a[i],a[i]])

for r in results:
    print(r)