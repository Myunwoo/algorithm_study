N = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
left, right = 0, len(arr)-1
answer = 0

while left < right:
    s = arr[left] + arr[right]
    if s == x:
        answer += 1
        left += 1
        right -= 1
    elif s > x:
        right -= 1
    elif s < x:
        left += 1

print(answer)