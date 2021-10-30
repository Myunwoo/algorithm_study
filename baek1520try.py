#https://www.acmicpc.net/problem/2141
import sys
N=int(sys.stdin.readline())

towns=[]
total=0
for i in range(N):
    town=list(map(int, sys.stdin.readline().strip().split()))
    towns.append(town)
    total+=town[1]

towns.sort(key=lambda x:x[0])
mid=total//2
if (total%2)!=0:
    mid+=1

temp=0
for x,a in towns:
    temp+=a
    if temp>=mid:
        print(x)
        break