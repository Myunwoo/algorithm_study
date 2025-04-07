#https://www.acmicpc.net/problem/10773
import sys
K=int(sys.stdin.readline())
stack=[]
for _ in range(K):
    i=int(sys.stdin.readline())
    if i==0 and stack:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))