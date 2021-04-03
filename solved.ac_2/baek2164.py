#https://www.acmicpc.net/problem/2164

from collections import deque

N = int(input())

pack = deque()

for i in range(1, N+1):
    pack.append(i)

flag = True

while len(pack) != 1:
    if flag == True:
        pack.popleft()
        flag = False
    else:
        pack.append(pack.popleft())
        flag = True

print(pack[0])