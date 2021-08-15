#https://www.acmicpc.net/problem/1417
import sys
from heapq import heapify,heappop,heappush

N=int(sys.stdin.readline())
dasom=0
others=[]
for i in range(N):
    if i==0:
        dasom=int(sys.stdin.readline())
    else:
        n=int(sys.stdin.readline())
        others.append([-n,n])

heapify(others)
count=0
while True and others:
    p=heappop(others)
    #다른 후보자 중 최대가 다솜보다 작은 경우 끝
    if dasom > p[1]:
        break
    else:
        p[0]+=1
        p[1]-=1
        dasom+=1
        count+=1
        heappush(others,p)

print(count)