import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print(0)
        continue
    typ = {}
    for _ in range(N):
        n, t = input().strip().split()
        if t in typ:
            typ[t].append(n)
        else:
            typ[t] = [n]
    
    s = 1
    for t in typ:
        s *= len(typ[t])+1
    s -= 1
    print(s)
