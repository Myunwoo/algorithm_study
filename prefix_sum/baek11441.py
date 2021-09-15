#https://www.acmicpc.net/problem/11441
import sys
N=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().strip().split()))
for i in range(len(nums)-1):
    nums[i+1]+=nums[i]

results=[]
M=int(sys.stdin.readline())
for _ in range(M):
    s,e=map(int, sys.stdin.readline().split())
    r=nums[e-1]
    if s-2>=0:
        r-=nums[s-2]
    results.append(r)

for r in results:
    print(r)