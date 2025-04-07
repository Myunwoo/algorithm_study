import sys
N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
result = sys.maxsize
s = 0
while True:
    if s >= S:
        result = min(result, right-left)
        s -= nums[left]
        left+=1
    elif right == N:
        break
    else:
        s += nums[right]
        right+=1


if result == sys.maxsize:
    print(0)
else:
    print(result)