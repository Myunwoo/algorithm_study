import sys
import math
from collections import Counter

n = int(sys.stdin.readline())

nums = []

avg = 0
center = math.floor(n / 2)

for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
    avg += num / n

#nums를 정렬
nums.sort()

def most_frequent(nums):
    arr_frq = Counter(nums).most_common()
    if len(arr_frq) > 1:
        if arr_frq[0][1] == arr_frq[1][1]:
            return arr_frq[1][0]
        else:
            return arr_frq[0][0]
    else:
        return arr_frq[0][0]


print(round(avg))
print(nums[center])
print(most_frequent(nums))
print(nums[len(nums)-1] - nums[0])