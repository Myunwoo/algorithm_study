#https://www.acmicpc.net/problem/19951
import sys
N,M=map(int,sys.stdin.readline().split())
ground=list(map(int, sys.stdin.readline().strip().split()))
temp_ground=[0 for _ in range(N)]
for _ in range(M):
    a,b,k=map(int, sys.stdin.readline().split())
    temp_ground[b-1]+=k
    if a-2>=0:
        temp_ground[a-2]-=k

for i in range(len(temp_ground)-2, -1, -1):
    temp_ground[i]+=temp_ground[i+1]

for i in range(len(ground)):
    print(ground[i]+temp_ground[i],end=' ')