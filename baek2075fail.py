#https://www.acmicpc.net/problem/2075
import sys
N=int(sys.stdin.readline())
nums=[[] for _ in range(N)]

for i in range(N):
    t=list(map(int, sys.stdin.readline().strip().split()))
    for j in range(len(t)):
        nums[j].append(t[j])

last_item=-1
for _ in range(N-1):
    m=-1
    index=-1
    for i in range(N):
        last_item=nums[i][len(nums[i])-1]
        if last_item>m:
            m=last_item
            index=i
    nums[index].pop()

result=0
for i in range(N):
    last_item=nums[i][len(nums[i])-1]
    if last_item>result:
        result=last_item

print(result)