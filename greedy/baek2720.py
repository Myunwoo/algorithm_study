#https://www.acmicpc.net/problem/2720
import sys
T=int(sys.stdin.readline())
Q=25
D=10
N=5
P=1

for _ in range(T):
    C=int(sys.stdin.readline())
    q=C//Q
    C%=Q
    d=C//D
    C%=D
    n=C//N
    C%=N
    p=C//P
    print(q, end=' ')
    print(d, end=' ')
    print(n, end=' ')
    print(p)