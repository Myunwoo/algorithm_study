n = int(input())
arr = list(map(int, input().split()))
x = int(input())

if n == 1:
    print(1 if arr[0] == x else 0)
    exit()

answer = 0
arr.sort()

left = 0
right = n-1

while left < right:
    s = arr[left] + arr[right]
    if s == x:
        answer += 1
        left += 1
        continue

    if s < x:
        left += 1
    else:
        right -= 1

print(answer)