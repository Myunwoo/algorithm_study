#https://www.acmicpc.net/problem/14241
from heapq import heapify,heappop,heappush
N=int(input())
slimes=list(map(int, input().split()))

for i in range(len(slimes)):
    slimes[i]=[-slimes[i],slimes[i]]
heapify(slimes)

result=0
while len(slimes)>1:
    x=heappop(slimes)
    y=heappop(slimes)
    result+=x[1]*y[1]
    heappush(slimes,[(x[0]+y[0]),(x[1]+y[1])])

print(result)