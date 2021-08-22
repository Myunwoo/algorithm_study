#https://www.acmicpc.net/problem/2212
import sys
N=int(input())
K=int(input())
sensors=list(map(int, input().split()))

if K >= N:
    print(0)
    sys.exit()

sensors.sort()
dist=[]
for i in range(len(sensors)-1):
    dist.append(sensors[i+1]-sensors[i])
dist.sort(reverse=True)

for _ in range(K-1):
    dist.pop(0)

print(sum(dist))