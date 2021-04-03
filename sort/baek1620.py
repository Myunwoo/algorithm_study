#https://www.acmicpc.net/problem/1620

import sys
from collections import Counter

N, M = map(int, input().split())

names = []

#듣
for _ in range(N):
    name = sys.stdin.readline().strip()
    names.append(name)
#보
for _ in range(M):
    name = sys.stdin.readline().strip()
    names.append(name)

names.sort()

dudbos = Counter(names).most_common()
count = 0
whos = []

for dudbo in dudbos:
    if dudbo[1] == 1:
        break
    
    count += 1
    whos.append(dudbo[0])

print(count)
for who in whos:
    print(who)    