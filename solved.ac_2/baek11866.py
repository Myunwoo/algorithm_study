#https://www.acmicpc.net/problem/11866

from collections import deque

N, K = map(int, input().split())

dq = deque()

for i in range(1, N+1):
    dq.append(i)

count = 1
results = []

while dq:
    if count % K == 0:
        results.append(dq.popleft())
    else:
        dq.append(dq.popleft())
    count += 1

print("<",end="")
for i in range(len(results)):
    if i == len(results) -1:
        print(results[i], end="")
        break
    print(str(results[i]) + ", ", end="")
print(">")