#https://www.acmicpc.net/problem/1449
N,L=map(int, input().split())
holes=list(map(int,input().split()))
holes.sort(reverse=True)

count=1
cover=holes.pop()-0.5+L
while holes:
    n=holes.pop()
    if n<=cover:
        continue
    else:
        count+=1
        cover=n-0.5+L

print(count)