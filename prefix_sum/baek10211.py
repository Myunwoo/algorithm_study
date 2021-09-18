#https://www.acmicpc.net/problem/10211
import sys
T=int(sys.stdin.readline())
results=[]
for _ in range(T):
    N=int(sys.stdin.readline())
    arr=list(map(int, sys.stdin.readline().strip().split()))
    m=-1
    for i in range(len(arr)-1):
        arr[i+1]+=arr[i]
    marr=[]
    for i in range(len(arr)):
        for j in range(i+1):
            if i==j:
                marr.append(arr[i])
            else:
                marr.append(arr[i]-arr[j])
    results.append(max(marr))

for r in results:
    print(r)