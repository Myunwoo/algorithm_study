import sys, math
M, N = map(int, sys.stdin.readline().split())

result = [True] * 1000001
result[1] = False

for i in range(2, math.ceil(1000001**0.5)):
    for j in range(i+i, 1000001, i):
        result[j] = False

for i in range(M, N+1):
    if result[i]:
        print(i)