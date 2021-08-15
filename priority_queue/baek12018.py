#https://www.acmicpc.net/problem/12018
import sys
n,m=map(int, sys.stdin.readline().split())
arr=[]
for _ in range(n):
    p,l=map(int, sys.stdin.readline().split())
    miles=list(map(int, sys.stdin.readline().split()))
    miles.sort(reverse=True)
    if (l-1) >= len(miles):
        arr.append(1)
    else:
        arr.append(miles[l-1])

arr.sort()
s=0
count=0
for a in arr:
    s+=a
    count+=1
    if s > m:
        s-=a
        count-=1
        break

print(count)