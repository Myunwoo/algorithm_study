#https://www.acmicpc.net/problem/10815

N = int(input())
sang = list(map(int, input().split()))

positive = [False for _ in range(10000001)]
negative = [False for _ in range(10000000)]

for s in sang:
    if s>=0:
        positive[s] = True
    else:
        negative[abs(s)] = True

M = int(input())
target = list(map(int, input().split()))

for t in target:
    if t >= 0:
        if positive[t]:
            print(1, end=" ")
        else:
            print(0, end=" ")
    else:
        if negative[abs(t)]:
            print(1, end=" ")
        else:
            print(0, end=" ")