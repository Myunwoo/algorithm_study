#https://www.acmicpc.net/problem/10828

import sys

N = int(input())

stack = []
commands = []

for _ in range(N):
    commands.append(list(sys.stdin.readline().strip().split()))

for command in commands:
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
            continue
        print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[len(stack) - 1])