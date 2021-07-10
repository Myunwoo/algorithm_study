#https://www.acmicpc.net/problem/3273

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

start = 0
end = n-1
count = 0

while start < end:
    tmp = nums[start] + nums[end]
    if tmp == x:
        count += 1
        start+=1
    elif tmp > x:
        end -= 1
    elif tmp < x:
        start += 1

print(count)