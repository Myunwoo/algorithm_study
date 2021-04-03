#https://www.acmicpc.net/problem/2562

import sys

nums = []

for _ in range(9):
    nums.append(int(input()))

max = -1
max_index = 0

for i in range(len(nums)):
    if nums[i] > max:
        max = nums[i]
        max_index = i+1

print(max)
print(max_index)