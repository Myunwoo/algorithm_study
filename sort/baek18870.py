#https://www.acmicpc.net/problem/18870

import sys

N = int(sys.stdin.readline().strip())

nums = []

nums = list(map(int, sys.stdin.readline().strip().split()))

for i in range(len(nums)):
    nums[i] = (nums[i], i)

nums.sort(key=lambda x:x[0])

zip = 0

for i in range(len(nums)):
    if i > 0 and nums[i][0] == nums[i-1][0]:
        zip -= 1
    nums[i] = (nums[i][0], nums[i][1], zip)
    zip += 1

nums.sort(key=lambda x:x[1])

for i in range(len(nums)):
    print(nums[i][2], end=" ")