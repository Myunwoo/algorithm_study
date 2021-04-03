#https://www.acmicpc.net/problem/4153

import sys

results = []

x, y, z = -1, -1, -1

while True:
    x, y, z = map(int, sys.stdin.readline().strip().split())
    if x==0 and y==0 and z==0:
        break
    nums = [x, y, z]
    nums.sort(reverse=True)
    if (nums[0] ** 2) == ((nums[1] ** 2) + (nums[2] ** 2)):
        results.append("right")
    else:
        results.append("wrong")

for result in results:
    print(result)