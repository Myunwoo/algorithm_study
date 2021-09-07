#https://www.acmicpc.net/problem/6198
import sys
N=int(sys.stdin.readline())
heights=[]
for _ in range(N):
    heights.append(int(sys.stdin.readline()))

count=0
stack=[]
for h in heights:
    while stack:
        #stack의 꼭대기에 있는 것이 h보다 작다 = 꼭대기 건물은 h건물을 볼 수가 없다.
        if stack[-1] <= h:
            stack.pop()
        else:
            break
    stack.append(h)
    count+=len(stack)-1

print(count)