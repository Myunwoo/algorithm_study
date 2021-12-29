#https://www.acmicpc.net/problem/14719
import sys
H,W=map(int, sys.stdin.readline().split())
blocks=list(map(int, sys.stdin.readline().strip().split()))

result=0
for i in range(1,W-1):
    leftMax=max(blocks[:i])
    rightMax=max(blocks[i+1:])
    m=min(leftMax,rightMax)
    if m>blocks[i]:
        result+=m-blocks[i]
    
print(result)