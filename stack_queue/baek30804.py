from collections import Counter

N = int(input())
nums = list(map(int, input().split()))

left, right = 0, 0
result = 0
countArr = [0 for _ in range(10)]
countArr[nums[0]] += 1

def calcCount(left, right, countArr):
    if left == right:
        return 0
    count = 0
    for i in range(10):
        if countArr[i] > 0:
            count += 1
    return count

while right < N:
    count = calcCount(left, right, countArr)
    if count > 2:
        countArr[nums[left]] -= 1
        left += 1
    else:
        result = max(result, right-left+1)
        right+=1
        if right >= N:
            break
        countArr[nums[right]] += 1
print(result)