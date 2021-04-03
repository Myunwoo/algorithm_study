#https://www.acmicpc.net/problem/1003

import sys

T = int(sys.stdin.readline().strip())
Ns = []

for _ in range(T):
    Ns.append(int(sys.stdin.readline().strip()))

fibo = [[] for _ in range(41)]

def fibonacci(num):
    global fibo
    if num == 0:
        if len(fibo[0]) == 0:
            fibo[0] = [1,0]
        return fibo[0]
    elif num == 1:
        if len(fibo[1]) == 0:
            fibo[1] = [0,1]
        return fibo[1]
    else:
        if len(fibo[num]) == 0:
            fibo[num] = [fibonacci(num-2)[0] + fibonacci(num-1)[0], fibonacci(num-2)[1] + fibonacci(num-1)[1]]
        return fibo[num]

fibonacci(40)

for N in Ns:
    print(str(fibo[N][0]) + " " + str(fibo[N][1]))