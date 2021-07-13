#https://www.acmicpc.net/problem/1182

import sys
from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count=0
for i in range(1, N+1):
    com = list(combinations(nums, i))
    for c in com:
        if sum(c) == S:
            count+=1

print(count)