#https://www.acmicpc.net/problem/2812
import sys

N,K = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().strip()))

stack=[]
k=K

for i in range(N):
    while k>0 and stack:
        if stack[-1] < nums[i]:
            stack.pop()
            k-=1
        else:
            break
    stack.append(nums[i])
    
for i in range(N-K):
    print(stack[i],end="")