#https://www.acmicpc.net/problem/9012

import sys

T = int(sys.stdin.readline().strip())

stack = []
results =  []

for _ in range(T):
    case = list(sys.stdin.readline().strip())
    for c in case:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                stack.append("error")
                break
            stack.pop()
    
    if len(stack) == 0:
        results.append("YES")
    else:
        results.append("NO")
    stack = []

for result in results:
    print(result)