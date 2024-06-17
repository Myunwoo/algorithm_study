from collections import Counter

N = int(input())
nums = list(map(int, input().split()))

left, right = 0, 1
result = 1
countArr = [0 for _ in range(10)]
countArr[nums[0]] += 1

while right < N:
    count = 0
    for i in range(10):
        if countArr[i] > 0:
            count += 1
    if count > 2:
        countArr[nums[left]] -= 1
        left += 1
    else:
        result = max(result, right-left)
        countArr[nums[right]] += 1
        right += 1

print(result)