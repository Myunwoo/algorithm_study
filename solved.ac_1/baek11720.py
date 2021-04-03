#https://www.acmicpc.net/problem/11720

N = int(input())
nums = list(input())

result = 0

for num in nums:
    result += int(num)

print(result)