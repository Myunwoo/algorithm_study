#https://www.acmicpc.net/problem/1253

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
count = 0

for i in range(len(nums)):
    target = nums[i]
    temp = nums[:i] + nums[i + 1:]

    left, right = 0, len(temp)-1

    while left < right:
        s = temp[left] + temp[right]
        
        if s == target:
            count += 1
            break
        if s < target:
            left += 1
        elif s > target:
            right -= 1

print(count)