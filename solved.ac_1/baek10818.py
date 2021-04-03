#https://www.acmicpc.net/problem/10818
N = int(input())
nums = list(map(int, input().split()))

min = 0
max = 0

nums.sort()
min = nums[0]
nums.sort(reverse=True)
max = nums[0]

print(str(min) + " " + str(max))