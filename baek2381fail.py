#https://www.acmicpc.net/problem/2381
import sys
N=int(sys.stdin.readline())
spots=[]

for _ in range(N):
    spots.append(list(map(int, sys.stdin.readline().strip().split())))

for s in spots:
    print(s)