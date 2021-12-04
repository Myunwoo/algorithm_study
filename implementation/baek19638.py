#https://www.acmicpc.net/problem/19638
import sys
import math
from heapq import heappush,heappop
N,H,T=map(int, input().split())
monsters=[]
for _ in range(N):
    heappush(monsters,int(sys.stdin.readline())*(-1))

count=0
for i in range(T):
    m=abs(heappop(monsters))
    if m==1:
        heappush(monsters,m*-1)
    elif m>=H:
        heappush(monsters,(m//2)*-1)
        count+=1
    else:
        print('YES')
        print(i)
        exit()

big=abs(heappop(monsters))
if big < H:
    print('YES')
    print(count)
else:
    print('NO')
    print(big)