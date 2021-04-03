#https://www.acmicpc.net/problem/10845

import sys
from collections import deque

N = int(input())

dq = deque()
commands = []

for _ in range(N):
    commands.append(list(sys.stdin.readline().strip().split()))

for command in commands:
    if command[0] == "push":
        dq.append(command[1])
    elif command[0] == "pop":
        if len(dq) == 0:
            print(-1)
            continue
        print(dq.popleft())
    elif command[0] == "size":
        print(len(dq))
    elif command[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif command[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq)-1])