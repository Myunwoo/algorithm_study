#https://www.acmicpc.net/problem/10866

import sys
from collections import deque

dq = deque()
results = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == "push_front":
        dq.appendleft(command[1])
    elif command[0] == "push_back":
        dq.append(command[1])
    elif command[0] == "pop_front":
        if len(dq) == 0:
            results.append(-1)
        else:
            results.append(dq.popleft())
    elif command[0] == "pop_back":
        if len(dq) == 0:
            results.append(-1)
        else:
            results.append(dq.pop())
    elif command[0] == "size":
        results.append(len(dq))
    elif command[0] == "empty":
        if len(dq) == 0:
            results.append(1)
        else:
            results.append(0)
    elif command[0] == "front":
        if len(dq) == 0:
            results.append(-1)
        else:
            results.append(dq[0])
    elif command[0] == "back":
        if len(dq) == 0:
            results.append(-1)
        else:
            results.append(dq[len(dq)-1])

for result in results:
    print(result)